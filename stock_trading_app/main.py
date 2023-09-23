import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv('.env')

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
    yesterday_closing = None
    day_before_yesterday_closing = None
    # Access the 1st and 2nd dict in the stock_data dict to get yesterday and day before yesterday stock data
    for key, value in stock_data.items():
        if yesterday_closing is None:
            yesterday_closing = float(stock_data[key]["4. close"])
        elif day_before_yesterday_closing is None:
            day_before_yesterday_closing = float(stock_data[key]["4. close"])
        else:
            break
    diff_percent = round(((day_before_yesterday_closing - yesterday_closing) / yesterday_closing) * 100, 2)
    return diff_percent


def get_news():
    news_apikey = os.getenv('NEWS_APIKEY')
    params = {'q': COMPANY_NAME, 'apikey': news_apikey}
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def format_message(data, price_differance, stock_name):
    up_down_indicator = '🔺' if price_differance < 0 else '🔻'
    message = f'{stock_name}: {up_down_indicator}{abs(price_differance)}%'
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
    send_message(format_message(news, stock_price_differance, STOCK))


