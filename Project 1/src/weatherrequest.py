import requests
"""Fetch weather data from OpenWeather API"""
base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "New York",
    "appid": "apiKey",
    "units": "imperial"
}
try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    print(data['main']['temp'])
    print("Data: ",data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    None