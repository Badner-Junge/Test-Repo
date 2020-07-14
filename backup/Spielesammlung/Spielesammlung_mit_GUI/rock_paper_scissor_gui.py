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
            txdebug.insert("end", "Bild Spieler: " + str(pic_player.get()) + "\nBild Computer: "
                           + str(pic_computer.get()) + "\nModus:" + str(mode_choice.get()) + "\nVersuchszähler:"
                           + str(versuch.get()) + "\nDebug Zähler:" + str(counter_debug.get())
                           + "\nModus Zähler:" + str(counter_mode.get())+ "\nVersuch Ref:" + str(versuch_ref.get()))

            main.minsize(width=400, height=450)                                                     # min. Fenstergröße
            main.maxsize(width=400, height=450)                                                     # max. Fenstergröße
        else:
            debug.debug_update()
    # Debug aktualisieren
    def debug_update():
        debug.debug_invisible()
        txdebug = tk.Text(main, width=47, height=9, relief="sunken", bd=2)
        txdebug.grid(column=0, row=7)
        txdebug.insert("end", "Bild Spieler: " + str(pic_player.get()) + "\nBild Computer: "
                           + str(pic_computer.get()) + "\nModus:" + str(mode_choice.get()) + "\nVersuchszähler:"
                           + str(versuch.get()) + "\nDebug Zähler:" + str(counter_debug.get())
                           + "\nModus Zähler:" + str(counter_mode.get())+ "\nVersuch Ref:" + str(versuch_ref.get()))
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
        load = Image.open(image_choice[pic_player.get()])
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frplayer, bg = bg, image=render)
        img.image = render
        img.grid(column=0, row=2, columnspan=2, rowspan=3)
    # Image Computer
    def image_computer():
        load = Image.open(image_choice[pic_computer.get()])
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frcomputer, bg = bg, image=render)
        img.image = render
        img.grid(column=0, row=2, columnspan=2, rowspan=3)

# Auswahl Modus
class mode():
    # Best of 5
    def bo5():
        mode_choice.set("1")
        versuch.set("5")
        versuch_ref.set("5")
        counter_mode.set("1")
        interface.mode_invisible()
        interface.mode_invisible()
        interface.mode_invisible()
        interface.counter_show()
        if counter_debug.get() == 1:
            debug.debug_update()
    # Best of 10
    def bo10():
        mode_choice.set("2")
        versuch.set("10")
        versuch_ref.set("10")
        counter_mode.set("1")
        interface.mode_invisible()
        interface.mode_invisible()
        interface.mode_invisible()
        interface.counter_show()
        if counter_debug.get() == 1:
            debug.debug_update()
    # unbegrenzt
    def unlimited():
        global frstop
        mode_choice.set("3")
        versuch.set("0")
        counter_mode.set("1")
        interface.mode_invisible()
        interface.mode_invisible()
        interface.mode_invisible()
        interface.counter_show()
        if counter_debug.get() == 1:
            debug.debug_update()
        # Button Runde beenden
        frstop = tk.Frame(frradio, highlightbackground="sandybrown")
        frstop.grid(column=1, row=1, rowspan=2)

        burestop = tk.Button(frstop, highlightbackground="sandybrown", text="Stop", relief="ridge",
                             command=guess.game_over)
        burestop.grid(column=1, row=1, rowspan=2)
    # Button Stop ausblenden
    def unlimited_invisible():
        children = frstop.winfo_children()
        for child in children:
            if str(type(child)) == "<class 'tkinter.Button'>":
                child.destroy()
                return

