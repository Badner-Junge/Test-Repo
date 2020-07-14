from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import os

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Application")
        self.minsize(640, 400)
        self.configure(background="white")

        self.createMenu()

        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="tab 1")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="tab 2")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="tab 3")

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="tab 4")
        self.addingTab4()

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="tab 5")

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="tab 6")

        self.tab7 = ttk.Frame(tabControl)
        tabControl.add(self.tab7, text="Tab 7")

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl

    def startpressed(self):
        new = tk.Toplevel(self)
        new.minsize(640, 400)
        new.geometry("500x300")
        new.configure(background="white")
        tabControl1 = ttk.Notebook(new)
        new.tab1 = ttk.Frame(tabControl1)
        tabControl1.add(new.tab1, text="tab 1")
        tabControl1.pack(expand=1, fill="both")

    def createMenu(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit")

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us")

    def addingTab4(self):
        Label(self.tab4, text="Please Select your choice").place(x=250, y=20)
        submit = Button(self.tab4, text="Submit", command=lambda: self.submit()).place(
            x=520, y=320
        )

    def submit(self):
        newTop = Toplevel(self.master)
        display = Label(newTop, text="Review").pack()
        newTop.title("Review and Submit")
        newTop.focus_set()
        newTop.geometry("400x600")
        # WOULD LIKE: when this button is clicked it takes the user to tab 7 of the notebook window
        btnResult = Button(newTop, text="Tab 7", command=self.result1).pack()
        btnBack = Button(newTop, text="Back").pack()

    def result1(self):
        # ttk.Notebook.select(self.tab7)
        self.tab_control.select(self.tab7)


root = Root()
root.mainloop()
