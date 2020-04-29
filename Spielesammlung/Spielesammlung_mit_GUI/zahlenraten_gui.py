# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = zahlenraten_gui.py
# __version__   = 0.9


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ToDo Bestenliste mit gesuchter Zahl, Versuchen, mit/ohne Hinweis
# ToDo Hintergrund, wenn Hinweis-Button wieder ausgeblendet
# ToDo Formatierung

# Debug anzeigen
def debug_show(event):
    global debug
    if debug == 0:
        debug = debug + 1
        txdebug = tk.Text(main, width=47, height=9, relief = "sunken", bd = 2)
        txdebug.grid(column=0, row=5)
        txdebug.insert("end", "Zufallszahl: " + str(secret) + "\nEingabe: " + str(guess) + "\nEingabe Liste:" +
                       str(guesslist) + "\nEingabe Liste gültig:" + str(guesslist_correct) + "\nVersuchszähler:" +
                       str(versuch) + "\nBild:" + str(pic) + "\nHinweiszähler:" + str(hint_counter) +
                       "\nHinweis hinzufügen:" + str(hint_add) + "\nHinweisliste:" + str(hint_list) + "\nDebug:"
                       + str(debug))
        main.minsize(width=400, height=450)                                                     # min. Fenstergröße
        main.maxsize(width=400, height=450)                                                     # max. Fenstergröße
    else:
        debug_update()
# Debug aktualisieren
def debug_update():
    debug_invisible()
    txdebug = tk.Text(main, width=47, height=9, relief = "sunken", bd = 2)
    txdebug.grid(column=0, row=5)
    txdebug.insert("end", "Zufallszahl: " + str(secret) + "\nEingabe: " + str(guess) + "\nEingabe Liste:" +
                   str(guesslist) + "\nEingabe Liste gültig:" + str(guesslist_correct) + "\nVersuchszähler:" +
                   str(versuch) + "\nBild:" + str(pic) + "\nHinweiszähler:" + str(hint_counter) +
                   "\nHinweis hinzufügen:" + str(hint_add) + "\nHinweisliste:" + str(hint_list) + "\nDebug:"
                   + str(debug))
    main.minsize(width=400, height=450)                                                     # min. Fenstergröße
    main.maxsize(width=400, height=450)                                                     # max. Fenstergröße
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
    global debug
    debug = debug - 1
    children = main.winfo_children()
    for child in children:
        if str(type(child)) == "<class 'tkinter.Text'>":
            child.destroy()
            main.minsize(width=400, height=320)                                             # min. Fenstergröße
            main.maxsize(width=400, height=320)                                             # max. Fenstergröße
            return

# Neue Zufallszahl + Startwerte zurücksetzen
def restart():
    global guess, versuch, hint_add, hint_list, hint_counter, pic, debug
    random.seed
    # Erste Zufallszahl generieren
    if secret == []:
        number = random.randint(999, 10000)
        secret.append(number)
    # Neue Zufallszahl generieren und alte löschen
    else:
        number = random.randint(999, 10000)
        secret.append(number)
        secret.remove(secret[0])
    # Startwerte zurücksetzen
    debug = 0
    guess = ""
    guesslist.clear()
    guesslist_correct.clear()
    hint_add = []
    hint_list = []
    enguess.delete(0, "end")
    lxout.delete(1.0, "end")
    versuch = 0
    hint_counter = 2
    pic = 0
    hint_invisible()
    debug_invisible()
    arrow()

# Hinweis
    # Hinweis-Button anzeigen
def hint():
    hinweis = tk.Button(frhint, highlightbackground = "beige", text="Hinweis", relief="ridge", command = hint_view)
    hinweis.grid(column=1, row=2, rowspan = 3)
    # Hinweis anzeigen
def hint_view():
    global hint_counter, versuch
    if hint_counter == 1:
        lxout.delete(1.0, "end")
        hint_counter = hint_counter - 1
        for i in hint_list:
            lxout.insert("end", i)
            lxout.insert("end", "\n")
    else:
        lxout.delete(1.0, "end")
        lxout.insert("end", "Hinweis schon verwendet")
    hint_invisible()
    # Hinweis-Button ausblenden
def hint_invisible():
    children = frhint.winfo_children()
    for child in children:
        if str(type(child)) == "<class 'tkinter.Button'>":
            child.destroy()
            return

