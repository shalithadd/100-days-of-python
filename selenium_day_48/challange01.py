from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import json

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=options)
driver.get('https://www.python.org/')

time_lst = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
events_lst = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

event_dict = {idx: {'time': time_lst[idx].text, 'name': events_lst[idx].text} for idx in range(len(time_lst))}
print(json.dumps(event_dict, indent=4))

driver.quit()

