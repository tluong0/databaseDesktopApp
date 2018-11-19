import sqlite3


def connect():
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS file (id INTEGER PRIMARY KEY, client text, carrier text, status text, date text)")
    conn.commit()
    conn.close()


def insert(client, carrier, status, date):
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO file VALUES (NULL, ?,?,?,?)", (client, carrier, status, date))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM file")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(client="", carrier="", status=""):
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM file WHERE client=? OR carrier=? OR status=?",(client, carrier, status))
    rows=cur.fetchall()
    conn.close()
    return rows
connect()


def delete(id):
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM file WHERE id=?",(id,))
    conn.commit()
    conn.close()


def update(id, client, carrier, status, date):
    conn=sqlite3.connect("files.db")
    cur=conn.cursor()
    cur.execute("UPDATE file SET client=?, carrier=?, status=?, date=? WHERE id=?",(client, carrier, status, date,id))
    conn.commit()
    conn.close()