# Eingabe durch Enter
def eingabe_return(event):
    global hint_add, guess, hint_counter, debug
    # Hinweis noch verfügbar
    if hint_counter == 0:
        try:
            guess = int(enguess.get())
            lxout.delete(1.0, "end")
            enguess.select_range(0, "end")
            check()
        except:
            only_numbers()
        hint_invisible()
    # Hinweis nicht mehr verfügbar
    else:
        try:
            guess = int(enguess.get())
            lxout.delete(1.0, "end")
            enguess.select_range(0, "end")
            check()
        except:
            only_numbers()
    # Eintrag in Hinweisliste, solange Hinweis verfügbar
    if versuch != 0:
        hint_add = [versuch, guess, hint_text]
        hint_list.append(hint_add)
    # Debugger updaten
    if debug == 1:
        debug_update()

# Bild
def arrow():
    load = Image.open(image[pic])
    render = ImageTk.PhotoImage(load)
    img = tk.Label(frinterface, bg = bg, image=render)
    img.image = render
    img.grid(column=0, row=2, columnspan=2, rowspan=3)

# Eingabe auswerten
    # Ungültige Eingabe
def only_numbers():
    tk.messagebox.showinfo("Falsche Eingabe", "Es sind nur Zahlen erlaubt!")
    enguess.delete(0, "end")
    lxout.delete(1.0, "end")
    lxout.insert("end", "Deine letzte gültige Eingabe war:\n"
               + str(guesslist_correct[-1]), "center")                                      # letzte Eingabe
    # Gültige Eingabe
def check():
    global hint_text, hint_counter, hint_add, hint_list, versuch, pic, guess
    # Zahl bereits versucht
    if guesslist.count(guess) == 1:
        lxout.insert("end", "Die Zahl hattest du bereits!", "center")
        versuch = versuch + 1
        if hint_counter == 2:
            hint_counter = hint_counter - 1
            hint()
        hint_text = "Bereits versucht"
        # Bereits versuchte Zahl suchen und pic-Wert setzen
        for x in hint_list:
            if x[1] == guess:
                if guess > secret[0]:
                    pic = 4
                elif guess > secret[0] + 10:
                    pic = 3
                elif guess < secret[0]:
                    pic = 2
                elif guess < secret[0] - 10:
                    pic = 1
        arrow()
    # Zahl gültig
    else:
        # Eintrag in Liste
        guesslist.append(guess)
        # Zahl zu klein/groß
        if guess < 1000 or guess > 9999:
            lxout.insert("end", "Die gesuchte Zahl \n"
                       "ist 4-stellig.", "center")
            versuch = versuch + 1
            hint_text = "4-stellig"
        # Zahl ist kleiner
        elif guess > secret[0]:
            if guess < secret[0] + 10:
                lxout.insert("end", "Nah dran, aber die \n"
                            "gesuchte Zahl ist kleiner.", "center")
                versuch = versuch + 1
                hint_text = "Nah dran, kleiner"
                pic = 3
            else:
                lxout.insert("end", "Die gesuchte Zahl ist kleiner.", "center")
                versuch = versuch + 1
                hint_text = "Kleiner"
                pic = 4
            guesslist_correct.append(guess)
            arrow()
        # Zahl ist größer
        elif guess < secret[0]:
            if guess > secret[0] - 10:
                lxout.insert("end", "Nah dran, aber die \n"
                            "gesuchte Zahl ist größer.", "center")
                versuch = versuch + 1
                hint_text = "Nah dran, größer"
                pic = 1
            else:
                lxout.insert("end", "Die gesuchte Zahl ist größer.", "center")
                versuch = versuch + 1
                hint_text = "Größer"
                pic = 2
            guesslist_correct.append(guess)
            arrow()
        # Zahl erraten
        else:
            retry = tk.messagebox.askyesno("Zahlenraten", "Super! Du hast hast die Zahl nach dem " + str(versuch + 1) +
                                           ". Versuch erraten!\n"
                                           "\nDie gesuchte Zahl war: " + str(secret[0]) +
                                           "\nMöchtest du noch eine Runde spielen?")
            if retry == 0:
                end()
            else:
                restart()

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
debug = 0
secret = []                                                                                 # Zufallszahl
guess = tk.StringVar()                                                                      # Eingabe
guess.set("")
guesslist = []                                                                              # Eingaben Liste
guesslist_correct = []                                                                      # Eingaben Liste gültig
versuch = 0                                                                                 # Versuchszähler
image = ["neutral.png", "green-near.png", "green-far.png", "red-near.png", "red-far.png"]   # Bild
pic = 0                                                                                     # Bilderauswahl
hint_counter = 2                                                                            # Hinweiszähler
hint_add = []                                                                               # Hinweis hinzufügen
hint_text = ""                                                                              # Hinweis Text
hint_list = []                                                                              # Hinweisliste

