import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

driver_path = '../../msedgedriver.exe'
service = Service(driver_path)
options = Options()
options.add_experimental_option('detach', True)

browser = webdriver.Edge(service=service, options=options)
browser.get('http://orteil.dashnet.org/experiments/cookie/')

# Get cookies to click
cookie = browser.find_element(By.XPATH, '//*[@id="cookie"]')

# Get upgrade items
items = browser.find_elements(By.CSS_SELECTOR, value='#store div')
item_ids = [item.get_attribute('id') for item in items]

five_min = time.time() + 60 * 5
timeout = time.time() + 5

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = browser.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = []

        # Convert <b> text into int
        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = browser.find_element(By.ID, value='money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)

        # Find affordable upgrades
        affordable_upgrades = {}
        for cost, item_id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = item_id

        # Purchase most expensive upgrade
        most_expensive_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[most_expensive_upgrade]

        browser.find_element(By.ID, value=to_purchase_id).click()

        # Add 5 seconds to reset timeout
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check cookies per second count
    if time.time() > five_min:
        cookies_per_s = browser.find_element(By.ID, value='cps')
        print(cookies_per_s)
        break
# browser.quit()
