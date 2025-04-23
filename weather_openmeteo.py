# Who did it: LaNya
import requests
import sqlite3
import time
import os
from datetime import datetime, timedelta

# Use yesterday’s date (Open-Meteo supports today & past)
DATE = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

# Print the full path to the database for clarity
db_path = os.path.abspath("final_project.db")
print(f"Using database: {db_path}")
print(f"Using date: {DATE}")

# City name with corresponding (latitude, longitude)
cities = {
    'New York': (40.7128, -74.0060),
    'Los Angeles': (34.0522, -118.2437),
    'Chicago': (41.8781, -87.6298),
    'Houston': (29.7604, -95.3698),
    'Phoenix': (33.4484, -112.0740),
    'Detroit': (42.3314, -83.0458),
    'New Orleans': (29.9511, -90.0715),
    'Atlanta': (33.7490, -84.3880)
}
# Connect to SQLite database
conn = sqlite3.connect("final_project.db")
cur = conn.cursor()

# Step 1: Create the Weather table
print("Creating Weather table (if not exists)...")
cur.execute('''
CREATE TABLE IF NOT EXISTS Weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    date TEXT,
    temperature REAL,
    humidity INTEGER,
    wind_speed REAL
)
''')
conn.commit()

# Step 2: Confirm table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables in database now:", tables)

# Step 3: Try a COUNT query to check existing rows
try:
    cur.execute("SELECT COUNT(*) FROM Weather")
    count = cur.fetchone()[0]
    print(f"Existing rows: {count}")
except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
    conn.close()
    exit(1)
# Step 4: Define function to fetch weather from Open-Meteo
def fetch_weather(city, lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&start_date={DATE}&end_date={DATE}"
        f"&daily=temperature_2m_max,temperature_2m_min,relative_humidity_2m_mean,wind_speed_10m_max"
        f"&timezone=America/New_York"
    )
    r = requests.get(url)
    data = r.json()

    if "daily" not in data or not data["daily"]["temperature_2m_max"]:
        print(f"[DEBUG] Full response for {city}:\n{data}")
        raise ValueError(f"{city} Open-Meteo parsing error: Missing data.")

    # Calculate average temperature and convert units
    temp_avg = (data["daily"]["temperature_2m_max"][0] + data["daily"]["temperature_2m_min"][0]) / 2
    humidity = data["daily"]["relative_humidity_2m_mean"][0]
    wind = data["daily"]["wind_speed_10m_max"][0]

    # Convert temp from Celsius to Fahrenheit, wind from km/h to mph
    return (
        city,
        DATE,
        round(temp_avg * 9 / 5 + 32, 1),
        humidity,
        round(wind / 1.609, 1)
    )
    
