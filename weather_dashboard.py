import requests
import json
import matplotlib.pyplot as plt

API_KEY = "d50489830d7f5d367e63631fd1750734"
CITY = "Hyderabad"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()

# Save API data to JSON file
with open("weather_data.json", "w") as file:
    json.dump(data, file, indent=4)

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    labels = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"]
    values = [temperature, humidity, wind_speed]

    plt.bar(labels, values)
    plt.title(f"Weather Dashboard for {CITY}")
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    plt.show()
else:
    print("Error fetching data:", data)