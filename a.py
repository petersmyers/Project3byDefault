import sqlite3

conn = sqlite3.connect('loans.db')
c = conn.cursor()

def view_table():
    c.execute('SELECT * FROM loan_stats ')
    conn.commit()
    c.close()
    conn.close()

view_table