import requests
import sqlite3
import time

#API key gathered from OpenWeather API
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
    
cur.execute("SELECT COUNT(*) FROM Weather")
count = cur.fetchone()[0]

# Only add 25 new records per run
if count < 100:
    to_add = 25
    for city in cities:
        for _ in range(5):  # loop through to collect up to 25 items
            if to_add == 0:
                break
            try:
                weather = fetch_weather(city)
                cur.execute('''
                    INSERT INTO Weather (city, date, temperature, humidity, wind_speed)
                    VALUES (?, ?, ?, ?, ?)
                ''', weather)
                to_add -= 1
                print(f"Inserted weather for {city}")
                time.sleep(1)  # Sleep to avoid hitting rate limits
            except Exception as e:
                print(f"Error for {city}: {e}")

# Save and close the database
conn.commit()
conn.close()
