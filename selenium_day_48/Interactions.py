from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=options)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Click on a link
# num_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# num_articles.click()

# Find link by link text
# content_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# content_portals.click()

# Type in web page
# time.sleep(3)
# search = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')
# search.send_keys('abc')

# Challenge
fname = 'gg'
lname = 'wp'
email = 'ggwp@mail.com'

driver.get('http://secure-retreat-92358.herokuapp.com/')

input_fname = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
input_fname.send_keys(fname)

input_lname = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
input_lname.send_keys(lname)

input_email = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
input_email.send_keys(email)

sign_up = driver.find_element(By.XPATH, value='/html/body/form/button')
time.sleep(2)
sign_up.click()
