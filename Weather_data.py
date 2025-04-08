import requests
import sqlite3
import time

#API key gatherd from OpenWeather API
API_KEY = "8f9cb73e7fd99cc609bcbcffde42a36e"

# List of cities to gather data for
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Detroit', 'New Orleans', 'Atlanta']
DATE = "2025-04-08"  
