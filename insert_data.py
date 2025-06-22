
import sqlite3
from datetime import datetime, timedelta
import random

conn = sqlite3.connect("dft_data.db")
cursor = conn.cursor()


scan_chains = ['SCAN_A', 'SCAN_B', 'SCAN_C']
pattern_prefix = 'PATTERN_'


base_time = datetime(2025, 6, 1, 9, 0)      # Generating and inserting 30 rows of synthetic data

for i in range(30):
    pattern_id = f"{pattern_prefix}{i+1:03}"
    scan_chain = random.choice(scan_chains)
    pass_rate = round(random.uniform(70.0, 100.0), 2)  
    test_time_ms = random.randint(100, 500) 
    timestamp = (base_time + timedelta(minutes=i * 5)).strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO dft_results (pattern_id, scan_chain, pass_rate, test_time_ms, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (pattern_id, scan_chain, pass_rate, test_time_ms, timestamp))

conn.commit()
conn.close()

print("Sample DFT test data inserted successfully!")
