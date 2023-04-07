# Program which will parse page listings of a certain job description

import cloudscraper # Uses the cloudscraper library to bypass cloudflare restrictions and obtain page informaiton. 
from bs4 import BeautifulSoup 
import csv

# Create a Cloudflare scraper instance
scraper = cloudscraper.create_scraper()

# Parameters to adjust program behvaiour
NUMBER_OF_JOBS = 100
SEARCH_TERM = "mechanical engineer" 

class job_data:
    def __init__ (self, title, worktype, salary, location, company):
        self.title = title
        self.worktype = worktype
        self.salary = salary
        self.locatoin = location

    def get_HTML (SEARCH_TERM, page):
        SEARCH_TERM = SEARCH_TERM.replace(" ", "+")
        url = f'https://ca.indeed.com/jobs?q={SEARCH_TERM}&start={page}'

        # Send a request through the get() method of cloudscrapper
        response = scraper.get(url)
        html_content = response.content

        # Parse the HTML content using Beautiful Soup. This setps soup to be a string of HTML text. 
        return BeautifulSoup(html_content, 'lxml')
    
    def parse(HTML):
        ul_element  = HTML.find('ul', class_='jobsearch-ResultsList css-0')
        li_elements = ul_element.find_all('li')

        # searches through each list item - individual job information - for class info
        for li in li_elements:
            jobCard = li.find ('table', class_= 'jobCard_mainContent big6_visualChanges')
            if jobCard:
                job_title = jobCard.find('h2', class_='jobTitle').text.strip()
                job_company  = jobCard.find ('span', class_= 'companyName').text.strip()
                job_location = jobCard.find('div', class_='companyLocation').text.strip()
                # job_link_element = jobCard.find('a', href=True)
                # if job_link_element:
                #     job_link = job_link_element.get('href')
                # else:
                #     job_link = None
                job_salary = jobCard.find('div', class_='metadata salary')

                # job_worktype = jobCard.find('div', class_='jobHeader').find('span', class_='jobEmploymentType').text.strip()
                print (f"{job_title}\n   Company: {job_company}\n   Location: {job_location}\n   Salary: {job_salary}")

def write_CSV():
    print ("")

def write_Markdown():
    print ("")

for page in range (0,NUMBER_OF_JOBS, 10):
    HTML = job_data.get_HTML(SEARCH_TERM, page)
    job_data.parse(HTML)