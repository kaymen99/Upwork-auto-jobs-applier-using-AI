# Upwork Jobs Cover Letters Automation

I built an AI-powered Upwork jobs cover letters generation system using Langgraph and Litellm. This project consists of two AI agents working together to achieve the following steps:

- **Scrape job listings from Upwork for the user provided job title.**
- **Classify scraped jobs to identify the ones that match with user profile.**
- **Generate personalized cover letters based on user writing style and the matched job description.**
- **Save generated cover letters for review and submission.**

## System Flowchart

This is the detailed flow of the system:

[![](https://mermaid.ink/img/pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA?type=png)](https://mermaid.live/edit#pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA)

## Takeaways and Design Choices

### **Using Langgraph** 

- For building agentic workflows, there are multiple popular frameworks available, such as CrewAI, AutoGen, or Agency Swarm. However, most of them grant full autonomy to the agents while accomplishing tasks and do not provide control over the working process of the agents.

- With Langgraph, you gain that control. You can decide when each agent or tool needs to be called, and you can add custom feedback based on the agent's output, which aids in self-improvement. Essentially, Langgraph is the best choice when you know exactly the process flow of your application, whereas other frameworks allow agents to choose the process.

- Langgraph also enables you to use an LLM only when necessary. For example, in this application, we need to scrape jobs from Upwork, which does not require an LLM call; a simple node tool suffices. In other frameworks, you would need to create an agent that calls the scraping tool through function calling, which helps reduce the application's cost.

### **Using LiteLLM** 

- LiteLLM is a framework that standardizes calls to 100+ LLMs. It allows interaction with different LLMs beyond OpenAI (GPT models) using the same input/output format, simplifying the process of switching models for the application to just changing the model name.

* **Use LLAMA3 with GROQ**:
  
```python
from litellm import completion

response = completion(
               model="groq/llama3-70b-8192",
               messages=messages,
               temperature=0.1
           )
```

* **Use Google Gemini**:
  
```python
response = completion(
               model="gemini/gemini-1.5-flash",
               messages=messages,
               temperature=0.1
           )
```

### **Future Improvements** 

While the current app provides correct results, it requires further tuning to be used in real job applications.

- Currently, only two example letters are provided to the writer agent (directly in its prompt) for crafting personalized letters. This is insufficient, and it would be better to create a file containing multiple cover letters written in the user's style, which will improve the model's output.

- **Enhanced Feedback Loop**: Implement a mechanism for continuous feedback from user, allowing the model to adapt and learn from user writing style (similar to reinforcement learning from human feedback).

## How to Run

### Prerequisites

- Python 3.9+
- Tavily API key
- Groq API key (for Llama3)
- Google Gemini API key (for using Gemini model)
- Necessary Python libraries (listed in `requirements.txt`)

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kaymen99/upwork-jobs-langgraph.git
   cd upwork-jobs-langgraph
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your API keys:

   ```env
   TAVILY_API_KEY=your_tavily_api_key
   GEMINI_API_KEY=your_gemini_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

### Running the Application

1. **Start the workflow:**

   ```sh
   python main.py
   ```

   The application will start scraping job listings, classifying them, generating cover letters, and saving the results.
   
   By default at the end of the process, all the cover letters generated are saved under `files/cover_letter.txt` file.

3. You can test the Upwork jobs scraping tool by running:
   ```sh
   python scrape_upwork_jobs.py
   ```

### Customization

* To use this automation for you own profile, just add your profile into `files/profile.md` and remove the example profile.

* You can customize the behavior of each agent by modifying the corresponding agent prompt in the `prompts` script.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

### Contact

If you have any questions or suggestions, feel free to contact me at `aymenMir10001@gmail.com`.
