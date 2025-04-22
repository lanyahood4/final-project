import requests
import sqlite3
import time

#API key gatherd from OpenWeather API
API_KEY = "8f9cb73e7fd99cc609bcbcffde42a36e"

# List of cities to gather data for
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Detroit', 'New Orleans', 'Atlanta']
DATE = "2025-04-08" 
# Connect to SQLite database
conn = sqlite3.connect('final_project.db')
cur = conn.cursor()

# Create AirQuality table
cur.execute('''
CREATE TABLE IF NOT EXISTS AirQuality (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    aqi INTEGER,
    main_pollutant TEXT,
    date TEXT
)
''')

# List of cities to collect AQI data for
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Detroit', 'New Orleans', 'Atlanta']

# Function to call the WeatherAPI and return relevant data
def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={DATE}"
    r = requests.get(url)
    data = r.json()
    day_data = data['forecast']['forecastday'][0]['day']
    return (
        city,
        DATE,
        day_data['avgtemp_f'],
        day_data['avghumidity'],
        day_data['maxwind_mph']
    )

