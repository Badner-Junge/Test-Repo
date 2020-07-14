"""FamiliyOrganizer Tabs.

Version: 0.1
Geschrieben von: Fabian Rieger
"""

# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter as tk
import config


class Register:
    """Manage Tabs."""

    def cards(self):
        """Create Tabs."""
        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Übersicht")
        Addings.Tab1(self)

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Kinder")
        Addings.Tab2(self)

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Kalender")
        Addings.Tab3(self)

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Einkaufen")
        Addings.Tab4(self)

        self.tab5 = ttk.Frame(tabControl)
        tabControl.add(self.tab5, text="Rezepte")
        Addings.Tab5(self)

        self.tab6 = ttk.Frame(tabControl)
        tabControl.add(self.tab6, text="Essensplan")
        Addings.Tab6(self)

        tabControl.pack(expand=1, fill="both")

        self.tab_control = tabControl


class Addings:
    """Add to Tabs."""

    def Tab1(self):
        """Tab1."""
        Label(
            self.tab1, text="Please Select your choice", font="Times 24 bold", fg="blue"
        ).place(x=250, y=20)
        Label(
            self.tab1, text="Please Select your choice", font="Times 24 bold", fg="blue"
        ).place(x=125, y=100)

    def Tab2(self):
        """Tab2."""
        Label(self.tab2, text="Please Select your choice").place(x=250, y=40)

    def Tab3(self):
        """Tab3."""
        Label(self.tab3, text="Please Select your choice").place(x=250, y=60)

    def Tab4(self):
        """Tab4."""
        Label(self.tab4, text="Please Select your choice").place(x=250, y=80)

    def Tab5(self):
        """Tab5."""
        Label(self.tab5, text="Please Select your choice").place(x=250, y=100)

    def Tab6(self):
        """Tab6."""
        Label(self.tab6, text="Please Select your choice").place(x=250, y=120)
