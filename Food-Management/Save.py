# Imports
import sqlite3      # DataBase SQLite3

from tkinter import messagebox as msg   # tkinter

from datetime import date               # DateTime


''' Initialising database '''
db_conn = sqlite3.connect("DataBase.db")
theCursor = db_conn.cursor()



''' Creating the table food '''
try:
    db_conn.execute("CREATE TABLE food(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, food_item TEXT NOT NULL, quan TEXT, addr TEXT, date TEXT, cash DOUBLE, cooked BOOL, avai INTEGER NOT NULL DEFAULT 1);")
    db_conn.commit()

except sqlite3.OperationalError:
    pass


def save_function(n, q, a, d, m, y, r, c):    
    try:
        food_name, quantity, address, day, reward, cooked = n.get(), q.get(), a.get(), date(int(y.get()), int(m.get()), int(d.get())), r.get(), c.get()
        
        db_conn.execute("INSERT INTO food (food_item, quan, addr, date, cash, cooked) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(food_name, quantity, address, day, reward, cooked))
        db_conn.commit()
        
    except:
        msg.showerror("Error", "Values Entered by you are Wrong!!\nPlease Enter Correct Values")