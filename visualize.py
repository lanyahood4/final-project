# Who did it: LaNya & Fatou
import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# Connect to the SQLite database
db_path = os.path.abspath("final_project.db")
print(f"Using database: {db_path}")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# ----- WEATHER DATA VISUALIZATION -----
print("Fetching weather data...")

cur.execute("SELECT city, temperature FROM Weather")
weather_data = cur.fetchall()

weather_by_city = defaultdict(list)
for city, temp in weather_data:
    weather_by_city[city].append(temp)

avg_temp_by_city = {
    city: sum(temps) / len(temps)
    for city, temps in weather_by_city.items()
}

cities = list(avg_temp_by_city.keys())
temps = list(avg_temp_by_city.values())

plt.figure(figsize=(10, 5))
plt.bar(cities, temps)
plt.title("Average Temperature by City (°F)")
plt.xlabel("City")
plt.ylabel("Avg Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----- EARTHQUAKE DATA VISUALIZATION -----
print("Fetching earthquake data...")

cur.execute("SELECT place, magnitude FROM Earthquakes")
quake_data = cur.fetchall()

places = [place for place, _ in quake_data]
magnitudes = [mag for _, mag in quake_data]

plt.figure(figsize=(12, 6))
plt.hist(magnitudes, bins=10, edgecolor='black')
plt.title("Earthquake Magnitude Distribution (Past 7 Days)")
plt.xlabel("Magnitude")
plt.ylabel("Number of Earthquakes")
plt.tight_layout()
plt.show()

# Close the database connection
conn.close()
