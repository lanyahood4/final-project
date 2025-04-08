# SI 206 Final Project - SI 206 API's

## Description
This project analyzes the relationship between weather conditions and air quality in major U.S. cities using data from:
- WeatherAPI
- IQAir API

## Files
- weather_data.py — gets weather data and stores it in SQLite
- air_quality_data.py — gets AQI data and stores it in SQLite
- analyze_data.py — joins data, calculates averages, writes to file
- visualize.py — creates 3 graphs: bar, scatter, and line chart
- calculated_data.txt — contains the output results of analysis
  
## Run Order
1. `python weather_data.py` (run multiple times to gather 100+ records)
2. `python air_quality_data.py` (run multiple times)
3. `python analyze_data.py` (writes `calculated_data.txt`)
4. `python visualize.py` (shows and saves graphs)