# Interface Änderungen
class interface():
    # Buttons anzeigen
    def mode_show():
        # Best of 5
        bubo5 = tk.Button(frmiddle, highlightbackground="peru", text="Best of 5", relief="raised", command=mode.bo5)
        bubo5.grid(column=1, row=0)
        # Best of 10
        bubo10 = tk.Button(frmiddle, highlightbackground="peru", text="Best of 10", relief="raised", command=mode.bo10)
        bubo10.grid(column=1, row=1)
        # unbegrenzt
        buunlim = tk.Button(frmiddle, highlightbackground="peru", text="unbegrenzt", relief="raised", command=mode.unlimited)
        buunlim.grid(column=1, row=2)
        interface.counter_invisible()
    # Buttons ausblenden
    def mode_invisible():
        children = frmiddle.winfo_children()
        for child in children:
            if str(type(child)) == "<class 'tkinter.Button'>":
                child.destroy()
                return
    # Zähler einblenden
    def counter_show():
        global counter_mode, frcounter
        # Erststart
        if counter_mode.get() == 1:
            frcounter = tk.Frame(frmiddle, width=10, height=3, bg="peru")
            frcounter.grid(column=0, row=0)

            txplayer = tk.Text(frcounter, width=8, height=1, highlightbackground="peru", bg="peru",
                               font="Times 13 bold")
            txplayer.grid(column=0, row=0)
            txplayer.insert("end", "Du:")

            txcounter = tk.Text(frcounter, width=8, height=2, highlightbackground="chocolate", bg="chocolate",
                                relief="sunken", bd=2, font="Times 16 bold")
            txcounter.grid(column=0, row=1)
            txcounter.insert("end", counter_player)
            txcounter.insert("end", " : ")
            txcounter.insert("end", counter_computer)
            txcounter.tag_configure("center", justify='center')
            txcounter.tag_add("center", 1.0, "end")

            txcomputer = tk.Text(frcounter, width = 8, height = 1, highlightbackground = "peru", bg = "peru",
                                 font="Times 13 bold")
            txcomputer.grid(column=0, row=2)
            txcomputer.insert("end", ":PC")
            txcomputer.tag_configure("right", justify='right')
            txcomputer.tag_add("right", 1.0, "end")
        # Zähler aktualisieren
        else:
            txcounter = tk.Text(frcounter, width=8, height=2, highlightbackground="chocolate", bg="chocolate",
                                relief="sunken", bd=2, font="Times 16 bold")
            txcounter.grid(column=0, row=1)
            txcounter.insert("end", counter_player)
            txcounter.insert("end", " : ")
            txcounter.insert("end", counter_computer)
            txcounter.tag_configure("center", justify='center')
            txcounter.tag_add("center", 1.0, "end")
    # Zähler ausblenden
    def counter_invisible():
        children = frmiddle.winfo_children()
        for child in children:
            if str(type(child)) == "<class 'tkinter.Frame'>":
                child.destroy()
                return

