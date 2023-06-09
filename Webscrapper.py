# Program which will parse page listings of a certain job description

import cloudscraper # Uses the cloudscraper library to bypass cloudflare restrictions and obtain page informaiton. 
from bs4 import BeautifulSoup 
import csv
import datetime
from datetime import date
import numpy as np


# TODO: searching through metatags of job postings 

# Parameters to adjust program behvaiour
NUMBER_OF_PAGES = 10 # indeed lists out 15 jobs per page
SEARCH_TERM = "mechanical engineer" 
LOCATION = "Vancouver"

def get_HTML (SEARCH_TERM, LOCATION,page):
    SEARCH_TERM = SEARCH_TERM.replace(" ", "+")
    url = f'https://ca.indeed.com/jobs?q={SEARCH_TERM}&l={LOCATION}&start={page}'
    print (url)
    # Send a request through the get() method of cloudscrapper
    response = scraper.get(url)
    return response.content

def parse_info(HTML):
    # parses the HTML to find the specifc container which contains the bulk of the HTML information
    soup = BeautifulSoup(HTML, 'html.parser')
    ul_element = soup.find('ul', class_='jobsearch-ResultsList css-0')
    li_elements = ul_element.find_all('li')

    # searches through each list item - individual job information - for class info
    for li in li_elements:
        jobCard = li.find('table', class_='jobCard_mainContent big6_visualChanges')
        if jobCard:
            job_data = get_job_data(jobCard)
            jobs.append(job_data)

def get_URL (jobCard):
    job_link = jobCard.find('a', attrs={'href': True})
    relavtive = job_link['href']
    return (f"indeed.com{relavtive}")

def search_metadata (metadata):
    Worktype = metadata.find ('div', class_='attribute_snippet')
    
    if Worktype == None:
        Worktype = 'N/A'
    else: 
        Worktype = Worktype.text.strip()

    return Worktype

# main script which is used to obtain all the individual pieces of job information
def get_job_data(jobCard):
    job_title = jobCard.find('h2', class_='jobTitle').text.strip()
    
    if '–' in job_title:
        job_title = job_title.replace('–', '-')

    job_company = jobCard.find ('span', class_= 'companyName').text.strip()
    job_location = jobCard.find('div', class_='companyLocation').text.strip()
    job_salary = jobCard.find('div', class_='metadata salary')
    job_URL = get_URL(jobCard)

    metadata = jobCard.find('div', class_= 'heading6 tapItem')

    if metadata != None:
        job_worktype = search_metadata (metadata)
    
    else:
        job_worktype = 'N/A'
    
    # print (f"{job_title}\n   Company: {job_company}\n   Location: {job_location}\n   Salary: {job_salary}")
    return (job_title, job_company, job_location, job_salary, job_worktype, job_URL)


# Create a Cloudflare scraper instance
scraper = cloudscraper.create_scraper()

# create a list to store the output
jobs = []

# MAIN 
# loops through job listings 
for page in range (0,NUMBER_OF_PAGES):
    HTML = get_HTML(SEARCH_TERM, LOCATION, page*10)    
    Main_job_info = parse_info(HTML)

num_jobs = len(jobs)
divider = '-' * 30

if num_jobs > 1:
    print (f"\n\n\n{divider}\n\n\nSuccessfully written to file. \n{num_jobs} jobs found.")
else:
    print (f"\n\n\n{divider}ERROR!")

# writes the output to a CSV
current_date = date.today()
CSV_title = f"{current_date}, {SEARCH_TERM}, {LOCATION}.csv"

with open(CSV_title, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company Name', 'Location', 'Salary', 'Worktype', 'Link'])
    writer.writerows(jobs)
