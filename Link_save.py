# Uses selenium to load a webpage and scrap the job title of it

# Issues: I don't understand how it works, very slow and needs to load a seperate instance of a browser to scrap it    


import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the user agent for the webdriver
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# Configure the web driver
driver = webdriver.Chrome(options=options)
url = 'https://ca.indeed.com/viewjob?jk=bb71e14877f45faa&tk=1fakhe7v5ouac801'
#driver.implicitly_wait(0.1)
driver.get(url)

# Find the element and print its text content
element = driver.find_element(By.CSS_SELECTOR, '.jobsearch-JobInfoHeader-title')
print(element.text)

# Close the web driver
driver.quit()