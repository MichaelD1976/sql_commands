## SQL Commands Project: Football Match Database

### Overview

This project is a beginner-friendly Python + SQLite setup for learning SQL in a hands-on way.  

It creates a simple **football matches database**, populates it with **sample data**, allows you to **query it in Python**, and optionally **export the data to a CSV** for easy viewing.

You can use this project as:

- A **tutorial** for SQL and Python database interaction  
- A **reference** for common SQL operations  

---

### Project Structure

sql_commands/
│
├── db/ # Contains the database file after running db_init.py
│ └── football_simple.sqlite3
├── db_init.py # Creates tables & inserts sample data
├── main.py # Queries and interacts with the database
├── utils.py # Helper functions (e.g., CSV export)
└── export_csv.py # Driver script to export the database to CSV

pgsql
Copy code

---

### File Descriptions

#### 1. `db_init.py`

**Purpose:**  

- Initialize the database
- Create the `Matches` table (if it doesn’t exist)
- Insert sample football match data

**How it works:**  

- Connects to SQLite database (`db/football_simple.sqlite3`)
- Uses SQL `CREATE TABLE` to create a table
- Uses Python `executemany()` to safely insert multiple rows

**How to run:**  

```powershell
python db_init.py
Expected output:

sql
Copy code
✅ Matches table created
✅ Sample match data inserted
✅ Database initialization complete
Note:
Run this script once to create the database. Running it again will add duplicate data.

2. main.py
Purpose:

Interact with the database and query data

Show all matches

Demonstrate filtering queries

How it works:

Connects to SQLite database

Uses SQL SELECT queries to fetch data

Filters matches using WHERE conditions

Prints results to console

Example queries included:

Show all matches

Show matches where HomeTeam scored more than 1 goal

How to run:

powershell
Copy code
python main.py
Expected output:

lua
Copy code
--- All Matches ---
(1, 'Red Lions', 'Blue Sharks', 3, 1)
(2, 'Green Eagles', 'Yellow Tigers', 2, 2)
(3, 'Red Lions', 'Yellow Tigers', 0, 1)
(4, 'Blue Sharks', 'Green Eagles', 1, 2)

--- Home Team scored more than 1 goals ---
(1, 'Red Lions', 'Blue Sharks', 3, 1)
(2, 'Green Eagles', 'Yellow Tigers', 2, 2)
3. utils.py
Purpose:

Store helper functions for the project

Current function: export_matches_to_csv()

export_matches_to_csv()

Exports all rows from the Matches table to a CSV file

Writes headers automatically

Creates matches.csv in your project folder

Why helpers live here:

Keeps the project organized

Functions in utils.py can be reused in multiple scripts

Avoids repeating code

4. export_csv.py
Purpose:

Small driver script to call the CSV export function in utils.py

Ensures Python can find utils.py and run the function without import errors

How to run:

powershell
Copy code
python export_csv.py
Expected output:

css
Copy code
✅ Exported matches to matches.csv
Open matches.csv in Excel or VS Code to view data like a spreadsheet

Running the Project in Order
Initialize database & insert sample data

powershell
Copy code
python db_init.py
Query and view matches

powershell
Copy code
python main.py
Export matches to CSV (optional)

powershell
Copy code
python export_csv.py
Tips for Beginners
Always run db_init.py before main.py or export_csv.py

If you want to reset the database, delete db/football_simple.sqlite3 and rerun db_init.py

All scripts can be run from PowerShell in the project folder

The .venv virtual environment ensures Python packages don’t conflict, but this project only uses the standard library

Learning Outcomes
By working with this project, you will learn:

How to use Python to create and manage an SQLite database

How to insert, query, and filter data using SQL

How to organize a project with separate scripts for setup, interaction, and utilities

How to export database tables to CSV for easy visualization

Optional Next Steps
Add more queries to main.py (e.g., top scoring team, average goals)

Add more helper functions in utils.py

Explore SQLite GUI tools to view football_simple.sqlite3 visually

Experiment with adding new tables, like Players or Teams
