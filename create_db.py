import sqLite3

conn = sqLite3.connect("expenses.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expences
(id INTEGER PRIMARY KEY,
Date DATE,
description TEXT,
categort TEXT,
price REAL)""")

conn.commit