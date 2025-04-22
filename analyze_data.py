#Who is doing this one?: 
import sqlite3
conn = sqlite3.connect('final_project.db')
cur = conn.cursor()

# Weather & AQI JOIN
query = '''
SELECT 
    Weather.city,
    Weather.temperature,
    Weather.humidity,
    AirQuality.aqi
FROM Weather
JOIN AirQuality
ON Weather.city = AirQuality.city AND Weather.date = AirQuality.date
'''
cur.execute(query)
rows = cur.fetchall()
