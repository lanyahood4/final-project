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
