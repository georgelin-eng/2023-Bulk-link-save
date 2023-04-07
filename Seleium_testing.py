from selenium import webdriver
import time

# create an instance of webdriver.chrome
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.google.com')

time.sleep (600)

driver.quit()