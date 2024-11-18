from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

#madebygauravmaurya2001
# Setup Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Setup Chrome driver using the Service object
service = Service(executable_path=r'c:\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)

# LinkedIn URL for job search (Modify with a valid URL)
url1 = 'https://in.linkedin.com/jobs/internship-in-noida-jobs?position=1&pageNum=0&original_referer=https%3A%2F%2Fin.search.yahoo.com%2F'
driver.get(url1)

# Scroll through jobs and extract details
companyname = []
titlename = []
job_links = []

# Wait for job listings to load
time.sleep(5)  # You can increase if needed

# Use XPath for more accurate element selection
companies = driver.find_elements(By.XPATH, "//h4[@class='base-search-card__subtitle']")
titles = driver.find_elements(By.XPATH, "//h3[@class='base-search-card__title']")
job_list = driver.find_elements(By.XPATH, "//a[@class='base-card__full-link']")

#madebygauravmaurya2001 

# Collect data
for i in range(len(job_list)):
    companyname.append(companies[i].text if i < len(companies) else "N/A")
    titlename.append(titles[i].text if i < len(titles) else "N/A")
    job_links.append(job_list[i].get_attribute('href'))

# Create a DataFrame and save to CSV
job_data = pd.DataFrame({
    'Job Title': titlename,
    'Company Name': companyname,
    'Job Link': job_links
})
job_data.to_csv('linkedin_jobs_details.csv', index=False)

# Close the browser
driver.quit()

print("Job details saved to 'linkedin_jobs_details.csv'.")
