# testing things in Tkinter
from tkinter import *
import time

class App:
    def __init__(self, window, name):
        self.mainframe = Frame(window)
        self.mainframe.config(highlightthickness = 1, highlightbackground = 'black')
        self.mainframe.pack()
        self.name = Label(self.mainframe, text=name)
        self.name.pack()
        window.mainloop()

    def add_button(self):
        pass

root = Tk()
app = App(root,"Hello World")
time.sleep(3)
app = App(root, "Hey Marge")
