import requests
import sqlite3
import datetime

# Connect to SQLite database
conn = sqlite3.connect('final_project.db')
cur = conn.cursor()
