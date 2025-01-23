import requests
"""Fetch weather data from OpenWeather API"""
base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "New York",
    "appid": "f08a56b902bb961a666d3feeb47491ad",
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
# def fetch_weather(self, city):
#         """Fetch weather data from OpenWeather API"""
#         base_url = "http://api.openweathermap.org/data/2.5/weather"
#         params = {
#             "q": city,
#             "appid": self.api_key,
#             "units": "imperial"
#         }
#         try:
#             response = requests.get(base_url, params=params)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching weather data: {e}")
#             return None

