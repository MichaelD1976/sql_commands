"""
db_init.py

Purpose:
--------
This script initializes the football database.
It creates the `Matches` table (if it doesn't exist)
and inserts some sample match data.

Where it runs:
--------------
- In your project folder.
- The database file will be created at: db/football_simple.sqlite3

How to run:
-----------
1. Open terminal / command prompt in the project folder.
2. Run:
    python db_init.py
3. You should see:
    ✅ Matches table created
    ✅ Sample match data inserted
    ✅ Database initialization complete

Note:
-----
- Run this script **once** to create the database and sample data.
- Running it multiple times will create duplicate data.
"""

import sqlite3
from pathlib import Path

# ------------------------------
# 1. Define database path
# ------------------------------
DB_FOLDER = Path("db")
DB_FOLDER.mkdir(exist_ok=True)  # Create folder if it doesn't exist
DB_PATH = DB_FOLDER / "football_simple.sqlite3"

# ------------------------------
# 2. Connect to SQLite database
# ------------------------------
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ------------------------------
# 3. Create Matches table
# ------------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS Matches (
    MatchID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each match
    HomeTeam TEXT NOT NULL,                     -- Home team name
    AwayTeam TEXT NOT NULL,                     -- Away team name
    HomeScore INTEGER,                          -- Home team goals
    AwayScore INTEGER                           -- Away team goals
)
""")
print("✅ Matches table created")

# ------------------------------
# 4. Insert sample data
# ------------------------------
matches = [
    ('Red Lions', 'Blue Sharks', 3, 1),
    ('Green Eagles', 'Yellow Tigers', 2, 2),
    ('Red Lions', 'Yellow Tigers', 0, 1),
    ('Blue Sharks', 'Green Eagles', 1, 2)
]

cur.executemany(
    "INSERT INTO Matches (HomeTeam, AwayTeam, HomeScore, AwayScore) VALUES (?, ?, ?, ?)",
    matches
)
print("✅ Sample match data inserted")

# ------------------------------
# 5. Save changes and close
# ------------------------------
conn.commit()
conn.close()
print("✅ Database initialization complete")



