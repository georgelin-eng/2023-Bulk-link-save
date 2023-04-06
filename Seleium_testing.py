from selenium import webdriver
import time

# create an instance of webdriver.chrome
driver = webdriver.Chrome()
driver.get('https://www.google.com')

time.sleep (20)

browser.quit()