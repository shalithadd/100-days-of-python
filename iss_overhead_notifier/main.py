import smtplib
from datetime import datetime
import requests
import time


MY_LAT = 341
MY_LONG = -123
MY_EMAIL = 'xx@gmail.com'
MY_PASSWORD = 'xxxix'
TO_EMAIL = 'xxx@gmail.com'


def is_iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    # Return true if it is dark now
    if time_now <= sunrise or time_now >= sunset:
        return True


def send_email():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg='Subject: LOOK UP NOW!\n\n'
                                'International Space Station above you in the sky!'
                            )


while True:
    time.sleep(60)
    if is_iss_visible() and is_dark():
        send_email()
    else:
        print("It's not even close! ☹️")
