import os, json
from dotenv import load_dotenv
from colorama import Fore, Style, init
from litellm import completion

# Load environment variables from a .env file
load_dotenv()

# Initialize colorama for colored terminal output
init(autoreset=True)

class Agent:
    """
    @title AI Agent Class
    @notice This class defines an AI agent that can uses function calling to interact with tools and generate responses.
    """

    def __init__(self, name, model, tools=[], available_tools={}, system_prompt=""):
        """
        @notice Initializes the Agent class.
        @param model The AI model to be used for generating responses.
        @param tools A list of tools that the agent can use.
        @param available_tools A dictionary of available tools and their corresponding functions.
        @param system_prompt system prompt for agent behaviour.
        """
        self.name = name
        self.system_prompt = system_prompt
        self.model = model
        self.tools = tools
        self.available_tools = available_tools
        self.messages = []
        if self.system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def invoke(self, message):
        print(Fore.GREEN + f"Calling agent: {self.name}\n")
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        self.reset()
        return result

    def reset(self):
        self.messages = []
        if self.system_prompt:
            self.messages.append({"role": "system", "content": self.system_prompt})

    def execute(self):
        """
        @notice Executes the AI model to generate a response and handle tool calls if needed.
        @return The final response from the AI.
        """
        # First, call the AI to get a response
        response = self._call_llm()
        response_message = response.choices[0].message
        self.messages.append(response_message)

        try:
            tool_calls = response_message.tool_calls
            if tool_calls:
                response = self._run_tools(tool_calls)
                response_message = response.choices[0].message
        except Exception as e:
            print(Fore.GREEN + f"No tool call to process\n")
            pass
        return response_message.content

    def _run_tools(self, tool_calls):
        """
        @notice Runs the necessary tools based on the tool calls from the AI response.
        @param tool_calls The list of tool calls from the AI response.
        @return The final response from the AI after processing tool calls.
        """
        # For each tool the AI wanted to call, call it and add the tool result to the list of messages
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = self.available_tools[function_name]
            function_args = json.loads(tool_call.function.arguments)

            print(Fore.GREEN + f"Calling tool: {function_name}\n")
            print(Fore.GREEN + f"Arguments: {function_args}\n")
            function_response = function_to_call(**function_args)

            self.messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response
            })

        # Call the AI again so it can produce a response with the result of calling the tool(s)
        response = self._call_llm()
        response_message = response.choices[0].message
        self.messages.append(response_message)

        # If the AI decided to invoke a tool again, invoke it
        try:
            tool_calls = response_message.tool_calls
            if tool_calls:
                response = self._run_tools(tool_calls)
        except Exception as e:
            print(Fore.GREEN + f"No tool call to process\n")
            pass

        return response

    def _call_llm(self):
        print(Fore.GREEN + "LLM Call\n")
        response = completion(
            model=self.model,
            messages=self.messages,
            **({"tools": self.tools} if self.tools else {}),
            temperature=0.1
        )
        return response