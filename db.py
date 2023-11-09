import sqlite3 as sl
import os

def remove():
    os.remove("database.db")

def init():
    os.remove("database.db")

    con = sl.connect("database.db")
    c = con.cursor()

    try:
        c.execute("""CREATE TABLE IF NOT EXISTS client (
                ID INTEGER PRIMARY KEY,
                Surname VARCHAR,
                Name VARCHAR,
                Email VARCHAR)""")
        print("client table initiated.")

        c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY,
                Price INTEGER,
                MagazineState INTEGER
                )""")
        print("product table initiated.")

        c.execute("""CREATE TABLE IF NOT EXISTS "order" (
                ID INTEGER PRIMARY KEY,
                client_id INTEGER,
                product_list TEXT,
                order_status TEXT CHECK(order_status IN ('pending', 'finished')),
                FOREIGN KEY(client_id) REFERENCES client(ID)
                )""")
        print("order table initiated.")

        print("all orders initiated")
    except:
        print("Error in initiating tables")
    
    con.commit()
    con.close()

def select(table, id=-1, all=False):
    con = sl.connect("database.db")
    c = con.cursor()

    if all:
        res = c.execute("SELECT * FROM " + table).fetchall()
    else:
        res = c.execute("SELECT * FROM " + table + " WHERE ID = " + str(id)).fetchall()
    
    con.commit()
    con.close()
    return res

def insert(table, values):
    con = sl.connect("database.db")
    c = con.cursor()

    atbs = str(list(values.keys()))[1:-1].replace("\'", "")
    vals = str(list(values.values()))[1:-1]

    c.execute("INSERT INTO " + table + " (" + atbs + ") VALUES (" + vals + ")")

    con.commit()
    con.close()

    