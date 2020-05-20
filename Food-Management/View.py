# Imports

import sqlite3                          # database SQLite

import tkinter as tk                    # tkinter
from tkinter import ttk                 # tkinter
from tkinter import messagebox as msg   # tkinter

''' Delete type function for availablity '''
def save_changes(n):
    
    try:
        db_conn.execute("UPDATE food SET avai = 0 WHERE ID={}".format(n))
        db_conn.commit()
        
        msg.showinfo("Saved", "Changes will be saved when the application is closed.")
     
    except sqlite3.OperationalError:
        print("Database couldn't be Updated")


''' Initialising database '''
db_conn = sqlite3.connect("DataBase.db")
theCursor = db_conn.cursor()


def view_function():        # view_function
    ''' Window settings '''
    win = tk.Tk()
    
    canvas = tk.Canvas(win)
    canvas.pack(padx=8, pady=8)
    scroll_y = tk.Scrollbar(win, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)
    '''
            win.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))         # size
            window.resizable(0,0)                                               # resizeablity
            window.title("Food")                                                # title
            window.iconbitmap('icon.ico')                                       # icon
    '''    
    ''' Some variables '''
    n = 1
    list_x = []
    list_y = []
    result = []
    
    
    ''' GUI'''
    ttk.Label(frame, text="Sl No").grid(row=0, column=0, padx=5, pady=2)        #grid: slno (lable)
    ttk.Label(frame, text="Name").grid(row=0, column=1, padx=5, pady=2)         #grid: name (lable)
    ttk.Label(frame, text="Quantity").grid(row=0, column=2, padx=5, pady=2)     #grid: quantity (lable)
    ttk.Label(frame, text="Address").grid(row=0, column=3, padx=5, pady=2)      #grid: address (lable)
    ttk.Label(frame, text="Date").grid(row=0, column=4, padx=5, pady=2)         #grid: date (lable)
    ttk.Label(frame, text="Reward").grid(row=0, column=5, padx=5, pady=2)       #grid: reward (lable)
    ttk.Label(frame, text="Cooked").grid(row=0, column=6, padx=5, pady=2)       #grid: cooked (lable)
    ttk.Label(frame, text="Availablity").grid(row=0, column=7, padx=5, pady=2)  #grid: availablity (lable)
    
    
    ''' GUI of List '''
    try:
        result = theCursor.execute("SELECT food_item, quan, addr, date, cash, cooked, avai FROM food")
    except sqlite3.OperationalError:
        msg.showerror("ERROR", "No items found!!")
    except:
        msg.showerror("ERROR" ,"Couldn't Retrieve Data From Database")
    
    
    for i in result:
        ttk.Label(frame, text=n).grid(row=n, column=0)
        ttk.Label(frame, text=i[0]).grid(row=n, column=1)
        ttk.Label(frame, text=i[1]).grid(row=n, column=2)
        ttk.Label(frame, text=i[2]).grid(row=n, column=3)
        ttk.Label(frame, text=i[3]).grid(row=n, column=4)
        ttk.Label(frame, text=i[4]).grid(row=n, column=5)
        ttk.Label(frame, text=i[5]).grid(row=n, column=6)
    
        list_x.append(i[6])

        n += 1
        
    for i in range(len(list_x)):
        if list_x[i] == 0:
            ttk.Label(frame, text="No").grid(column=7, row=i+1)
            list_y.append(ttk.Button(frame, text="Not Avaiable", command=lambda c=i: save_changes(c+1)))
        else:
            list_y.append(ttk.Button(frame, text="Not Avaiable", command=lambda c=i: save_changes(c+1)))
            list_y[i].grid(column=7, row=i+1)
    
    
    ''' Window settings '''
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')
    
    win.mainloop()