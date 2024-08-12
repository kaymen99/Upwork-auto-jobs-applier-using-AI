import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Strip newline characters and any surrounding whitespace
        lines = [line.strip() for line in lines if line.strip()]
        return "".join(lines)

def scrape_upwork_data(search_query, num_jobs):
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    job_listings = []

    try:
        # Open Upwork job search page
        url = f'https://www.upwork.com/nx/search/jobs?q={search_query}&sort=recency&page=1&per_page={num_jobs}'
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)

        # Find job listings
        jobs = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="JobTile"]')

        # Extract and collect job details
        for job in jobs:
            try:
                title_element = job.find_element(By.CSS_SELECTOR, 'h2.job-tile-title > a')
                title = title_element.text.strip()
                link = title_element.get_attribute('href')
                description = job.find_element(By.CSS_SELECTOR, 'div[data-test="JobTileDetails"] > div > div > p').text.strip()
                
                job_info = job.find_element(By.CSS_SELECTOR, 'ul.job-tile-info-list')
                job_type = job_info.find_element(By.CSS_SELECTOR, 'li[data-test="job-type-label"]').text.strip()
                experience_level = job_info.find_element(By.CSS_SELECTOR, 'li[data-test="experience-level"]').text.strip()

                # Check for budget (fixed price or hourly)
                try:
                    budget = job_info.find_element(By.CSS_SELECTOR, 'li[data-test="is-fixed-price"]').text.strip()
                except:
                    budget = job_info.find_element(By.CSS_SELECTOR, 'li[data-test="duration-label"]').text.strip()

                job_listings.append({
                    'title': title,
                    'link': link,
                    'description': description,
                    'job_type': job_type,
                    'experience_level': experience_level,
                    'budget': budget
                })
            except Exception as e:
                print(f'Error parsing job listing: {e}')
                continue

    finally:
        # Close the browser
        driver.quit()

    return job_listings

def save_jobs_to_file(job_listings, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for job in job_listings:
            file.write(f"Title: {job['title']}\n")
            file.write(f"Link: {job['link']}\n")
            file.write(f"Description: {job['description']}\n")
            file.write(f"Job Type: {job['job_type']}\n")
            file.write(f"Experience Level: {job['experience_level']}\n")
            file.write(f"Budget: {job['budget']}\n")
            file.write("\n---\n\n")