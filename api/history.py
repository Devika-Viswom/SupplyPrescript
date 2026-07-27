import sqlite3

conn = sqlite3.connect("history.db", check_same_thread=False)

cursor = conn.cursor()

'''
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
id INTEGER PRIMARY KEY,
timestamp TEXT,
origin_port TEXT,
destination_port TEXT,
transport_mode TEXT,
risk_probability REAL,
predicted_lead_time REAL,
risk_level TEXT
)
""")

conn.commit()
'''

cursor.execute(
"""
INSERT INTO predictions(
timestamp,
origin_port,
destination_port,
transport_mode,
risk_probability,
predicted_lead_time,
risk_level
)
VALUES(?,?,?,?,?,?,?)
""",
(
datetime.now().strftime(
"%Y-%m-%d %H:%M:%S"
),
data.origin_port,
data.destination_port,
data.transport_mode,
risk_probability,
lead_time,
risk_level
)
)

conn.commit()