# Eingabe
class guess():
    random.seed
    global counter_player, counter_computer, counter_mode, mode_choice, versuch, counter_debug
    # Eingabe auswerten
    def guess():
        counter_mode.set("2")
        if versuch.get() == -1:
            tk.messagebox.showinfo("Runde vorbei", "Starte eine neue Runde!")
            reset()
        else:
            if mode_choice.get() != 0:
                # Modus unbegrenzt
                if mode_choice.get() == 3:
                    # Auswahl Computer
                    pic_computer.set(random.randint(3, 5))
                    # Versuch dazuzählen
                    versuch.set(versuch.get() + 1)
                    # Bilder aktualisieren
                    images.image_player()
                    images.image_computer()
                    # Gesten vergleichen
                    guess.guess_evaluate()
                    if versuch.get() < 0:
                        guess.draw()
                    interface.counter_show()
                # Modus Bo5/Bo10
                else:
                    # Auswahl Computer
                    pic_computer.set(random.randint(3, 5))
                    # pic_computer.set("5")                                                     # Test: Computer nur Blatt
                    # Versuch abziehen
                    versuch.set(versuch.get() - 1)
                    # Bilder aktualisieren
                    images.image_player()
                    images.image_computer()
                    # Gesten vergleichen
                    guess.guess_evaluate()
                    interface.counter_show()
                    guess.game_over()
            # Info "Erst Modus wählen"
            else:
                tk.messagebox.showinfo("Modus", "Du musst zuerst einen Modus wählen!")
    # Ergebnisse auswerten
    def game_over():
        # Mehr als die Hälfte gewonnen
        if versuch.get() >= 1 and mode_choice.get() != 3:
            if counter_player > versuch_ref.get()/2:
                tk.messagebox.showinfo("Runde vorbei", "Gewonnen")
                versuch.set("-1")
            elif counter_computer > versuch_ref.get() / 2:
                tk.messagebox.showinfo("Runde vorbei", "Leider verloren!")
                versuch.set("-1")
        # Unentschieden
        elif versuch.get() < 0:
            guess.draw()
        # Keine Versuche mehr
        else:
            if counter_player > counter_computer:
                tk.messagebox.showinfo("Runde vorbei", "Gewonnen")
                versuch.set("-1")
            elif counter_player < counter_computer:
                tk.messagebox.showinfo("Runde vorbei", "Leider verloren!")
                versuch.set("-1")
            # Unentschieden + letzte Runde
            else:
                tk.messagebox.showinfo("Runde vorbei", "Unentschieden!\n"
                                                       "\nHier kommt die alles entscheidende Runde!")
                if mode_choice.get() == 3:
                    versuch.set("-2")

    # Gesten vergleichen
    def guess_evaluate():
        global counter_player, counter_computer
        # Schere / Papier
        if pic_player.get() == 0 and pic_computer.get() == 5:
            counter_player = counter_player + 1
        # Schere / Stein
        elif pic_player.get() == 0 and pic_computer.get() == 4:
            counter_computer = counter_computer + 1
        # Stein / Schere
        elif pic_player.get() == 1 and pic_computer.get() == 3:
            counter_player = counter_player + 1
        # Stein / Papier
        elif pic_player.get() == 1 and pic_computer.get() == 5:
            counter_computer = counter_computer + 1
        # Papier / Stein
        elif pic_player.get() == 2 and pic_computer.get() == 4:
            counter_player = counter_player + 1
        # Papier / Schere
        elif pic_player.get() == 2 and pic_computer.get() == 3:
            counter_computer = counter_computer + 1
        if counter_debug.get() == 1:
            debug.debug_update()
    # Runde bei Unentschieden
    def draw():
        # Auswahl Computer
        random.seed
        pic_computer.set(random.randint(3, 5))
        while pic_player.get() == 0 and pic_computer.get() == 3 or pic_player.get() == 1 and pic_computer.get() == 4 or pic_player.get() == 2 and pic_computer.get() == 5:
            pic_computer.set(random.randint(3, 5))
        # Bilder aktualisieren
        images.image_player()
        images.image_computer()
        # Gesten vergleichen
        guess.guess_evaluate()
        interface.counter_show()
        if counter_player > counter_computer:
            tk.messagebox.showinfo("Runde vorbei", "Gewonnen")
        elif counter_player < counter_computer:
            tk.messagebox.showinfo("Runde vorbei", "Leider verloren!")

# Werte zurücksetzten
def reset():
    global counter_player, counter_computer, counter_mode
    if mode_choice.get() == 3:                                                              # Stop Button ausblenden,
        mode.unlimited_invisible()                                                          # falls sichtbar
    versuch.set("0")                                                                        # Versuche reset
    versuch_ref.set("0")                                                                    # Versuche Referenz reset
    counter_player = 0                                                                      # Zähler Spieler reset
    counter_computer = 0                                                                    # Zähler Computer reset
    counter_mode.set("0")                                                                   # Zähler Modus reset
    pic_player.set("0")                                                                     # Spieler Auswahl reset
    pic_computer.set("5")                                                                   # Computer Auswahl reset
    images.image_player()                                                                   # Spieler Bild reset
    images.image_computer()                                                                 # Computer Bild reset
    mode_choice.set("0")                                                                    # Modus reset
    interface.counter_invisible()                                                           # Zähler ausblenden
    interface.mode_show()                                                                   # Buttons einblenden
    if counter_debug.get() == 1:                                                            # Debug aktualisieren,
        debug.debug_update()                                                                # falls sichtbar

# Programm Ende
def end():
    main.destroy()

# Optionen
bg = "beige"                                                                                # Allgemeine Hintergrundfarbe

# Hauptfenster
main = tk.Tk()
main.title("Spielesammlung")                                                                # Fenstername
main.configure(bg = bg)                                                                     # Hintergrundfarbe
main.minsize(width=400, height=400)                                                         # min. Fenstergröße
main.maxsize(width=400, height=400)                                                         # max. Fenstergröße
main.columnconfigure(0, weight = 3)                                                         # Zentrieren

