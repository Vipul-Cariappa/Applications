''' Imports '''

import tkinter as tk                    # tkinter
from tkinter import ttk                 # tkinter
from tkinter import messagebox as msg   # tkinter

from Save import save_function          # My Function
from View import view_function


''' Main Window - Settings '''
window = tk.Tk()

'''
win.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))         # size
window.resizable(0,0)                                               # resizeablity
window.title("Food")
'''                                                # title
window.iconbitmap('icon.ico')                                       # icon   
window.resizable(0,0)                                               # resizeablity
window.title("Food")


app = tk.Frame(window)
app.pack(padx=8, pady=8)

''' Gui of Frame '''

#--------------- name ---------------
ttk.Label(app, text="Enter the food item: ").grid(row=0, column=0, sticky="w", pady=2)  # grid: food name (label)
food_item = tk.StringVar()                                                              # To Be Saved (food name)
it = ttk.Entry(app, width=30, textvariable=food_item)                                   # food name entry
it.grid(row=0, column=1, sticky="w", pady=2)                                            # grid: food name(entry)

#--------------- cooked or un cooked ---------------
cook = tk.BooleanVar()                                                                  # To Be Saved (cooked or uncooked)
cooked = ttk.Checkbutton(app, text="Cooked: ", variable=cook)                           # cooked entry
cooked.grid(row=5, columnspan=2, pady=2)                                                # grid: cooked

#--------------- Quantity ---------------
ttk.Label(app, text="Enter the Quantity: ").grid(row=1, column=0, sticky="w", pady=2)                   # grid: quantity (label)
quantity = tk.StringVar()                                                                               # To Be Saved (quantity)
quan = ttk.Combobox(app, width=12, textvariable=quantity)                                               # quantity entry
quan['values'] = ("100g", "200g", "300g", "400g", "500g", "1kg", "2kg", "3kg", "4kg", "5kg", "10kg")    # giving somw values
quan.grid(row=1, column=1, pady=2)                                                                      # grid: quantity (entry)

#--------------- cash money ---------------
ttk.Label(app, text="Enter the cash money: ").grid(row=4, column=0, pady=2)             # grid: money(label)
reward = tk.StringVar()                                                                 # To Be Saved (cash reward) 
re = ttk.Entry(app, width=30, textvariable=reward)                                      # cash reward
re.grid(row=4, column=1, pady=2)                                                        # grid: money (entry)


#--------------- address ---------------
ttk.Label(app, text="Adress and Contact: ").grid(row=2, column=0, pady=2)               # grid: address (label) 
address = tk.StringVar()                                                                # To Be Saved
addr = ttk.Entry(app, width=30, textvariable=address)                                   # address
addr.grid(row=2, column=1, pady=2)                                                      # grid: address(entry)

#--------------- date --------------- NOTE: In new frame
ttk.Label(app, text="Enter the Date: ").grid(row=3, column=0, pady=2)
day = tk.StringVar()                                                                    # To Be Saved (date)
month = tk.StringVar()                                                                  # To Be Saved (month)
year = tk.StringVar()                                                                   # To Be Saved (year)
day_frame = tk.Frame(app)
day_frame.grid(row=3, column=1, pady=2)

# day
daytk = ttk.Combobox(day_frame, width=8, textvariable=day)
daytk['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
daytk.grid(row=0, column=0)                                                             # grid: date

# month
monthtk = ttk.Combobox(day_frame, width=8, textvariable=month)
monthtk['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
monthtk.grid(row=0, column=1)                                                           # grid: month

# year
yeartk = ttk.Entry(day_frame, width=8, textvariable=year)
yeartk.grid(row=0, column=2)                                                            # grid: year

#--------------- Buttons ---------------

try:
    # Save Button
    ttk.Button(app, text="Save", command=lambda: save_function(food_item, quan, address, daytk, monthtk, yeartk, reward, cook)).grid(row=6, columnspan=2, sticky="we")
except:
    msg.showerror("Error", "error")

# View Button
ttk.Button(app, text="View", command=lambda: view_function()).grid(row=7, columnspan=2, sticky="we")


window.mainloop()