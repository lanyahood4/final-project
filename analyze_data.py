# Who did it: LaNya & Fatou
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("final_project.db")

# Read tables
weather_df = pd.read_sql_query("SELECT * FROM Weather", conn)
earthquake_df = pd.read_sql_query("SELECT * FROM Earthquakes", conn)
# Ensure correct types
weather_df['temperature'] = pd.to_numeric(weather_df['temperature'], errors='coerce')
weather_df['humidity'] = pd.to_numeric(weather_df['humidity'], errors='coerce')
weather_df['wind_speed'] = pd.to_numeric(weather_df['wind_speed'], errors='coerce')

# Save cleaned data to CSVs for easy use in visualization
weather_df.to_csv("cleaned_weather.csv", index=False)
earthquake_df.to_csv("cleaned_earthquakes.csv", index=False)

