# SI 206 Final Project - SI 206 API's

## Topic
Analyzing how weather, air quality, and earthquake events are related across U.S. cities.

## APIs Used
- open-meteo (avg temperature, humidity, wind)
- IQAir API (air quality index)
- USGS Earthquake API (location, magnitude of quakes)

## Files
- weather_openmeteo.py stores weather data (limit 25/run)
- air_quality_data.py – stores AQI data (limit 25/run)
- earthquake_data.py – fetches recent earthquakes
- analyze_data.py – SQL JOINs, analysis, outputs calculated_data.txt
- visualize.py – creates 3 visualizations (AQI, temp vs AQI, quake bar chart)

## How to Use
1. Add your API keys to `weather_data.py` and `air_quality_data.py`
2. Run:
   - `python weather_openmeteo.py` multiple times
   - `python air_quality_data.py` multiple times
   - `python earthquake_data.py` once
   - `python analyze_data.py` to process and output results
   - `python visualize.py` to create 3 graphs