# Startwerte Variablen
counter_player = 0                                                                          # Zähler Spieler
counter_computer = 0                                                                        # Zähler Computer
counter_mode = tk.IntVar()
counter_mode.set("0")                                                                       # Zähler Modus
counter_debug = tk.IntVar()
counter_debug.set("0")                                                                      # Zähler Debug
image_choice = ["left_scissor.png", "left_rock.png", "left_paper.png",
                "right_scissor.png", "right_rock.png", "right_paper.png"]                   # Bilder
pic_player = tk.IntVar()
pic_player.set("0")                                                                         # Spieler Bildauswahl
pic_computer = tk.IntVar()
pic_computer.set("5")                                                                       # Computer Bildauswahl
mode_choice = tk.IntVar()
mode_choice.set("0")                                                                        # Modus
versuch = tk.IntVar()
versuch.set("0")                                                                            # Versuchszähler
versuch_ref = tk.IntVar()
versuch_ref.set("0")                                                                        # Versuche Referenz

# Hauptfenster Header
lbheader = tk.Label(main, width = 43, bg = "brown", fg = "white", text = "********* Schere, Stein, Papier *********",
                    font = "Times 16 bold", relief = "raised", bd = 4)
lbheader.bind("<Double-1>", debug.debug_show)
lbheader.grid(column = 0, row = 0)

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
frintroduction.grid(column = 0, row = 1)
    # Anweisung Text
txinstruction = tk.Text(frintroduction, bg = bg, width = 48, height = 4)
txinstruction.grid(column = 0, row = 0, columnspan = 5)
txinstruction.insert(tk.INSERT, "Schlage deinen Gegen!\n"
                                "\nWähle Schere, Stein oder Papier, um"
                                "\ndeinen Gegner zu besiegen!\n")

# Interface
    # Interface Frame
frinterface = tk.Frame(main, width = 45, height = 5, bg = bg, relief = "sunken", bd = 0)
frinterface.grid(column = 0, row = 2, columnspan = 3)
    # Interface Bilder
        # Spieler
frplayer = tk.Frame(frinterface, bg = bg, relief = "sunken", bd = 0)
frplayer.configure(height = 100, width = 120)
frplayer.grid(column = 0, row = 1)
        # Computer
frcomputer = tk.Frame(frinterface, bg = bg, relief = "sunken", bd = 0)
frcomputer.configure(height = 100, width = 120)
frcomputer.grid(column = 5, row = 1)

    # Interface Knöpfe
        # Frame Mitte
frmiddle = tk.Frame(frinterface, bg="peru", relief="raised", bd=4)
frmiddle.configure(height=100, width=120)
frmiddle.grid(column=3, row=1)

    # Interface Radiobutton
        # Frame Radio
frradio = tk.Frame(main, bg = "sandybrown", relief="groove", bd=2)
frradio.grid(column = 0, row = 3)
            # Schere
rbscissor = tk.Radiobutton(frradio, bg = "sandybrown", text = "Schere", variable = pic_player, value = 0)
rbscissor.grid(column = 0, row = 0, sticky = "w")
            # Stein
rbrock = tk.Radiobutton(frradio, bg = "sandybrown", text = "Stein", variable = pic_player, value = 1)
rbrock.grid(column = 0, row = 1, sticky = "w")
            # Papier
rbpaper = tk.Radiobutton(frradio, bg = "sandybrown", text = "Papier", variable = pic_player, value = 2)
rbpaper.grid(column = 0, row = 2, sticky = "w")

    # Interface Bottom
            # Accept
buaccept = tk.Button(frradio, highlightbackground = "sandybrown", text = "Bestätigen", relief = "ridge", command = guess.guess)
buaccept.grid(column = 0, row = 3)
            # Restart
burestart = tk.Button(frradio, highlightbackground = "sandybrown", text = "Neustart", relief = "ridge", command = reset)
burestart.grid(column = 1, row = 0, rowspan = 2)
            # Beenden
buend = tk.Button(frradio, highlightbackground = "sandybrown", text = "Beenden", relief = "ridge", command = end)
buend.grid(column = 1, row = 2, rowspan = 2)

# Hauptprogrammschleife starten
interface.mode_show()
images.image_player()
images.image_computer()
main.mainloop()