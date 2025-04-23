# Who did it: LaNya & Fatou
import sqlite3
import matplotlib.pyplot as plt
from collections import defaultdict
import os

# Connect to the SQLite database
db_path = os.path.abspath("final_project.db")
print(f"Using database: {db_path}")
conn = sqlite3.connect(db_path)
cur = conn.cursor()
