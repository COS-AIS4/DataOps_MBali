import requests
import json

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&daily=temperature_2m_max&timezone=Europe/Paris"

def fetch_weather_data():
    response = requests.get(API_URL)
    data = response.json()
    
    with open("data/weather.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("✅ Données météo enregistrées dans data/weather.json")

if __name__ == "__main__":
    fetch_weather_data()

