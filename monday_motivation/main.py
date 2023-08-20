import datetime as dt
import random
import smtplib


my_email = '345@gmail.com'
recipient_email = '123@gmail.com'
my_password = 123

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open('quotes.txt', 'r') as data:
        list_of_quotes = data.readlines()
        quote = random.choice(list_of_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f'Subject: Quote of the day!\n\n{quote}'
        )
