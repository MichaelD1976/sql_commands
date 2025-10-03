"""
utils.py

Purpose:
--------
Helper functions for the football database project.

Currently includes:
- export_matches_to_csv(): export Matches table to CSV.

How to use:
-----------
See the optional driver script `export_csv.py` for running this function.

"""

import sqlite3
import csv
from pathlib import Path

import sqlite3
import csv
from pathlib import Path

DB_PATH = Path("db/football_simple.sqlite3")

def export_matches_to_csv(csv_file="matches.csv"):
    """
    Export all rows from the Matches table to a CSV file.

    Parameters:
    -----------
    csv_file : str
        Name of the CSV file to create (default: matches.csv)
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Matches")
    rows = cur.fetchall()

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        # Write headers
        writer.writerow([d[0] for d in cur.description])
        # Write all rows
        writer.writerows(rows)

    conn.close()
    print(f"✅ Exported matches to {csv_file}")

