# Overview
This project is part of my learning journey to understand how to fetch and work with APIs. The main goal of this project is to determine if it will rain in two specific geographical locations, and if rain is expected, to send a mail notification providing information about the expected rain in each location. Additionally, the project is deployed on a PythonAnywhere server to run automatically every morning.

# Project Components
API Integration: This project utilizes the OpenWeather Map API to gather weather data for the specified locations.

Mail Notification: The Python smtplib module is employed to send email notifications. If rain is expected in either of the two locations, an email is sent to provide information about the expected rainfall.

Automation: The project is configured to run automatically once every morning. This ensures that you receive the latest rain alerts to start your day well-prepared.

