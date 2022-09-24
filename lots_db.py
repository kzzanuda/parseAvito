import sqlite3

conn = sqlite3.connect('lots.db')
cur = conn.cursor()


def init_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS lots(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       cdate DATE,
       age INT,
       cost INT,
       url TEXT,
       prod TEXT,
       model TEXT,
       run INT);
    """)
    conn.commit()
    print('Database init')
    return 0


def select_all():
    cur.execute("""SELECT * FROM lots""")
    rows = cur.fetchall()
    return rows


def select_wh(pr, wh):
    cur.execute("SELECT * FROM lots WHERE ? = ?", (pr, wh))
    rows = cur.fetchall()
    return rows


def insert_lot(lot):
    cur.execute("INSERT INTO lots (cdate, age, cost, url, prod, model, run) VALUES (?,?,?,?,?,?,?)", lot)
    conn.commit()
    return 0


if __name__ == '__main__':
    init_db()
