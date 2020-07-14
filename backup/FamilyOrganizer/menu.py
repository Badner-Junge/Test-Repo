"""FamiliyOrganizer Menü.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import config


class menuBar:
    """Create Menubar."""

    def createMenu(self):
        """Create Menu Categories."""
        menubar = Menu(self)
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Beenden", command=self.end)

        visual_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Darstellung", menu=visual_menu)
        visual_menu.add_command(label="Vollbild", command=self.fullscreen_toggle)
        # visual_menu.add_command(label="Vollbild aus", command=self.fullscreen_off)

        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About Us")


class options:
    """Option Settings."""

    def fullscreen_toggle(self):
        """Switch Fullscreen on/off."""
        if self.attributes("-fullscreen") == FALSE:
            self.attributes("-fullscreen", TRUE)
        else:
            self.attributes("-fullscreen", FALSE)
