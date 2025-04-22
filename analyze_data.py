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
# Calculate weather/AQI averages
results = []

for city, data in city_data.items():
    avg_temp = sum(data['temps']) / len(data['temps'])
    avg_humidity = sum(data['humidities']) / len(data['humidities'])
    avg_aqi = sum(data['aqis']) / len(data['aqis'])
    results.append((city, avg_temp, avg_humidity, avg_aqi))

