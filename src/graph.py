import json
from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from typing import List
from colorama import Fore, Style
from .agent import Agent
from .utils import scrape_upwork_data, save_jobs_to_file
from .prompts import classify_jobs_prompt, generate_cover_letter_prompt

SCRAPED_JOBS_FILE = "./files/upwork_job_listings.txt"
COVER_LETTERS_FILE = "./files/cover_letter.txt"


### Our graph state
class GraphState(TypedDict):
    job_title: str
    scraped_jobs_list: str
    matches: List[dict]
    job_description: str
    cover_letter: str
    num_matches: int


class UpworkAutomationGraph:
    def __init__(self, profile, num_jobs=10):
        # Freelancer profile/resume
        self.profile = profile

        # Number of jobs to collect
        self.number_of_jobs = num_jobs

        # Build agents
        self.init_agents()

        # Build graph
        self.graph = self.build_graph()

    def scrape_upwork_jobs(self, state):
        """
        Scrape jobs based on job title provided

        @param state: The current state of the application.
        @return: Updated state with scraped jobs.
        """
        job_title = state["job_title"]

        print(
            Fore.YELLOW
            + f"----- Scraping Upwork jobs for: {job_title} -----\n"
            + Style.RESET_ALL
        )
        job_listings = scrape_upwork_data(job_title, self.number_of_jobs)

        print(
            Fore.GREEN
            + f"----- Scraped {len(job_listings)} jobs -----\n"
            + Style.RESET_ALL
        )
        # write scraped jobs to txt file
        save_jobs_to_file(job_listings, SCRAPED_JOBS_FILE)
        job_listings_str = "\n".join(map(str, job_listings))
        return {**state, "scraped_jobs_list": job_listings_str}

    def classify_scraped_jobs(self, state):
        """
        Classify scraped jobs based on the profile.

        @param state: The current state of the application.
        @return: Updated state with classified jobs.
        """
        print(Fore.YELLOW + "----- Classifying scraped jobs -----\n" + Style.RESET_ALL)
        scraped_jobs = state["scraped_jobs_list"]
        classify_result = self.classify_jobs_agent.invoke(scraped_jobs)
        matches = json.loads(classify_result, strict=False)["matches"]
        return {**state, "matches": matches}

    def check_for_job_matches(self, state):
        print(
            Fore.YELLOW
            + "----- Checking for remaining job matches -----\n"
            + Style.RESET_ALL
        )
        if len(state["matches"]) == 0:
            return {**state, "num_matchs": 0}
        else:
            return {**state, "num_matchs": len(state["matches"])}

    def need_to_process_matches(self, state):
        """
        Check if there are any job matches.

        @param state: The current state of the application.
        @return: "empty" if no job matches, otherwise "process".
        """
        if len(state["matches"]) == 0:
            print(Fore.RED + "No job matches\n" + Style.RESET_ALL)
            return "No matches"
        else:
            print(
                Fore.GREEN
                + f"There are {len(state['matches'])} Job matches to process\n"
                + Style.RESET_ALL
            )
            return "Process jobs"

    def generate_cover_letter(self, state):
        """
        Generate cover letter based on the job description and the profile.

        @param state: The current state of the application.
        @return: Updated state with generated cover letter.
        """
        print(Fore.YELLOW + "----- Generating cover letter -----\n" + Style.RESET_ALL)
        matches = state["matches"]
        job_description = str(matches[-1])
        cover_letter_result = self.generate_cover_letter_agent.invoke(job_description)
        cover_letter = json.loads(cover_letter_result, strict=False)["letter"]
        # reset writer agent messages history, so each letter is unique
        self.generate_cover_letter_agent.reset()
        return {
            **state,
            "cover_letter": cover_letter,
            "job_description": job_description,
        }

    def save_cover_letter(self, state):
        """
        Save the generated cover letter to a file.

        @param state: The current state of the application.
        @return: The updated state after saving the cover letter.
        """
        print(Fore.YELLOW + "----- Saving cover letter -----\n" + Style.RESET_ALL)
        with open(COVER_LETTERS_FILE, "a") as file:
            file.write(state["cover_letter"] + f'\n{"-"*70}\n')

        # Remove already processed job
        state["matches"].pop()
        return {**state, "matches": state["matches"]}

    def init_agents(self):
        """
        Initialize agents for scraping jobs, classifying jobs, and generating cover letters.
        """
        # Using Gemini model for its longer context length
        # llama3 with Groq will hit the TPM limit and throw an error
        self.classify_jobs_agent = Agent(
            name="Job Classifier Agent",
            model="gemini/gemini-1.5-pro",
            system_prompt=classify_jobs_prompt.format(profile=self.profile),
        )
        self.generate_cover_letter_agent = Agent(
            name="Writer Agent",
            model="groq/llama3-70b-8192",
            system_prompt=generate_cover_letter_prompt.format(profile=self.profile),
        )

    def build_graph(self):
        graph = StateGraph(GraphState)

        # create all required nodes
        graph.add_node("scrape_upwork_jobs", self.scrape_upwork_jobs)
        graph.add_node("classify_scraped_jobs", self.classify_scraped_jobs)
        graph.add_node("check_for_job_matches", self.check_for_job_matches)
        graph.add_node("generate_cover_letter", self.generate_cover_letter)
        graph.add_node("save_cover_letter", self.save_cover_letter)

        # Link nodes to complete workflow
        graph.set_entry_point("scrape_upwork_jobs")
        graph.add_edge("scrape_upwork_jobs", "classify_scraped_jobs")
        graph.add_edge("classify_scraped_jobs", "check_for_job_matches")
        graph.add_conditional_edges(
            "check_for_job_matches",
            self.need_to_process_matches,
            {"Process jobs": "generate_cover_letter", "No matches": END},
        )
        graph.add_edge("generate_cover_letter", "save_cover_letter")
        graph.add_edge("save_cover_letter", "check_for_job_matches")

        return graph.compile()

    def run(self, job_title):
        print(
            Fore.BLUE + "----- Running Upwork Jobs Automation -----\n" + Style.RESET_ALL
        )
        state = self.graph.invoke({"job_title": job_title})
        return state
