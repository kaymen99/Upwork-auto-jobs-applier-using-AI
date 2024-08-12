<!--
  Title: UpworkScribe AI: Automated Jobs Application on Upwork
  Description: UpworkScribe AI is an innovative, AI tool designed to automate and optimize the job application process on Upwork, enabling freelancers to efficiently apply to multiple relevant projects with personalized cover letters.
  Author: Aymen Mir
  Keywords: Langgraph, litellm, LLAMA3, Upwork automation, automated job applications, AI cover letter generator, job scraping, freelance tools
-->

# UpworkScribe AI: Automated Jobs Application on Upwork

## Introduction

**UpworkScribe AI** is an innovative, AI-powered tool designed to revolutionize the freelance job application process on Upwork. In today's fast-paced gig economy, where opportunities can disappear within hours, this program offers freelancers a significant edge. By harnessing the power of artificial intelligence and automation, UpworkScribe AI enables users to efficiently apply to multiple relevant projects with personalized cover letters, maximizing their chances of securing ideal freelance opportunities.

## The Challenge of Modern Freelancing

The freelance marketplace has undergone a dramatic transformation in the digital age. While platforms like Upwork have opened up a world of opportunities, they have also intensified competition. Freelancers often find themselves spending countless hours searching for suitable projects, tailoring proposals, and crafting unique cover letters. This process can be not only time-consuming but also mentally exhausting, leading to missed opportunities and proposal fatigue.

## Enter UpworkScribe AI: Your Personal Freelance Assistant

UpworkScribe AI steps in as a game-changing solution to these challenges. It's not just a tool; it's your tireless, 24/7 freelance proposal partner. By automating the most time-consuming aspects of the job search and application process, it allows you to focus on what truly matters - preparing for client interviews and delivering outstanding work.

## Features

### Intelligent Job Scraping and Classification

- Customizable search criteria based on user-provided job titles
- Continuous scanning for new project listings
- Smart classification to identify jobs matching user profiles

### AI-Powered Cover Letter Generation

- Dynamic cover letter creation based on job descriptions
- Personalization aligned with user writing style
- Keyword optimization for improved proposal relevance

### Efficient Application Management

- Bulk cover letter generation for multiple projects
- Automatic saving of generated cover letters for review
- Streamlined submission process

### Advanced AI Technology

- Utilizes Langgraph for workflow orchestration
- Implements Litellm for robust language model integration

## How It Works

1. **Job Scraping**: The system scrapes Upwork for job listings based on user-provided criteria.
2. **Job Classification**: AI agents classify scraped jobs to identify the best matches for the user's freelance profile.
3. **Cover Letter Generation**: Personalized cover letters are created using AI, tailored to each job description and the user's skills, experience and writing style.
4. **Review and Submission**: Generated cover letters are saved for user review before submission.

### System Flowchart

This is the detailed flow of the system:

[![](https://mermaid.ink/img/pako:eNqdk0FvozAQhf-K5UirrZRI0eaScKiUQBulaquqNOoBejB4CFbARrZJWiX57x0H0tJbFw54Bt735hnhA00VB-rRjWZVTl6CWBK85tHagCYrWdX2jYxG18c7lZAXYQs4ksVf14QpEqCvGmBxFj2zPXHv7oWxQm7MkfgH1_sFM0ZkAi1b_w1Ie2pq_4w-MJvmwB2OWBD5aofqe7AWl1ctcOmgb110Lcsf8E0UCJMyzVtVc79ttvSkVSYKaDblfDEnCe2H21jQ1QdnxRIkaGbRuxsIhyyjZ9gJ2JM_JGQ7aEctz9C8qjSq-ZGsorBOSmGJVWRd7ZXe_hA-AnBDnJERSjYBYtkojMtE5gTTFt4gm2VDY7XagjeYTqdtPdoLbnPvX_U-TFWhtDcYj8ddfNHiSfKNTyaT3-L-ZXqS9MGDy_SsF37T4pzzPvjtJXw264Mvv758L3zV4rP_mU6HtARdMsHxRB6cXUxtDiXE1MOSM72NaSxPqGO1VeGHTKlndQ1DqlW9yamXscJgV1ccf9pAMDzWZfv09AkL_EYn?type=png)](https://mermaid.live/edit#pako:eNqdk0FvozAQhf-K5UirrZRI0eaScKiUQBulaquqNOoBejB4CFbARrZJWiX57x0H0tJbFw54Bt735hnhA00VB-rRjWZVTl6CWBK85tHagCYrWdX2jYxG18c7lZAXYQs4ksVf14QpEqCvGmBxFj2zPXHv7oWxQm7MkfgH1_sFM0ZkAi1b_w1Ie2pq_4w-MJvmwB2OWBD5aofqe7AWl1ctcOmgb110Lcsf8E0UCJMyzVtVc79ttvSkVSYKaDblfDEnCe2H21jQ1QdnxRIkaGbRuxsIhyyjZ9gJ2JM_JGQ7aEctz9C8qjSq-ZGsorBOSmGJVWRd7ZXe_hA-AnBDnJERSjYBYtkojMtE5gTTFt4gm2VDY7XagjeYTqdtPdoLbnPvX_U-TFWhtDcYj8ddfNHiSfKNTyaT3-L-ZXqS9MGDy_SsF37T4pzzPvjtJXw264Mvv758L3zV4rP_mU6HtARdMsHxRB6cXUxtDiXE1MOSM72NaSxPqGO1VeGHTKlndQ1DqlW9yamXscJgV1ccf9pAMDzWZfv09AkL_EYn)

## Benefits

- Save hours of time on proposal writing
- Increase the number of quality applications submitted
- Improve proposal relevance and personalization
- Focus energy on preparing for client interviews and project execution

**UpworkScribe AI is not just a tool; it's your partner in navigating the competitive world of freelancing, helping you secure more projects and grow your freelance career. 🚀**

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
   git clone https://github.com/kaymen99/upwork-auto-jobs-applier-using-AI.git
   cd upwork-auto-jobs-applier-using-AI
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
