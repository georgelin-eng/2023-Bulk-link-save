# Uses selenium to load a webpage and scrap the job title of it

# Issues: I don't understand how it works, very slow and needs to load a seperate instance of a browser to scrap it    


import os # is not neccessary for selenium but needs to be uesd in order to write to systemn files
from selenium import webdriver # This module is necessary to use selenium
from selenium.webdriver.common.by import By

# configure the browsing options that are sent in selenium
# the first is to specifically configure options
options = webdriver.ChromeOptions ()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
options.add_argument("--headless")

# Configure the web driver
driver = webdriver.Chrome(options=options)
url = 'https://ca.indeed.com/viewjob?jk=bb71e14877f45faa&tk=1fakhe7v5ouac801'
driver.implicitly_wait(0.1)
driver.get(url)

# Find the element and print its text content
element = driver.find_element(By.CSS_SELECTOR, '.jobsearch-JobInfoHeader-title')
print(element.text)

# Close the web driver
driver.quit()


