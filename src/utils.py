import os, re, time, json
import html2text
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from playwright.sync_api import sync_playwright
import google.generativeai as genai
from .structured_outputs import (
    UpworkJobs,
    JobInformation,
    JobScores,
    CoverLetter,
    CallScript,
)
from .prompts import *

SCRAPED_JOBS_FOLDER = "./files/upwork_job_listings/"


def call_gemini_api(
    prompt: str, response_schema=None, model="gemini-1.5-flash"
) -> tuple:
    llm = genai.GenerativeModel(model)
    if response_schema is not None:
        llm = genai.GenerativeModel(
            model,
            generation_config={
                "response_mime_type": "application/json",
                "response_schema": response_schema,
            },
        )

    completion = llm.generate_content(prompt)
    usage_metadata = completion.usage_metadata
    token_counts = {
        "input_tokens": usage_metadata.prompt_token_count,
        "output_tokens": usage_metadata.candidates_token_count,
    }
    try:
        output = json.loads(completion.text)
    except json.JSONDecodeError:
        output = completion.text
    return output, token_counts


def scrape_website_to_markdown(url: str) -> str:
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context(user_agent=USER_AGENT)

        page = context.new_page()
        page.goto(url)
        html_content = page.content()

        browser.close()

    # Convert HTML to markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_tables = False
    markdown_content = h.handle(html_content)

    # Clean up excess newlines
    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
    markdown_content = markdown_content.strip()

    return markdown_content


def scrape_upwork_data(search_query, num_jobs=20):
    url = f"https://www.upwork.com/nx/search/jobs?q={search_query}&sort=recency&page=1&per_page={num_jobs}"

    markdown_content = scrape_website_to_markdown(url)
    prompt = SCRAPER_PROMPT_TEMPLATE.format(markdown_content=markdown_content)
    completion, _ = call_gemini_api(prompt, UpworkJobs)
    jobs_links_list = [job["link"] for job in completion["jobs"]]

    jobs_data = []
    for link in tqdm(jobs_links_list, desc="Scraping job pages"):
        try:
            job_page_content = scrape_website_to_markdown(link)
            prompt = SCRAPER_PROMPT_TEMPLATE.format(markdown_content=job_page_content)
            completion, _ = call_gemini_api(prompt, JobInformation)
            jobs_data.append(completion)
            time.sleep(5)
        except Exception as e:
            print(f"Error processing link {link}: {e}")

    jobs_df = process_job_info_data(jobs_data)

    return jobs_df


def process_job_info_data(jobs_data):
    def clean_client_info(text):
        if pd.isna(text):
            return text

        cleaned = (
            text.replace("\n\n", " | ")
            .replace("\n", " ")
            .replace("***", "")
            .replace("**", "")
            .replace("*", "")
            .strip()
        )

        # Remove multiple spaces
        cleaned = re.sub(r"\s+", " ", cleaned)
        # Remove multiple separators
        cleaned = re.sub(r"\|\s*\|", "|", cleaned)
        # Clean up spaces around separators
        cleaned = re.sub(r"\s*\|\s*", " | ", cleaned)

        return cleaned.strip()

    jobs_df = pd.DataFrame(jobs_data)
    jobs_df["rate"] = jobs_df["rate"].str.replace(
        r"\$?(\d+\.?\d*)\s*\n*-\n*\$?(\d+\.?\d*)", r"$\1-$\2", regex=True
    )
    jobs_df["client_infomation"] = jobs_df["client_infomation"].apply(clean_client_info)

    return jobs_df


def score_scaped_jobs(jobs_df, profile):
    jobs_dict_list = []
    for index, row in jobs_df.iterrows():
        job_dict = {
            "id": index,
            "title": row["title"],
            "experience_level": row["experience_level"],
            "job_type": row["job_type"],
            "duration": row["duration"],
            "rate": row["rate"],
            "description": row["description"],
            "client_infomation": row["client_infomation"],
        }
        jobs_dict_list.append(job_dict)

    jobs_list = [jobs_dict_list[i : i + 5] for i in range(0, len(jobs_dict_list), 5)]

    jobs_final_score = []
    for jobs in jobs_list:
        score_jobs_prompt = SCORE_JOBS_PROMPT_TEMPLATE.format(
            profile=profile, jobs=jobs
        )
        completion, _ = call_gemini_api(score_jobs_prompt, JobScores)
        jobs_final_score.extend(completion["matches"])

    # Merge the scores into jobs_df based on the index
    scores_df = pd.DataFrame(jobs_final_score)
    jobs_df["score"] = scores_df["score"]

    return jobs_df


def convert_jobs_matched_to_string_list(jobs_matched):
    jobs = []
    for _, row in jobs_matched.iterrows():
        job = f"Title: {row['title']}\n"
        job += f"Description:\n{row['description']}\n"
        jobs.append(job)
    return jobs


def generate_cover_letter(job_desc, profile):
    cover_letter_prompt = GENERATE_COVER_LETTER_PROMPT_TEMPLATE.format(
        profile=profile, job_description=job_desc
    )
    completion, _ = call_gemini_api(cover_letter_prompt, CoverLetter)
    return completion["letter"]


def generate_interview_script_content(job_desc):
    call_script_writer_prompt = GENERATE_CALL_SCRIPT_PROMPT_TEMPLATE.format(
        job_description=job_desc
    )
    completion, _ = call_gemini_api(call_script_writer_prompt, CallScript)
    return completion["script"]


def save_scraped_jobs_to_csv(scraped_jobs_df):
    os.makedirs(SCRAPED_JOBS_FOLDER, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{SCRAPED_JOBS_FOLDER}scraped_jobs_{date_str}.csv"
    scraped_jobs_df.to_csv(filename, index=False)


def read_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        return "".join(lines)
