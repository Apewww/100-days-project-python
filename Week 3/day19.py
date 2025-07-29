# Introduction
import requests

API_KEY = '3960a3f492bddfe3a386e1511e54c3be'
city = "Cimahi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     # print("Success")
#     weather_data = response.json()
#     print(weather_data)
# else:
#     print("An error occurred.")
