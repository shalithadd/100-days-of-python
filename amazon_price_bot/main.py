import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env')
EMAIL = os.getenv('EMAIL')
PW = os.getenv('PW')

URL = ('https://www.amazon.co.uk/Samsung-Odyssey-Curved-Gaming-Monitor/dp/B0866C9XJM/ref=sr_1_65?'
       'crid=3FQ1N8CG5R6GY&keywords=1440p%2B240hz%2Bmonitor%2Bultra%2Bwide&qid=1696366536&s=computers&'
       'sprefix=1440p%2B240hz%2Bmonitor%2Bultra%2Bwide%2Ccomputers%2C84&sr=1-65&th=1')
MY_PRICE = 480

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
}

response = requests.get(url=URL, headers=headers, )
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

product_name = soup.select_one('h1 #productTitle').get_text().strip()
price = int(soup.select_one('div .a-price-whole').get_text().split('.')[0])

if price < MY_PRICE:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PW)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject: Price Drop Alert!!!\n\nBuy {product_name} just for £{price}!'.encode('utf-8')
        )

