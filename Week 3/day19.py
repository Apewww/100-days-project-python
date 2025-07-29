# Introduction
import requests

# API_KEY = '3960a3f492bddfe3a386e1511e54c3be'
# city = "Cimahi"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     # print("Success")
#     weather_data = response.json()
#     print(weather_data)
# else:
#     print("An error occurred.")


# Weather App using OpenWeatherMap API

# Step 1: API SETUP
API_KEY = '3960a3f492bddfe3a386e1511e54c3be'
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"

# Step 2: Get Weather Data
def get_weather_data(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data['name'],
                "Temperature": f"{data['main']['temp']}C",
                "Weather": data['weather'][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']}m/s",
            }
            return weather
        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print("An eror occurred:", e)

# Step 3: Display Weather Information
def display_weather(weather):
    print("\n----- Weather Information -----")
    for key, value in weather.items():
        print(f"{key}: {value}")
        
# Step 4: Main Program
while True:
    print("\n----- Weather App -----")
    city = input("Enter a city name (or 'q' to quit): ")
    if city.lower() == 'q':
        break
    weather = get_weather_data(city)
    if weather:
        display_weather(weather)