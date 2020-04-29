# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = rock_paper_scissor.py
# __version__   = v_0.9

# 2Do:
# - Eingabe von Werten über 3 = ungültig
# - Merkmale farblich hervorheben

# Import Module
import random, time
from colorama import init, Fore

# Startwerte Variablen
init(autoreset=True)                            # Farbe automatisch zurücksetzen
random.seed()                                   # Random initialisieren
wdh = 1                                         #
repeat = 1                                      # erneute Runde
selection = ["Schere", "Stein", "Papier"]       # Liste Gesten
choice_mode = 9999                              # Auswahl Modus
mode = [5, 10, ""]                              # Rundenanzahl
i = 1                                           # Rundenzähler
selection_player = 9999                         # Auswahl Geste Spieler
selection_computer  = 0                         # Auswahl Geste Computer
win = 0                                         # Siege Spieler
loose = 0                                       # Niederlagen Spieler

# Funktionen
def seperator():
    print("****************************************")

def clear_line():
    print()

def player():
    clear_line()
    print("Du hast '", selection[selection_player - 1], "' gewählt.")

def computer():
    print("Dein Gegner hat'", selection[selection_computer - 1], "' gewählt.")
    clear_line()

# Programmstart
while wdh == 1:
    while repeat == 1 and choice_mode not in (0, 1, 2, 3):
        seperator()
        print("Schere, Stein, Papier")
        print("Schlage deinen Gegner")
        print("Drücke die '" + Fore.MAGENTA + "0" + Fore.RESET + "' um das Spiel abzubrechen.")
        seperator()

        # Modus oder Ende
        print("")
        print("1 = Best of 5")
        print("2 = Best of 10")
        print("3 = unbegrenzt")
        clear_line()
        try:
            choice_mode = int(input("Wähle einen Modus: "))
            seperator()
            if choice_mode == 1:
                clear_line()
                print(Fore.LIGHTMAGENTA_EX + "*** Best of 5 ***")
                clear_line()
            elif choice_mode == 2:
                clear_line()
                print(Fore.LIGHTYELLOW_EX + "*** Best of 10 ***")
                clear_line()
            elif choice_mode == 3:
                clear_line()
                print(Fore.LIGHTCYAN_EX + "*** unbegrenzt ***")
                clear_line()
            elif choice_mode == 0:
                repeat = 0
                clear_line()
                print("Das Spiel wird beendet!")
                break
            else:
                clear_line()
                print(Fore.RED + "Ungültige Auswahl!")
                clear_line()
                continue
        except:
            seperator()
            clear_line()
            print(Fore.RED + "Ungültige Auswahl!")
            clear_line()
            continue

    # Auswertung Modus
    else:
        # Ende
        if choice_mode == 0:
            break

        # Rundenangabe und Auswahl Geste * Modus: Best of 5/10
        print("Gewinne mehr Runden als dein Gegner!")
        if choice_mode < 3:
            for i in range(mode[choice_mode - 1]):
                while selection_player not in (1, 2, 3):
                    seperator()
                    print("Runde ", i + 1, " von ", mode[choice_mode - 1])
                    clear_line()
                    print("1 = Schere")
                    print("2 = Stein")
                    print("3 = Papier")
                    clear_line()
                    try:
                        selection_player = int(input("Auswahl: "))

                        # Runde end
                        if selection_player == 0:
                            print("Die Runde wird abgebrochen!")
                            break
                    except:
                        print(Fore.RED + "Ungültige Auswahl!")
                        continue

                # Runde end
                if selection_player == 0:
                    break

                # Rundenzähler erhöhen, wenn Eingabe gültig
                i = i + 1

                # Ausgabe Spielergeste
                player()

                # Ausgabe Computergeste
                selection_computer = random.randint(1, 3)
                computer()

                # Vergleich Gesten
                if selection_player == 1 and selection_computer == 3:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 1 and selection_computer == 2:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                elif selection_player == 2 and selection_computer == 1:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 2 and selection_computer == 3:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                elif selection_player == 3 and selection_computer == 2:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 3 and selection_computer == 1:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                else:
                    print("Ihr habt beide das Gleiche gewählt.")
                print("Du: " + Fore.GREEN + str(win) + Fore.RESET + "    Gegner: " + Fore.LIGHTRED_EX + str(
                    loose))

                # Zurücksetzen Spielergeste
                if selection_player != 0:
                    selection_player = 9999
                else:
                    selection_player = 0
                    break

        else:
            # Rundenangabe und Auswahl Geste * Modus: unbegrenzt
            while selection_player != 0:
                while selection_player not in (0, 1, 2, 3):
                    seperator()
                    print("Runde ", i)
                    clear_line()
                    print("1 = Schere")
                    print("2 = Stein")
                    print("3 = Papier")
                    clear_line()
                    try:
                        selection_player = int(input("Auswahl: "))

                        # Runde abbrechen
                        if selection_player == 0:
                            print("Die Runde wird abgebrochen.")
                            break
                    except:
                        print("Ungültige Auswahl!")

                # Runde abbrechen
                if selection_player == 0:
                    break

                else:
                    # Rundenzähler erhöhen, wenn Eingabe gültig
                    i = i + 1

                    # Ausgabe Spielergeste
                    player()

                    # Ausgabe Computergeste
                    selection_computer = random.randint(1, 3)
                    computer()

                    # Vergleich Gesten
                    if selection_player == 1 and selection_computer == 3:
                        win += 1
                        print("Ein Punkt für dich!")
                    elif selection_player == 1 and selection_computer == 2:
                        loose += 1
                        print("Leider ein Punkt für deinen Gegner.")
                    elif selection_player == 2 and selection_computer == 1:
                        win += 1
                        print("Ein Punkt für dich!")
                    elif selection_player == 2 and selection_computer == 3:
                        loose += 1
                        print("Leider ein Punkt für deinen Gegner.")
                    elif selection_player == 3 and selection_computer == 2:
                        win += 1
                        print("Ein Punkt für dich!")
                    elif selection_player == 3 and selection_computer == 1:
                        loose += 1
                        print("Leider ein Punkt für deinen Gegner.")
                    else:
                        print("Ihr habt beide das Gleiche gewählt.")
                    print("Du: " + Fore.GREEN + str(win) + Fore.RESET + "    Gegner: " + Fore.LIGHTRED_EX + str(
                        loose))

                    # Zurücksetzen Spielergeste
                    if selection_player != 0:
                        selection_player = 9999
                    else:
                        selection_player = 0
                        break

        # Ende
        if win > loose:
            clear_line()
            print("Super, du hast ", win, "zu", loose, "gewonnen!")
        elif loose > win:
            clear_line()
            print("Schade, du hast ", win, "zu", loose, "verloren")
        elif win == loose and selection_player == 0:
            pass

        # Enscheidungsrunde bei Unentschieden
        else:
            clear_line()
            print("Es steht unentschieden.")
            print("Du: ", win, "Gegner: ", loose)
            seperator()
            print("Hier kommt die letzte, alles entscheidende Runde:")
            clear_line()
            while win == loose:
                print("1 = Schere")
                print("2 = Stein")
                print("3 = Papier")
                clear_line()
                try:
                    selection_player = int(input("Auswahl: "))
                except:
                    print("Ungültige Auswahl!")

                # Ausgabe Spielergeste
                player()

                # Ausgabe Computergeste
                selection_computer = random.randint(1, 3)
                computer()

                # Vergleich Gesten
                if selection_player == 1 and selection_computer == 3:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 1 and selection_computer == 2:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                elif selection_player == 2 and selection_computer == 1:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 2 and selection_computer == 3:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                elif selection_player == 3 and selection_computer == 2:
                    win += 1
                    print("Ein Punkt für dich!")
                elif selection_player == 3 and selection_computer == 1:
                    loose += 1
                    print("Leider ein Punkt für deinen Gegner.")
                else:
                    print("Ihr habt beide das Gleiche gewählt.")
                    clear_line()

            # Ausgabe Ergebnis
            if win > loose:
                clear_line()
                print("Super, du hast ", win, "zu", loose, "gewonnen!")
            elif loose > win:
                clear_line()
                print("Schade, du hast ", win, "zu", loose, "verloren")

        # Wiederholung
        seperator()
        clear_line()
        print("Möchtest du noch einmal spielen?")
        print("Ja = 1   Nein = 0")
        try:
            repeat = int(input("Auswahl:"))

            # Wiederholung und Werte zurücksetzen
            if repeat == 1:
                choice_mode = 9999
                selection_player = 9999
                i = 1
                win = 0
                loose = 0
                clear_line()
                continue

            # Ende
            else:
                clear_line()
                print("Das Spiel wird beendet!")
                seperator()
                clear_line()
                break
        except:
            clear_line()
            print("*** Ungültig Eingabe ***")
            clear_line()
            repeat = 0