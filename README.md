# Upwork Job Cover Letters Automation

I built an AI-powered Upwork job cover letter automation system using Langgraph and Litellm. This project consists of two AI agents working together to achieve the following steps:

- **Scrape job listings from Upwork for the user provided job title.**
- **Classify scraped jobs to identify relevant opportunities.**
- **Check for job matches with freelancer profiles.**
- **Generate personalized cover letters for job applications.**
- **Save generated cover letters for review and submission.**

## System Flowchart

This is the detailed flow of the system:

[![](https://mermaid.ink/img/pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA?type=png)](https://mermaid.live/edit#pako:eNqNkE1vgzAMhv-K5XP7BzhMaqGdNK3TJMopcMgS0zA-gpzAVJX-9wVYpR12mE_-eN7Xlm-orCaM8MKyN3BO8g5CZCJzxNCzHStNDl7sB5wr31AB2-0T7ESqAk-Q9V-W63nsilW5W4C9iBvpXFVeYSX1b2a_MLGIDakaSsuL_0l6ZejBxDMzvbNV5Bx8BvEEiXimjlh6gtiO4b5X8p74R5EsrkeRyvHP-fHfW98stGt7goM4dLrADbbErax0eNVtZnP0hlrKMQqpllznmHf3wMnB2_TaKYw8D7RBtsPFPIqh1-H6pJLh3S1GpWwc3b8Bljd8zA)

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
