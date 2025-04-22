# Who is doing this one?: 
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('final_project.db')
cur = conn.cursor()

# Weather & AQI Join
cur.execute('''
SELECT 
    Weather.city,
    AVG(Weather.temperature),
    AVG(Weather.humidity),
    AVG(AirQuality.aqi)
FROM Weather
JOIN AirQuality
ON Weather.city = AirQuality.city AND Weather.date = AirQuality.date
GROUP BY Weather.city
''')
data = cur.fetchall()
cities = [row[0] for row in data]
avg_temps = [row[1] for row in data]
avg_humidities = [row[2] for row in data]
avg_aqis = [row[3] for row in data]

# Graph 1: AQI bar chart
plt.figure(figsize=(8, 5))
plt.bar(cities, avg_aqis, color='teal')
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("AQI")
plt.tight_layout()
plt.savefig("aqi_bar_chart.png")
plt.show()

