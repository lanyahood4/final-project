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
