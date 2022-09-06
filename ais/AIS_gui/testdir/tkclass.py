import tkinter as tk
from tkinter import ttk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Select Folder")
        self.geometry("800x800")
        self.config(background = "black")
        self.label = ttk.Label(self, text = 'Hello, shit')
        self.label.pack()


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
