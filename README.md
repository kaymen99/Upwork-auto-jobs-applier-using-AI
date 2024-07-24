# Automated Upwork Cover Letters Generation

Welcome to the AI-powered Upwork Cover Letters Generation System! This project leverages Langgraph and Litellm to automate the creation of personalized cover letters for job applications on Upwork.

## Table of Contents

- [Introduction](#introduction)
- [System Flowchart](#system-flowchart)
- [Key Technologies](#key-technologies)
  - [Langgraph](#using-langgraph)
  - [LiteLLM](#using-litellm)
- [Future Improvements](#future-improvements)
- [How to Run](#how-to-run)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Running the Application](#running-the-application)
  - [Customization](#customization)
- [Contributing](#contributing)

## Introduction

The AI-powered Upwork Cover Letters Generation System is designed to streamline the job application process by automating the creation of tailored cover letters. This project consists of two AI agents that collaborate to perform the following tasks:

1. **Scrape job listings from Upwork for the user-provided job title.**
2. **Classify scraped jobs to identify those that match the user's profile.**
3. **Generate personalized cover letters based on the user's writing style and the matched job description.**
4. **Save generated cover letters for review and submission.**

## System Flowchart

Below is the detailed flow of the system:

[![System Flowchart](https://mermaid.ink/img/pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA?type=png)](https://mermaid.live/edit#pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA)

## Key Technologies

### Using Langgraph

Langgraph is pivotal for building agentic workflows in this project. Unlike other frameworks like CrewAI, AutoGen, or Agency Swarm, Langgraph provides:

- **Control Over Agent Processes**: You can decide when each agent or tool needs to be called, adding custom feedback based on the agent's output, aiding in self-improvement.
- **Selective LLM Usage**: Langgraph enables the use of a Large Language Model (LLM) only when necessary, when there is a reasoning to be done. For example, scraping jobs from Upwork does not require an agent or an LLM call, in Langgraph you can set is as a tool node, reducing operations costs.

### Using LiteLLM

LiteLLM standardizes calls to over 100 LLMs, facilitating interaction with different models using a uniform input/output format, the one used by openai. This simplifies the process of switching models, making it as easy as changing the model name. Here are examples of using LiteLLM with different models:

- **Using LLAMA3 with GROQ**:
  ```python
  from litellm import completion

  response = completion(
                 model="groq/llama3-70b-8192",
                 messages=messages,
                 temperature=0.1
             )
  ```

- **Using Google Gemini**:
  ```python
  response = completion(
                 model="gemini/gemini-1.5-flash",
                 messages=messages,
                 temperature=0.1
             )
  ```

## Future Improvements

To enhance the application's performance and accuracy, consider the following improvements:

- **Expand Training Data**: Provide more example letters to the writer agent. Creating a file with multiple cover letters written in the user's style will improve the model's output.
- **Enhanced Feedback Loop**: Implement a mechanism for continuous user feedback, allowing the system to adapt and learn from the user's writing style, similar to reinforcement learning from human feedback.

## How to Run

### Prerequisites

Ensure you have the following prerequisites:

- Python 3.9+
- Tavily API key
- Groq API key (for LLAMA3)
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
   The application will start scraping job listings, classifying them, generating cover letters, and saving the results. By default, all generated cover letters are saved under the `files/cover_letter.txt` file.

2. **Test the Upwork jobs scraping tool:**
   ```sh
   python scrape_upwork_jobs.py
   ```

### Customization

- To use this automation for your profile, add your profile details to `files/profile.md` and remove the example profile.
- Customize each agent's behavior by modifying the corresponding agent prompt in the `prompts` script.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes..

### Contact

If you have any questions or suggestions, feel free to contact me at `aymenMir10001@gmail.com`.
