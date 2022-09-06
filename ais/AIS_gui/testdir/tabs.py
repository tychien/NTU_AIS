from tkinter import *
import tkinter as tk
from tkinter import ttk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tab Widget")
        tabControl = ttk.Notebook(self)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text= "Shit1")
        tabControl.add(tab2, text= "Shit2")
        tabControl.pack(expand = 1, fill= "both")

        label_tab1= Label(tab1,
                text = "shit1").grid(column = 0,
                                    row     = 0,
                                    padx    = 30,
                                    pady    = 30)
        label_tab2 =Label(tab2,
                text = "shit2").grid(column = 0,
                                    row     = 0,
                                    padx    = 30,
                                    pady    = 30)




if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
