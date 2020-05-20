from Bill import Bill_Object
import pickle
from datetime import date
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import *



window = tk.Tk()
window.title("Bill Application")
window.resizable(0, 0)
window.iconbitmap('icon.ico')

#category problem
category_list = []

# Save Function
def save_function():

    try:
        issued = date(year.get(), month.get(), day.get())
        list_bills = []
        
        category_list.append(category.get().upper())
        
        try:
            with open("bills", "rb")as MyBills:
                list_bills = pickle.load(MyBills)
        except:
            pass
        
        list_bills.append(name.get())
        
        for i in list_bills:
            if isinstance(i, Bill_Object):
                pass
            else:
                i = Bill_Object(name.get(), category.get().upper(), issued, amount.get())
                list_bills.append(i)
                
        for i in list_bills:
            if isinstance(i, Bill_Object):
                pass
            else:
                list_bills.remove(i)
                
        with open("bills", "wb")as MyBills:
            pickle.dump(list_bills, MyBills)
            
        nameEntered.delete(0, 'end')
        dayEntered.delete(0, 'end')
        monthEntered.delete(0, 'end')
        yearEntered.delete(0, 'end')
        categoryEntered.delete(0, 'end')
        amountEntered.delete(0, 'end')
        msg.showinfo("Saved" ,"Your bill has been saved.")
        
        nameEntered.focus()
    
    except:
        nameEntered.delete(0, 'end')
        dayEntered.delete(0, 'end')
        monthEntered.delete(0, 'end')
        yearEntered.delete(0, 'end')
        categoryEntered.delete(0, 'end')
        amountEntered.delete(0, 'end')
        msg.showinfo("Error" ,"The values entered has Error.\n Please check!!!")
        
        
    

# view Function
def view_function():    
    try:
        # List It Self
        list_bills = []
        with open("bills", "rb")as MyBills:
            list_bills = pickle.load(MyBills)
        total = float()
        x = 1
        
        win = tk.Tk()
        win.title("List Of Bills")
        win.resizable(0,0)
        win.iconbitmap('icon.ico')

        sizex = 500
        sizey = 400
        posx  = 40
        posy  = 40
        win.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        
        canvas = tk.Canvas(win)
        scroll_y = tk.Scrollbar(win, orient="vertical", command=canvas.yview)

        frame = tk.Frame(canvas)
        
        name_button = []
        button_list = []
        
        for i in list_bills:
            ttk.Label(frame, text=x).grid(column=0, row=x)
            ttk.Label(frame, text=i.name).grid(column=1, row=x, sticky="w", padx=2)
            ttk.Label(frame, text=i.category).grid(column=2, row=x, sticky="w", padx=2)
            ttk.Label(frame, text=i.issued).grid(column=3, row=x, padx=2)
            ttk.Label(frame, text=i.amount).grid(column=4, row=x, padx=2)
            total += i.amount
            x += 1
            name_button.append(i.name)
        
        cost = "Total " + str(total) + " Rs"
        ttk.Label(frame, text=cost).grid(column=0, columnspan=5)
        
        for i in range(len(name_button)):
            button_list.append(ttk.Button(frame, text="Delet", command=lambda c=i: delete(c, win, canvas, scroll_y, frame)))
            button_list[i].grid(column=5, row=i+1)
        
        
        # Title
        ttk.Label(frame, text="SlNo: ").grid(column=0, row=0)
        ttk.Label(frame, text="Name: ", width=20).grid(column=1, row=0)
        ttk.Label(frame, text="Category: ", width=20).grid(column=2, row=0)
        ttk.Label(frame, text="Issued: ").grid(column=3, row=0)
        ttk.Label(frame, text="Amount: ").grid(column=4, row=0)
        
        
        with open("bills", "wb")as MyBills:
            pickle.dump(list_bills, MyBills)
        
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                 
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        win.mainloop()
        
    except:
        win = tk.Tk()
        win.title("List Of Bills")
        win.resizable(0, 0)
        win.iconbitmap('icon.ico')
        
        msg.showinfo("Bills", "No Bills Found")
        
        
        win.mainloop()


#delet function
def delete(x, win, canvas, scroll_y, frame):
    
    list_bills = []
    
    with open("bills", "rb")as MyBills:
        list_bills = pickle.load(MyBills)
        
    for i in range(len(list_bills)):
        if i == x:
            del list_bills[i]
            
    with open("bills", "wb")as MyBills:
        pickle.dump(list_bills, MyBills)
        
    y = len(list_bills) + 3
    
    ttk.Label(frame, text="Your bill will be deletes when the window closes").grid(column=0, columnspan=6)
    
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
        
    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                 
    canvas.pack(fill='both', expand=True, side='left')
    
    



# Name
ttk.Label(window, text="Name: ", width=21).grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(window, width=21, textvariable=name)
nameEntered.grid(column=1, row=0)


# Date
ttk.Label(window, text="Date (dd): ", width=21).grid(column=0, row=1)
day = tk.IntVar()
dayEntered = ttk.Entry(window, width=21, textvariable=day)
dayEntered.grid(column=1, row=1)

ttk.Label(window, text="Month (mm): ", width=21).grid(column=0, row=2)
month = tk.IntVar()
monthEntered = ttk.Entry(window, width=21, textvariable=month)
monthEntered.grid(column=1, row=2)

ttk.Label(window, text="Year (yyyy): ", width=21).grid(column=0, row=3)
year = tk.IntVar()
yearEntered = ttk.Entry(window, width=21, textvariable=year)
yearEntered.grid(column=1, row=3)


# Category
ttk.Label(window, text="Category: ", width=21).grid(column=0, row=4)
category = tk.StringVar()
categoryEntered = ttk.Entry(window, width=21, textvariable=category)
categoryEntered.grid(column=1, row=4)




# Amount
ttk.Label(window, text="Amount (number only): ", width=21).grid(column=0, row=5)
amount = tk.DoubleVar()
amountEntered = ttk.Entry(window, width=21, textvariable=amount)
amountEntered.grid(column=1, row=5)

# TouchUp
nameEntered.focus()


# Bottons
# save
save_action = ttk.Button(window, text="Save", command=save_function)
save_action.grid(column=0, columnspan=2)

#view
view_action = ttk.Button(window, text="View", command=view_function)
view_action.grid(column=0, columnspan=2)


window.mainloop()