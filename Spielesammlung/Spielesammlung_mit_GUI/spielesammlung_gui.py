# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = spielesammlung_gui.py
# __version__   = 0.1

# import tkinter
#
# def end():
#     main.destroy()
#
# def anzeigen():
#     lbAuswahl["text"] = str(choice_menu.get())
#
# def menu():
#     choice_menu.set("0")
#
# def show_zahlenraten():
#     zahlenraten.lift()
#
# def hide_zahlenraten():
#     zahlenraten.lower()
#
# # Hauptfenster erzeugen
# main = tkinter.Tk()
# main.title("Spielesammlung")
# main.geometry ("600x600")
#
# # Startwerte
# choice_menu = tkinter.IntVar()
# choice_menu.set("0")
#
# # Hauptmenü
# menu = tkinter.Frame(main)
# menu.pack()
#
# rb1 = tkinter.Radiobutton(menu, text = "Zahlenraten", variable = choice_menu, value = 10)
# rb1.pack()
# rb2 = tkinter.Radiobutton(menu, text = "Galgenmännchen", variable = choice_menu, value = 20)
# rb2.pack()
# rb3 = tkinter.Radiobutton(menu, text = "Schere, Stein, Papier", variable = choice_menu, value = 30)
# rb3.pack()
#
# buAnzeigen = tkinter.Button(menu, text = "Anzeigen", command = anzeigen)
# buAnzeigen.pack(side = "top")
#
# lbAuswahl = tkinter.Label(menu, text = "Auswahl")
# lbAuswahl.pack()
#
# bu = tkinter.Button(menu, text = "Button zum Beenden", command = end)
# bu.pack()
#
#
#
# # Zahlenraten
# zahlenraten = tkinter.Frame(main)
# zahlenraten.pack()
#
# lbtest = tkinter.Label(main, text = "Test")
# lbtest.pack()
#
# buback = tkinter.Button(menu, text = "Hauptmenü", command = menu)
# buback.pack()
#
# # Hauptmenü
# main.mainloop()


from functools import partial

try:
    # Tkinter for Python 2.xx
    import Tkinter as tk
except ImportError:
    # Tkinter for Python 3.xx
    import tkinter as tk

APP_TITLE = "Lift lower frame to the top"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200

FRAMES = 5


class Application(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)

        for index in range(FRAMES):
            frame = tk.Frame(self, relief='raised', bd=1)
            frame.place(x=20, y=20, width=100, height=100)
            frame.name = "Frame: {}".format(index)
            if index == 0:
                frame['bg'] = 'green'

        frame['bg'] = 'red'

        for child in self.winfo_children():
            print(child.winfo_class(), child.name, child)

        self.after(1000, self.lift_frame)

    def lift_frame(self):
        frame = self.winfo_children()[0]
        frame.lift()


def main():
    app_win = tk.Tk()
    app_win.title(APP_TITLE)
    app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))

    app = Application(app_win).pack(fill='both', expand=True)

    app_win.mainloop()


if __name__ == '__main__':
    main()