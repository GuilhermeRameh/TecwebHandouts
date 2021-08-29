import sqlite3

class Database:

    def __init__(self, name):
        self.conn = sqlite3.connect(name+".db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")