# Who did it: Fatou N. Diallo
import requests
import sqlite3
import os
from datetime import datetime, timedelta

# Print database path
db_path = os.path.abspath("final_project.db")
print(f"Using database: {db_path}")

# Connect to SQLite database
conn = sqlite3.connect("final_project.db")
cur = conn.cursor()

# Step 1: Create the Earthquakes table
cur.execute('''
CREATE TABLE IF NOT EXISTS Earthquakes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    magnitude REAL,
    place TEXT,
    time TEXT
)
''')
conn.commit()

# Step 2: Define API URL for the past 7 days of significant earthquakes
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=7)
url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
    f"&starttime={start_time.strftime('%Y-%m-%d')}"
    f"&endtime={end_time.strftime('%Y-%m-%d')}"
    "&minmagnitude=4.5"
)

# Step 3: Fetch earthquake data
response = requests.get(url)
data = response.json()

# Step 4: Insert up to 100 records into the Earthquakes table
quake_count = 0
for feature in data['features'][:100]:  # Limit to the first 100 entries
    properties = feature['properties']
    magnitude = properties.get('mag')
    place = properties.get('place')
    time_ms = properties.get('time')
    time_str = datetime.utcfromtimestamp(time_ms / 1000).strftime('%Y-%m-%d %H:%M:%S')

    cur.execute('''
    INSERT INTO Earthquakes (magnitude, place, time)
    VALUES (?, ?, ?)
    ''', (magnitude, place, time_str))
    
    quake_count += 1

conn.commit()
conn.close()

print(f"Inserted {quake_count} earthquake records.")
