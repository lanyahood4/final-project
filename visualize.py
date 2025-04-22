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

# Graph 2: Temp vs AQI scatter
plt.figure(figsize=(8, 5))
plt.scatter(avg_temps, avg_aqis, color='orange')
for i in range(len(cities)):
    plt.annotate(cities[i], (avg_temps[i], avg_aqis[i]))
plt.title("Temperature vs AQI")
plt.xlabel("Avg Temperature (F)")
plt.ylabel("Avg AQI")
plt.tight_layout()
plt.savefig("temp_vs_aqi.png")
plt.show()


# Graph 3: Earthquake frequency by region
cur.execute("SELECT place FROM Earthquakes")
quake_data = cur.fetchall()
region_counts = {}

for place in quake_data:
    region = place[0].split(",")[-1].strip() if "," in place[0] else place[0].split(" ")[-1]
    if region not in region_counts:
        region_counts[region] = 0
    region_counts[region] += 1


# Sort and pick top 5 quake-heavy regions
top_regions = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)[:5]
labels = [r[0] for r in top_regions]
values = [r[1] for r in top_regions]

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color='crimson')
plt.title("Top 5 Regions with Most Earthquakes")
plt.xlabel("Region")
plt.ylabel("Number of Earthquakes")
plt.tight_layout()
plt.savefig("earthquake_bar.png")
plt.show()

conn.close()


