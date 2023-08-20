import datetime as dt
import random
import pandas
import smtplib

MY_NAME = 'xxx'
MY_EMAIL = 'xxxx@gmail.com'
MY_PASSWORD = 'xxx'

today = dt.datetime.now()
today_tuple = (today.day, today.month)

data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.day, data_row.month): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'

    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_text = contents.replace("[NAME]", birthday_person["name"])
        new_text = new_text.replace('Angela', MY_NAME)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject: Happy Birthday!\n\n{new_text}'
                            )
