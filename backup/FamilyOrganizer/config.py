"""FamiliyOrganizer Configuration.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk


class Config:
    """Style Settings"""

    def Tabs(self):
        tabStyle = ttk.Style()
        tabStyle.configure("TNotebook", tabposition="w")
