import requests
import smtplib
import os

mail = os.environ.get("SENDER_MAIL")
pass_word = os.environ.get("PASS_WORD")

API_KEY = os.environ.get("APIKEY")


locations = {
    "Lagos": {"lat": 6.595680, "lon": 3.337030},
    "Abeokuta": {"lat": 7.150130, "lon": 3.346030},
}

will_rain = {}

for location, params in locations.items():
    params.update({"appid": API_KEY, "exclude": "current,minutely,daily"})
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
    response.raise_for_status()
    data = response.json()["hourly"]

    will_rain[location] = any(item["weather"][0]["id"] < 600 for item in data[:12])

if any(will_rain.values()):
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=mail, password=pass_word)
        message = "Subject: Bankole's Rain Alert System\n\n"
        message += "It is going to rain sometime within the next 12 hours in the following locations:\n"
        message += ", ".join(location for location, rain in will_rain.items() if rain)
        message += ". \nYou should take an umbrella."
        connection.sendmail(from_addr=mail, to_addrs=[os.environ.get("MAIL_1"), os.environ.get("MAIL_2")], msg=message)



# print(data)
