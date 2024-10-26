<!--
  Title: UpworkScribe AI: Automated Jobs Application on Upwork
  Description: UpworkScribe AI is an innovative, AI tool designed to automate and optimize the job application process on Upwork, enabling freelancers to efficiently apply to multiple relevant projects with personalized cover letters.
  Author: Aymen
  Keywords: Langgraph, litellm, LLAMA3, Upwork automation, automated job applications, AI cover letter generator, job scraping, freelance tools
-->

# UpworkScribe AI: Automated Jobs Application on Upwork

**UpworkScribe AI is not just a tool; it's your partner in navigating the competitive world of freelancing, helping you secure more projects and grow your freelance career. 🚀**

## Introduction

**UpworkScribe AI** is an AI tool designed to simplify and accelerate the freelance job application process on Upwork. In today's fast-paced gig economy, where opportunities can disappear within hours, this system offers freelancers a significant edge. By harnessing the power of AI and automation, it enables freelancers to efficiently apply to multiple relevant projects with personalized cover letters, maximizing their chances of securing ideal freelance opportunities.

## The Challenge of Modern Freelancing

The freelance marketplace has undergone a dramatic transformation in the digital age. While platforms like Upwork have opened up a world of opportunities, they have also intensified competition. Freelancers often find themselves spending countless hours searching for suitable projects, tailoring proposals, and crafting unique cover letters. This process can be not only time-consuming but also mentally exhausting, leading to missed opportunities and proposal fatigue.

## Enter UpworkScribe AI: Your Personal Freelance Assistant

UpworkScribe AI steps in as a game-changing solution to these challenges. It's not just a tool; it's your tireless, 24/7 freelance proposal partner. By automating the most time-consuming aspects of the job search and application process, it allows you to focus on what truly matters - preparing for client interviews and delivering outstanding work.

## Features

### Jobs Scraping and Classification

- **Continuous Job Monitoring**: The system continuously scans Upwork for new project listings of the freelancer provided job titles, ensuring freelancer stay up-to-date.
- **Intelligent Job Scoring**: Each job receives a score based on various criteria such: match with freelancer experience & skills, budget, duration, client history and past projects on the platform,etc. Only jobs scoring 7/10 or higher proceed for further analysis.

### AI Cover Letter and Interview Script Generation

- **Dynamic Cover Letter Creation**: AI crafts custom cover letters based on each job description and.
- **Personalized Content**: Tailors cover letters to reflect the user’s unique writing style, skills, and relevant experiences.
- **Interview Script and Questions**: Prepares a list of potential interview questions and a script for the freelancer, covering job-specific topics to improve interview readiness.
- **Keyword Optimization**: Incorporates job-related keywords to enhance proposal relevance and client interest.

## How It Works

1. **User Input**: The process starts with the user entering a job title.
2. **Job Scraping**: The system continuously scrapes Upwork for job listings that match the user-provided criteria, gathering relevant opportunities in real-time.
3. **Job Scoring and Filtering**: Each job is scored by AI, and only jobs with a score of 7/10 or higher are presented to the freelancer, filtering out lower-quality matches.
5. **Cover Letter and Interview Prep**: For strong job matches, the system generates:
   - A personalized cover letter emphasizing the user’s qualifications and alignment with the job.
   - A custom interview script and potential questions to prepare the user for discussions with potential clients.
6. **Review and Submission**: The generated cover letter, interview script, and questions are saved for user review, allowing for final adjustments before submission to prospective clients.

### System Flowchart

This is the detailed flow of the system:

[![](https://mermaid.ink/img/pako:eNqdlMGO2jAQhl_FMlJPoNJyKETtSiEBxGqL2rJ7Sjg49oRYBDuyHegKePc6TlKye1olUiJP8n_zz4xiXzCVDLCH94oUGXoOY4Hs9Ri9aFBoLYrSaPQoE_TMTQ47NBo9ID_aUqsG9FKcpTpUn_Wu5nwnmFuBVIBqGesK6ue8kl1r0Xf07fOX8RWF623g_wmjkGtKFENP8jyqFFzsuwm66MOPhg0uQQb0gFKpXLE_iaEZ6FvXM3DgLyUpaNeStp7RCgQoYsBhflHknBLDpUCBFAaE2XXhjWwzX9FiE0b2ftNW6Lpf3JMG8mSn-ATGgNp1Ncu7Zm191InDuRoXLwz6hH6XoKsi3g5t4chVtCUnQC3uhvuu2GUtrIOVC4JY1KE2r7ltFqU8z70BTdOhNkoewBtMJpNmPTpzZjLva_F3SGUulTcYj8dd3G_wdHbHp9PpR_F5gydJL_egdU-SPnjYuqe98EXrns764Mv_o-uFrxp81s-92WNNEsZYrwlseiXAQ3wEdSSc2dPmUiWMscngCDH27JIRdYhxLG5WR0ojt6-CYs-oEoZYyXKfYS8lubZRWTD744ec2CPr2Ly9_QPS1oVz?type=png)](https://mermaid.live/edit#pako:eNqdlMGO2jAQhl_FMlJPoNJyKETtSiEBxGqL2rJ7Sjg49oRYBDuyHegKePc6TlKye1olUiJP8n_zz4xiXzCVDLCH94oUGXoOY4Hs9Ri9aFBoLYrSaPQoE_TMTQ47NBo9ID_aUqsG9FKcpTpUn_Wu5nwnmFuBVIBqGesK6ue8kl1r0Xf07fOX8RWF623g_wmjkGtKFENP8jyqFFzsuwm66MOPhg0uQQb0gFKpXLE_iaEZ6FvXM3DgLyUpaNeStp7RCgQoYsBhflHknBLDpUCBFAaE2XXhjWwzX9FiE0b2ftNW6Lpf3JMG8mSn-ATGgNp1Ncu7Zm191InDuRoXLwz6hH6XoKsi3g5t4chVtCUnQC3uhvuu2GUtrIOVC4JY1KE2r7ltFqU8z70BTdOhNkoewBtMJpNmPTpzZjLva_F3SGUulTcYj8dd3G_wdHbHp9PpR_F5gydJL_egdU-SPnjYuqe98EXrns764Mv_o-uFrxp81s-92WNNEsZYrwlseiXAQ3wEdSSc2dPmUiWMscngCDH27JIRdYhxLG5WR0ojt6-CYs-oEoZYyXKfYS8lubZRWTD744ec2CPr2Ly9_QPS1oVz)

## Tech Stack

### **Using Langgraph** 

- For building agentic workflows, there are multiple popular frameworks available, such as CrewAI, AutoGen, or Agency Swarm. However, most of them grant full autonomy to the agents while accomplishing tasks and do not provide control over the working process of the agents.

- With Langgraph, you gain that control. You can decide when each agent or tool needs to be called, and you can add custom feedback based on the agent's output, which aids in self-improvement. Essentially, Langgraph is the best choice when you know exactly the process flow of your application, whereas other frameworks allow agents to choose the process.

- Langgraph also enables you to use an LLM only when necessary. For example, in this application, we need to scrape jobs from Upwork, which does not require an LLM call; a simple node tool suffices. In other frameworks, you would need to create an agent that calls the scraping tool through function calling, which helps reduce the application's cost.

## How to Run

### Prerequisites

- Python 3.9+
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
   GOOGLE_API_KEY=your_gemini_api_key
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