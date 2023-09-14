import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv('../.env')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'


def get_stock_data():
    stock_apikey = os.getenv('STOCK_APIKEY')
    params = {'function': 'TIME_SERIES_DAILY',
              'symbol': STOCK,
              'apikey': stock_apikey
              }
    response = requests.get(STOCK_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def calc_stock_price_differance(data):
    stock_data = data['Time Series (Daily)']
    count = 0
    # Access the 2nd and 3rd dict in the stock_data dict to get yesterday and day before yesterday stock data
    for key, value in stock_data.items():
        # for each key, value pair in stock_data check if the value is a dict and increment the counter
        if isinstance(value, dict):
            count += 1
            if count == 1:
                yesterday_closing = float(stock_data[key]["4. close"])
            elif count == 2:
                day_before_yesterday_closing = float(stock_data[key]["4. close"])
            elif count > 3:
                break
    diff_percent = round(((day_before_yesterday_closing - yesterday_closing) / yesterday_closing) * 100, 2)
    return diff_percent


def get_news():
    news_apikey = os.getenv('NEWS_APIKEY')
    params = {'q': COMPANY_NAME, 'apikey': news_apikey}
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def format_message(data, price_differance):
    if price_differance < 0:
        up_down_indicator = '🔺'
    else:
        up_down_indicator = '🔻'
    message = f'{STOCK}: {up_down_indicator}{abs(price_differance)}%'
    for i in range(3):
        message += f"\nHeadline: {data[i]['title']}\nRead article: {data[i]['url']}\n"
    return message


def send_message(data):
    twilio_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    from_num = os.getenv('FROM_NUMBER')
    to_num = os.getenv('TO_NUMBER')
    client = Client(twilio_sid, auth_token)
    message = client.messages.create(
        body=data,
        from_=from_num,
        to=to_num,
    )
    print(message.status)


stock_price_differance = calc_stock_price_differance(get_stock_data())
if abs(stock_price_differance) > 5:
    news = get_news()['articles'][:3]
    send_message(format_message(news, stock_price_differance))


