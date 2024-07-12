from dotenv import load_dotenv
from utils import read_text_file
from graph import UpworkAutomationGraph

# Load environment variables from a .env file
load_dotenv()

if __name__ == "__main__":
    # Job title to look for
    job_title = "AI agent Developer"

    # load the freelancer profile
    profile = read_text_file("./files/profile.md")

    # run automation graph
    bot = UpworkAutomationGraph(profile)
    bot.run(job_title)