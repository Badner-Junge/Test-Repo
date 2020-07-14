# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = rock_paper_scissor_gui.py
# __version__   = 0.9


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ToDo Bestenliste mit gesuchter Zahl, Versuchen, mit/ohne Hinweis
# ToDo Fehler: Bestätigen, Neustart, Modus auswählen -> Zähler bleibt eingeblendet
# ToDo Fehler: Modus unbegrenzt, Unentschieden
# ToDo Hintergrund, wenn Stop-Button (Modus: unbegrenzt) wieder ausgeblendet
# ToDo Formatierung

# Debug
class debug():
    global counter_debug
    # Debug anzeigen
    def debug_show(event):
        if counter_debug.get() == 0:
            counter_debug.set("1")
            txdebug = tk.Text(main, width=47, height=9, relief = "sunken", bd = 2)
            txdebug.grid(column=0, row=7)
            txdebug.insert("end", "")

            main.minsize(width=400, height=450)                                                     # min. Fenstergröße
            main.maxsize(width=400, height=450)                                                     # max. Fenstergröße
        else:
            debug.debug_update()
    # Debug aktualisieren
    def debug_update():
        debug.debug_invisible()
        txdebug = tk.Text(main, width=47, height=9, relief="sunken", bd=2)
        txdebug.grid(column=0, row=7)
        txdebug.insert("end", "")
        main.minsize(width=400, height=450)  # min. Fenstergröße
        main.maxsize(width=400, height=450)  # max. Fenstergröße
    # Debug ausblenden
    def debug_invisible():
        children = main.winfo_children()
        for child in children:
            if str(type(child)) == "<class 'tkinter.Text'>":
                child.destroy()
                main.minsize(width=400, height=320)                                             # min. Fenstergröße
                main.maxsize(width=400, height=320)                                             # max. Fenstergröße
                return
    # Debug ausblenden Menü
    def debug_invisible_menu():
        counter_debug.set("0")
        children = main.winfo_children()
        for child in children:
            if str(type(child)) == "<class 'tkinter.Text'>":
                child.destroy()
                main.minsize(width=400, height=320)                                             # min. Fenstergröße
                main.maxsize(width=400, height=320)                                             # max. Fenstergröße
                return

# Bilder
class images():
    # Image Player
    def image_player():
        load = Image.open(symbol[0])
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frplayer, bg = bg, image=render)
        img.image = render
        img.grid(column=0, row=2, columnspan=2, rowspan=3)
    # Image Computer
    def image_computer():
        load = Image.open(symbol[1])
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frcomputer, bg = bg, image=render)
        img.image = render
        img.grid(column=0, row=2, columnspan=2, rowspan=3)

# # Auswahl Modus
# class mode():
#
# # Interface Änderungen
# class interface():
#
# # Eingabe
# class guess():
#
# Werte zurücksetzten
def reset():
    pass

# Programm Ende
def end():
    main.destroy()

# Optionen
bg = "beige"                                                                                # Allgemeine Hintergrundfarbe

# Hauptfenster
main = tk.Tk()
main.title("Spielesammlung")                                                                # Fenstername
main.configure(bg = bg)                                                                     # Hintergrundfarbe
main.minsize(width=400, height=320)                                                         # min. Fenstergröße
main.maxsize(width=400, height=320)                                                         # max. Fenstergröße
main.columnconfigure(0, weight = 3)                                                         # Zentrieren

# Startwerte Variablen
counter_debug = tk.IntVar()
counter_debug.set("0")                                                                      # Zähler Debug
symbol = ["X.png", "O.png"]                                                                 # Bilder


# Hauptfenster Header
lbheader = tk.Label(main, width = 43, bg = "brown", fg = "white", text = "************** Tic Tac Toe **************",
                    font = "Times 16 bold", relief = "raised", bd = 4)
lbheader.bind("<Double-1>", debug.debug_show)
lbheader.grid(column = 0, row = 0, columnspan = 3)

# Menü
mBar = tk.Menu(main)

mFile = tk.Menu(mBar)
mDebug = tk.Menu(mBar)

mBar.add_cascade(label = "Datei", menu = mFile, underline = 0)
mBar.add_cascade(label = "Debugger", menu = mDebug, underline = 0)

mFile.add_command(label = "Neustart", underline = 0, command = reset)
mFile.add_separator()
mFile.add_command(label = "Beenden", command = end)

mDebug.add_command(label = "Debugger aus", command = debug.debug_invisible_menu)

main["menu"] = mBar

# Anweisung
    # Anweisung Frame
frintroduction = tk.Frame(main, relief = "sunken", bd = 3)
frintroduction.configure(bg = bg)
frintroduction.grid(column = 0, row = 1, columnspan = 3)
    # Anweisung Text
