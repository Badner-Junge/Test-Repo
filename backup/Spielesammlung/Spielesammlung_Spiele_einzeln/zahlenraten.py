# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = zahlenraten.py
# __version__   = v_1.0

# 2Do:
# - Ergebnisse speichern

# Import Module
import random
from colorama import init, Fore

# Startwerte Variablen
init(autoreset=True)        # Farbe automatisch zurücksetzen
wdh = 1                     #
repeat = 1                  # erneute Runde
secret = 0                  # gesuchte Zahl
guess = 0                   # Spielereingabe
i = 0                       # Zähler Versuche

# Funktionen
def seperator():
    print("****************************************")

def clear_line():
    print()


# Programmstart
while wdh == 1:
    while repeat == 1:
        secret = random.randint(999, 10000)
        list = []
        seperator()
        print("Zahlenraten")
        print("Errate die geheime Zahl!")
        print("Drücke die '" + Fore.MAGENTA + "0" + Fore.RESET + "' um das Spiel abzubrechen.")
        seperator()

        # Eingabe
        while guess != secret:
            try:
                guess = int(input("Gib eine Zahl ein: "))
            except:
                print("Es sind " + Fore.RED + "nur Zahlen" + Fore.RESET + " erlaubt!")
                clear_line()
                continue

            # Zähler Versuche
            i = i + 1

            # Eintrag in Liste oder Ende
            if guess == 0:
                repeat = int(0)
                clear_line()
                print("Die Runde wird abgebrochen!")
                break
            else:
                if list.count(guess) == 1:
                    print(Fore.RED + "Diese Zahl hattest du bereits.")
                    clear_line()
                    continue
                else:
                    list.append(guess)

                    # Auswertung Eingabe
                    if guess < 1000 or guess > 9999:
                        print("Die gesuchte Zahl ist", Fore.LIGHTRED_EX + "4-stellig.")
                        clear_line()
                    elif guess > secret:
                        if guess < secret + 10:
                            print(
                                Fore.LIGHTYELLOW_EX + "Nah dran" + Fore.RESET + " , aber die gesuchte Zahl ist " + Fore.LIGHTYELLOW_EX + "kleiner!")
                            clear_line()
                        else:
                            print("Die gesuchte Zahl ist " + Fore.LIGHTYELLOW_EX + " kleiner.")
                            clear_line()
                    elif guess < secret:
                        if guess > secret - 10:
                            print(
                                Fore.LIGHTCYAN_EX + "Nah dran" + Fore.RESET + ", aber die gesuchte Zahl ist " + Fore.LIGHTCYAN_EX + "größer!")
                            clear_line()
                        else:
                            print("Die gesuchte Zahl ist " + Fore.LIGHTCYAN_EX + " größer.")
                            clear_line()

        # Zahl erraten
        else:
            clear_line()
            print("Super! Die gesuchte Zahl ist:", Fore.GREEN + str(secret))
            print("Du hast die Zahl nach " + Fore.GREEN + str(i) + Fore.RESET + " Versuch(en) erraten.")
            seperator()
            name = str(input("Gib deinen Namen ein: "))
            repeat = 0

    # Wiederholung
    else:
        seperator()
        clear_line()
        print("Möchtest du noch einmal spielen?")
        print("Ja = 1   Nein = 0")
        try:
            repeat = int(input("Auswahl:"))

            # Wiederholung und Werte zurücksetzen
            if repeat == 1:
                i = 0
                clear_line()
                continue

            # Ende
            else:
                repeat = 0
                clear_line()
                print("Das Spiel wird beendet!")
                seperator()
                clear_line()
                break
        except:
            clear_line()
            print(Fore.RED + "*** Ungültig Eingabe ***")
            clear_line()
            repeat = 0