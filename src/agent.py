from colorama import Fore, init
from litellm import completion

# Initialize colorama for colored terminal output
init(autoreset=True)


class Agent:
    """
    @title AI Agent Class
    @notice This class defines a simple AI agent with no function calling capabilities
    """

    def __init__(self, name, model, system_prompt="", temperature=0.1):
        """
        @notice Initializes the Agent class.
        @param model The AI model to be used for generating responses.
        @param tools A list of tools that the agent can use.
        @param available_tools A dictionary of available tools and their corresponding functions.
        @param system_prompt system prompt for agent behaviour.
        """
        self.name = name
        self.model = model
        self.temperature = temperature
        self.system_prompt = system_prompt

    def invoke(self, message):
        print(Fore.GREEN + f"\nCalling Agent: {self.name}")
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": message}
        ]
        response = completion(
            model=self.model,
            messages=messages,
            temperature=self.temperature
        )
        return response.choices[0].message.content