txinstruction = tk.Text(frintroduction, bg = bg, width = 48, height = 2)
txinstruction.grid(column = 0, row = 0, columnspan = 3)
txinstruction.insert(tk.INSERT, "Gewinne, indem du von deinen Symbolen,\n"
                                "3 in einer Reihe platzierst!")

# Spielfeld
    # Hauptfenster
catable = tk.Canvas(main, width = 210, height = 210, highlightbackground = "sandybrown", bg = "peru", relief = "groove", bd = 5)
catable.grid(column = 0, row = 2, sticky = "w", padx = 25, pady = 5)
catable_bg = tk.Canvas(catable, width = 210, height = 210, highlightbackground = "sandybrown", bg = "peru", relief = "groove", bd = 5)
catable_bg.grid(column = 0, row = 0)

table = tk.PhotoImage(file = "table.png")
catable_bg.create_image(113,113,image = table)

    # Feld 1
# img_player = tk.PhotoImage(file = "X.png")
# cafield_1 = tk.Canvas(catable, width = 9, height = 4)
# cafield_1.grid(column = 0, row = 0)
# cafield_1.create_image(60,60,image=img_player)
# field_2 = tk.Text(frtable, width = 9, height = 4)
# field_2.grid(column = 1, row = 0)
# field_3 = tk.Text(frtable, width = 9, height = 4, bg = "green")
# field_3.grid(column = 2, row = 0)
# field_4 = tk.Text(frtable, width = 9, height = 4, bg = "red")
# field_4.grid(column = 1, row = 1)
# field_5 = tk.Text(frtable, width = 9, height = 4, bg = "orange")
# field_5.grid(column = 0, row = 2)

    # Canvas
# catable = tk.Canvas(main, width = 200, height = 200, highlightbackground = "sandybrown", bg = "peru", relief = "groove", bd = 5)
# catable.grid_columnconfigure(2, weight = 5)
# catable.grid_rowconfigure(2, weight = 5)
# catable.grid(column = 0, row = 2, sticky = "w", padx = 25, pady = 5)
    # Linien
# catable.create_line(5, 70, 205, 70, fill = "black", width = 3)
# catable.create_line(5, 140, 205, 140, fill = "black", width = 3)
# catable.create_line(70, 5, 70, 205, fill = "black", width = 3)
# catable.create_line(140, 5, 140, 205, fill = "black", width = 3)

# field_1 = tk.Canvas(catable, width = 60, height = 60)
# # field_1.grid(column = 0, row = 0)
# # catable.create_window(20,20, window = field_1)
# catable.create_window(20,20, window=field_1)

# Interface
    # Interface Frame


    # Interface Bilder
#         # Spieler
# frplayer = tk.Frame(catable, bg = "red", relief = "sunken", bd = 0)
# frplayer.configure(height = 60, width = 60)
# frplayer.grid(column = 0, row = 0)
#         # Computer
# frcomputer = tk.Frame(frinterface, bg = bg, relief = "sunken", bd = 0)
# frcomputer.configure(height = 100, width = 120)
# frcomputer.grid(column = 5, row = 1)

    # Interface Knöpfe
        # Frame Mitte
# frmiddle = tk.Frame(frinterface, bg="peru", relief="raised", bd=4)
# frmiddle.configure(height=100, width=120)
# frmiddle.grid(column=3, row=1)

    # Interface Radiobutton
        # Frame Radio
frradio = tk.Frame(main, bg = "sandybrown", relief="groove", bd=2)
frradio.grid(column = 1, row = 2)
            # Schere
# rbscissor = tk.Radiobutton(frradio, bg = "sandybrown", text = "Schere", variable = pic_player, value = 0)
# rbscissor.grid(column = 0, row = 0, sticky = "w")
#             # Stein
# rbrock = tk.Radiobutton(frradio, bg = "sandybrown", text = "Stein", variable = pic_player, value = 1)
# rbrock.grid(column = 0, row = 1, sticky = "w")
#             # Papier
# rbpaper = tk.Radiobutton(frradio, bg = "sandybrown", text = "Papier", variable = pic_player, value = 2)
# rbpaper.grid(column = 0, row = 2, sticky = "w")

    # Interface Bottom
            # Accept
# buaccept = tk.Button(frradio, highlightbackground = "sandybrown", text = "Bestätigen", relief = "ridge", command = guess.guess)
# buaccept.grid(column = 0, row = 3)
            # Restart
burestart = tk.Button(frradio, highlightbackground = "sandybrown", text = "Neustart", relief = "ridge", command = reset)
burestart.grid(column = 1, row = 0, rowspan = 2)
            # Beenden
buend = tk.Button(frradio, highlightbackground = "sandybrown", text = "Beenden", relief = "ridge", command = end)
buend.grid(column = 1, row = 2, rowspan = 2)

# Hauptprogrammschleife starten
main.mainloop()