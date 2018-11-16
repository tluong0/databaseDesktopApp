import sqlite3


def connect():
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST files (id INTEGER PRIMARY KEY, client text, carrier text, status text, date text)")
    conn.commit()
    conn.close()

def insert()

connect()
