from src.utils import scrape_upwork_data

if __name__ == "__main__":
    search_query = "AI agent developer"
    number_of_jobs = 10
    job_listings = scrape_upwork_data(search_query, number_of_jobs)
    print(job_listings)
