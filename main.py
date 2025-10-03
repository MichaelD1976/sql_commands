"""
main.py

Purpose:
--------
This script allows you to interact with the football database.
It demonstrates:
- How to view all matches
- How to filter matches based on conditions

Where it runs:
--------------
- In your project folder.
- It reads from the database: db/football_simple.sqlite3

How to run:
-----------
1. Make sure db_init.py has been run at least once to create the database.
2. In terminal / command prompt, run:
    python main.py
3. You should see all matches printed and example filter output.

Notes:
------
- You can add more queries in the script following the examples.
- This script is separate from db_init.py to separate data creation from querying.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("db/football_simple.sqlite3")

# ------------------------------
# Function: show all matches
# ------------------------------
def show_all_matches():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Matches")  # Get all rows
    rows = cur.fetchall()
    print("\n--- All Matches ---")
    for row in rows:
        print(row)
    conn.close()

# ------------------------------
# Function: filter matches (example)
# ------------------------------
def home_team_scored_more_than(goals):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # ? is a placeholder for parameter
    cur.execute("SELECT * FROM Matches WHERE HomeScore > ?", (goals,))
    rows = cur.fetchall()
    print(f"\n--- Home Team scored more than {goals} goals ---")
    for row in rows:
        print(row)
    conn.close()

# ------------------------------
# Main program
# ------------------------------
if __name__ == "__main__":
    show_all_matches()
    home_team_scored_more_than(1)



