from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.get('https://www.amazon.co.uk/Samsung-Odyssey-LC32G75TQSPXXU-Curved-Monitor/dp/B0BS1NT84N/ref=sr_1_4?'
           'crid=3QFZGCCDJ2FNI&keywords=odyssey+g7&qid=1696450810&sprefix=oddysy%2Caps%2C76&sr=8-4&ufe='
           'app_do%3Aamzn1.fos.16386313-b7bf-4b29-bfa1-0d3d5f3a0dd5')

# Access element by class name
price_pounds = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_pence = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
print(f'Price is {price_pounds.text}.{price_pence.text}')

# Access element by ID
x = driver.find_element(By.ID, value='newAccordionRow_0')
# print(x)

# Access element by name
search_bar = driver.find_element(By.NAME, value='field-keywords')
print(search_bar.get_attribute('value'))

# Access element by CSS selector
image = driver.find_element(By.CSS_SELECTOR, value='div#imgTagWrapperId img')
print(image.get_attribute('src'))

# Access elements by X-Path
discount = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div['
                                               '1]/span[1]')
print(discount.text)


driver.quit()