# Hauptfenster Header
lbheader = tk.Label(main, width = 43, bg = "brown", fg = "white", text = "************* Zahlenraten *************",
                    font = "Times 16 bold", relief = "raised", bd = 4)
lbheader.bind("<Double-1>", debug_show)
lbheader.grid(column = 0, row = 0)

# Menü
mBar = tk.Menu(main)

mFile = tk.Menu(mBar)
mDebug = tk.Menu(mBar)

mBar.add_cascade(label = "Datei", menu = mFile, underline = 0)
mBar.add_cascade(label = "Debugger", menu = mDebug, underline = 0)

mFile.add_command(label = "Neue Zahl", underline = 0, command = restart)
mFile.add_separator()
mFile.add_command(label = "Beenden", command = end)

mDebug.add_command(label = "Debugger aus", command = debug_invisible_menu)

main["menu"] = mBar

# Anweisung
    # Anweisung Frame
frintroduction = tk.Frame(main, relief = "sunken", bd = 3)
frintroduction.configure(bg = bg)
frintroduction.grid(column = 0, row = 1)
    # Anweisung Text
txinstruction = tk.Text(frintroduction, bg = bg, width = 48, height = 5, relief = "sunken", bd = 1)
txinstruction.grid(column = 0, row = 0, columnspan = 5)
txinstruction.insert(tk.INSERT, "Errate die geheime Zahl! \n"
                                "\nGibst du eine Zahl zum 2. Mal ein, hast du"
                                "\ndie Möglichkeit, dir einmalig deinen\n"
                                "Verlauf (Hinweis) zeigen zu lassen.")

# Interface
    # Interface Frame
frinterface = tk.Frame(main, bg = bg, relief = "sunken", bd = 0)
frinterface.grid(column = 0, row = 2, columnspan = 2)
    # Interface Eingabe
laguess = tk.Label(frinterface, bg = bg, text = "Gib hier deine Zahl ein:")
laguess.grid(column = 0, row = 0)

enguess = tk.Entry(frinterface, bg = "lightgrey", relief = "sunken", bd = 0)
enguess.grid(column = 1, row = 0)
enguess.bind("<Return>", eingabe_return)                                                    # Eingabe durch Enter

    # Interface Ausgabe
scbout = tk.Scrollbar(frinterface, orient = "vertical")
lxout = tk.Text(frinterface, width = 45, height = 5, relief = "sunken", bd = 1, yscrollcommand = scbout.set)
lxout.tag_configure("center", justify = "center")
lxout.tag_add("center", 1.0, "end")
lxout.grid(column = 0, row = 1, columnspan = 2)
scbout["command"] = lxout.yview()
scbout.place(x = 333, y = 27)
    # Bild Frame
frimage = tk.Frame(frinterface, bg = bg, relief = "sunken", bd = 0)
frimage.configure(width = 40)
frimage.grid(column = 0, row = 2, columnspan = 2, rowspan = 3)

# Knöpfe
    # Frame Hinweis-Knopf
frhint = tk.Frame(frinterface)
frhint.grid(column = 1, row = 2, rowspan = 3)
    # Neue Zahl
burestart = tk.Button(frinterface, highlightbackground = bg, text = "Neue Zahl", relief = "ridge", command = restart)
burestart.grid(column = 0, row = 2, rowspan = 2)
    # Beenden
buend = tk.Button(frinterface, highlightbackground = bg, text = "Beenden", relief = "ridge", command = end)
buend.grid(column = 0, row = 4, rowspan = 2)

# Hauptprogrammschleife starten
restart()
arrow()
main.mainloop()