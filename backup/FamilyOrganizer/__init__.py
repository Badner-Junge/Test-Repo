"""FamiliyOrganizer Main.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import os
import menu, modules, tabs, config

if os.environ.get("DISPLAY", "") == "":
    print("no display found. Using :0.0")
    os.environ.__setitem__("DISPLAY", ":0.0")


class Root(Tk):
    """Main Window."""

    def __init__(self):
        """Initialize."""
        super(Root, self).__init__()
        self.title("Family Organizer")
        self.attributes("-fullscreen", TRUE)
        self.minsize(512, 265)
        self.configure(background="white")

        menu.menuBar.createMenu(self)
        config.Config.Tabs(self)
        tabs.Register.cards(self)

    def fullscreen_toggle(self):
        """Fullscreen from menu.py."""
        menu.options.fullscreen_toggle(self)

    def end(self):
        """Close Main Window."""
        root.destroy()


root = Root()
root.mainloop()
