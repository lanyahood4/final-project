# Who did it: LaNya & Fatou
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("final_project.db")

# Read tables
weather_df = pd.read_sql_query("SELECT * FROM Weather", conn)
earthquake_df = pd.read_sql_query("SELECT * FROM Earthquakes", conn)
