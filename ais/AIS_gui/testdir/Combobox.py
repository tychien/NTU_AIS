import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
    print(comboExample.get())

app = tk.Tk()
app.geometry('200x100')

labelTop = tk.Label(app,text = 'Choose your favorite month')
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app,
                            values = [
                                        1,
                                        2, 
                                        3,
                                        "Apr",
                                        "May",
                                        "Jun",
                                        "Jul",
                                        "Aug",
                                        "Sep",
                                        "Oct",
                                        "Nov",
                                        "Dec"],
                            state = "readonly")
comboExample.grid(column=0, row = 1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())
comboExample.bind("<<ComboboxSelected>>", callbackFunc)

app.mainloop()
