
import sqlite3

conn = sqlite3.connect("dft_data.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    schema = f.read()

cursor.executescript(schema)

conn.commit()
conn.close()

print("Database and table created successfully!")
