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
# Get earthquake counts by general region (e.g., California, Alaska)
cur.execute('''
SELECT place FROM Earthquakes
''')
quake_rows = cur.fetchall()
quake_counts = {}
for place_tuple in quake_rows:
    place = place_tuple[0]
    region = place.split(",")[-1].strip() if "," in place else place.split(" ")[-1]
    if region not in quake_counts:
        quake_counts[region] = 0
    quake_counts[region] += 1
    

