import sqlite3

con = sqlite3.connect("./phones.db")
cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS phones
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
value VARCHAR(20));
"""
cur.execute(sql)
con.close()

