# Uses the cloudscraper library to bypass cloudflare restrictions and obtain page informaiton. 
# This is useful since the indeed page that I'm scapping uses JS which is annoying to scape.  

import requests
import cloudscraper
from bs4 import BeautifulSoup 

# Create a Cloudflare scraper instance
scraper = cloudscraper.create_scraper()
url = 'https://ca.indeed.com/viewjob?jk=8e405d106440187a&tk=1gtagip57k55q801&from=hp'

# Send a request through the get() method of cloudscrapper
response = scraper.get(url)
html_content = response.content

# Parse the HTML content using Beautiful Soup. This setps soup to be a string of HTML text. 
soup = BeautifulSoup(html_content, 'lxml')

# the find function  is applied multiple times to obtain the job title. 
# this is done by passing it through using OBJECT.find()
h1_tag = soup.find('h1', class_="icl-u-xs-mb--xs")
span_tag  = h1_tag.find ('span')
job_title = span_tag.text

print (job_title)
