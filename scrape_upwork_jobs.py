from utils import scrape_upwork_data, save_jobs_to_file

if __name__ == "__main__":
    search_query = 'AI agent developer'
    job_listings = scrape_data(search_query)
    save_jobs_to_file(job_listings, 'upwork_job_listings.txt')
    print(job_listings)
