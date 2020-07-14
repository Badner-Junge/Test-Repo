# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = menu.py
# __version__   = v_0.1

# Import Module
import random
from colorama import init, Fore
init(autoreset=True)                           # Farbe automatisch zurücksetzen


# Funktionen
def seperator():
    # Trennlinie
    print("****************************************")


def clear_line():
    # Leerzeile
    print()


def choice_game():
    # Auswahl Spiel
    try:
        choice = int(input("Auswahl: "))
        clear_line()
        while choice != 0:
            # Zahlenraten
            if choice == 1:
                games.zahlenraten()
                break

            # Hangman
            elif choice == 2:
                games.hangman()
                break

            # Tic Tac Toe
            elif choice == 3:
                games.tic_tac_toe()
                break

            # rock, paper, scissor
            elif choice == 4:
                games.rock_paper_scissor()
                break

            # Bestenliste
            elif choice == 9:
                games.scoreboard()
                break

            else:
                main_menu()

        else:
            print(Fore.CYAN + "-----------------------------------------")
            choice = 9999
            print(Fore.LIGHTCYAN_EX + "*** Schade! Bis zum nächsten Mal! ***")
            print(Fore.CYAN + "-----------------------------------------")

    except:
        if choice == 0:
            pass
        else:
            clear_line()
            print(Fore.RED + "Ungültige Eingabe!!!")
            choice = 9999
            clear_line()
            main_menu()


def main_menu():
    # Hauptmenü
    print(Fore.MAGENTA + "----------------------------------------")
    print(Fore.LIGHTMAGENTA_EX + "************ Spielesammlung ************")
    print(Fore.MAGENTA + "----------------------------------------")
    print("Wähle ein Spiel:")
    clear_line()
    print("1: Zahlenraten")
    print("2: Galgenmännchen")
    print("3: Tic Tac Toe")
    print("4: Schere, Stein, Papier")
    print("9: Bestenliste")
    print("0: Beenden")
    clear_line()

    #Auswahl Spiel
    choice_game()
    clear_line()

# Klassen
class games:

    def zahlenraten():
        # Startwerte Variablen
        wdh = 1                                     #
        repeat = 1                                  # erneute Runde
        secret = 0                                  # gesuchte Zahl
        guess = 0                                   # Spielereingabe
        i = 0                                       # Zähler Versuche

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
                        print( "Es sind " + Fore.RED + "nur Zahlen" + Fore.RESET + " erlaubt!")
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

        # Hauptmenü
        main_menu()

    def hangman():
        # Startwerte Variablen
        random.seed()                               # Random initialisieren
        wdh = 1                                     #
        repeat = 1                                  # erneute Runde
        tries = 10                                  # Versuche
        hangman = 0                                 # Hangman Bilderauswahl
        letter = 1                                  # Spielereingabe Buchstabe
        choice_word = []                            # ausgewähltes Wort
        code = []                                   # codiertes Wort
        hint = 2                                    # Hinweis

        # Hangman image_choice
        hangman_pics = ['''







                   ''', '''






          =========''', '''

               |
               |
               |
               |
               |
          =========''', '''

           +---+
               |
               |
               |
               |
               |
          =========''', '''

           +---+
           |   |
               |
               |
               |
               |
          =========''', '''

            +---+
            |   |
            O   |
                |
                |
                |
          =========''', '''

            +---+
            |   |
            O   |
            |   |
                |
                |
          =========''', '''

            +---+
            |   |
            O   |
           /|   |
                |
                |
          =========''', '''

            +---+
            |   |
            O   |
           /|\  |
                |
                |
          =========''', '''

            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
          =========''', '''

            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
          =========''']

        # Programmstart
        while wdh == 1:
            while repeat == 1:
                while tries != 1 and repeat == 1:

                    # Liste Zufallswort, erlaubte & schon verwendete Buchstaben
                    wordlist = ["hallo", "baum", "haus", "spielplatz", "garten", "wolke", "schere",  # gesuchte Worte
                                "badezimmer", "kastanie", "laugenbrezel"]
                    letter_allow = "abcdefghijklmnopqrstuvwxyz0"  # erlaubte Zeichen
                    letter_used = []  # geratene Buchstaben

                    # Auswahl und Codierung Zufallswort
                    ran_word = random.choice(wordlist)
                    choice_word.extend(ran_word)

                    # Erzeugung Zufallswort
                    len_ran_word = len(ran_word)
                    seperator()
                    print("Galgenmännchen")
                    print("Errate das gesuchte Wort!")
                    print("Drücke die '" + Fore.MAGENTA + "0" + Fore.RESET + "' um das Spiel abzubrechen.")
                    # print(choice_word)
                    seperator()
                    clear_line()

                    # Wort in Code umwandeln und verschlüsselte Ausgabe
                    code.extend("-" * int(len_ran_word))

                    # Zähler Versuche
                    if letter != 0:
                        while tries != 0 and "-" in code:
                            print(hangman_pics[hangman])
                            clear_line()
                            print(code)
                            if tries >= 6:
                                print("Du hast noch " + Fore.GREEN + str(tries) + Fore.RESET + " Versuche")
                            elif tries in (3, 4, 5):
                                print("Du hast noch " + Fore.YELLOW + str(tries) + Fore.RESET + " Versuche")
                            else:
                                print("Du hast noch " + Fore.RED + str(tries) + Fore.RESET + " Versuche")

                            # Eingabe Buchstabe
                            try:
                                letter = input("Gib einen Buchstaben ein: ")
                                letter = letter.upper().lower()
                            except:
                                continue

                            # Eingabe auswerten
                            if letter == "0":
                                repeat = int(0)
                                clear_line()
                                print("Die Runde wird abgebrochen!")
                                break

                            # Bereits verwendet (einmalig, nach Wiederholung von Buchstaben)
                            elif letter == "1" and hint == 1:
                                clear_line()
                                seperator()
                                print("Diese Buchstaben hast du bereits versucht:")
                                print(Fore.RED + str(sorted(letter_used)))
                                seperator()
                                clear_line()
                                hint -= 1
                                continue

                            else:
                                # Prüfen, ob Eingabe erlaubt
                                if letter_allow.find(letter.lower()) != -1:

                                    # Prüfung, ob Wiederholung und bereits verwendet
                                    if letter in letter_used:
                                        if hint == 2:
                                            print(Fore.RED + "Diesen Buchstaben hattest du bereits!")
                                            clear_line()
                                            seperator()
                                            print(
                                                "Drücke die '" + Fore.MAGENTA + "1" + Fore.RESET + "' , um bereits verwendete Buchstaben einmalig zu sehen.")
                                            seperator()
                                            hint -= 1
                                        else:
                                            print(Fore.RED + "Diesen Buchstaben hattest du bereits!")
                                        tries -= 1
                                        hangman = hangman + 1
                                        clear_line()
                                        continue

                                    # Prüfung, ob Vorhanden
                                    elif letter not in ran_word:
                                        letter_used.append(letter)
                                        print(
                                            "Der Buchstabe " + Fore.RED + "kommt nicht" + Fore.RESET + " im gesuchten Wort" + Fore.RED + " vor!")
                                        tries -= 1
                                        hangman = hangman + 1
                                        clear_line()
                                        continue

                                    # Ersetzen erratener Buchstaben
                                    else:
                                        letter_used.append(letter)
                                        count_letter = list(i for i in range(len(ran_word)) if ran_word[i] == letter)
                                        for n in count_letter:
                                            code[n] = letter
                                        clear_line()

                                # Unerlaubte Eingabe
                                else:
                                    print("Es sind nur " + Fore.RED + "einzelne Buchstaben" + Fore.RESET +  " erlaubt!")
                                    tries -= 1
                                    hangman = hangman + 1
                                    clear_line()
                                    continue

                        # Ausgabe, wenn keine Versuche mehr oder gelöst
                        else:
                            if "-" not in code:
                                print("Super, du hast das Wort '" + Fore.GREEN + ran_word + Fore.RESET + "' erraten!")
                                repeat = "0"
                                break
                            else:
                                print(hangman_pics[hangman])
                                clear_line()
                                print("Du hast leider keine Versuche mehr!")
                                print("Das gesuchte Wort war: '" + Fore.RED + ran_word + "'")
                                repeat = "0"
                                break

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
                        tries = 10
                        choice_word = []
                        code = []
                        hangman = 0
                        hint = 2
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
                    print("*** Ungültig Eingabe ***")
                    clear_line()
                    repeat = 0

        # Hauptmenü
        main_menu()

    def tic_tac_toe():
        print("Noch in Arbeit")
        main_menu()

    def rock_paper_scissor():                       # Fehlerhaft
        # Startwerte Variablen
        init(autoreset=True)                        # Farbe automatisch zurücksetzen
        random.seed()                               # Random initialisieren
        wdh = 1                                     #
        repeat = 1                                  # erneute Runde
        selection = ["Schere", "Stein", "Papier"]   # Liste Gesten
        choice_mode = 9999                          # Auswahl Modus
        mode = [5, 10, ""]                          # Rundenanzahl
        i = 1                                       # Rundenzähler
        selection_player = 9999                     # Auswahl Geste Spieler
        selection_computer = 0                      # Auswahl Geste Computer
        win = 0                                     # Siege Spieler
        loose = 0                                   # Niederlagen Spieler

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
                        seperator()
                        clear_line()
                        main_menu()
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
                                    clear_line()
                                    print("Die Runde wird abgebrochen!")
                                    break
                            except:
                                clear_line()
                                print(Fore.RED + "Ungültige Auswahl!")
                                continue

                        # Runde end
                        if selection_player == 0:
                            break

                        # Rundenzähler erhöhen, wenn Eingabe gültig
                        i = i + 1

                        # Ausgabe Spielergeste
                        clear_line()
                        print("Du hast '", selection[selection_player - 1], "' gewählt.")

                        # Ausgabe Computergeste
                        selection_computer = random.randint(1, 3)
                        print("Dein Gegner hat'", selection[selection_computer - 1], "' gewählt.")
                        clear_line()

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
                                    clear_line()
                                    print("Die Runde wird abgebrochen.")
                                    break
                            except:
                                clear_line()
                                print(Fore.RED + "Ungültige Auswahl!")

                        # Runde abbrechen
                        if selection_player == 0:
                            break

                        else:
                            # Rundenzähler erhöhen, wenn Eingabe gültig
                            i = i + 1

                            # Ausgabe Spielergeste
                            clear_line()
                            print("Du hast '", selection[selection_player - 1], "' gewählt.")

                            # Ausgabe Computergeste
                            selection_computer = random.randint(1, 3)
                            print("Dein Gegner hat'", selection[selection_computer - 1], "' gewählt.")
                            clear_line()

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
                    seperator()
                    print("Super, du hast " + Fore.GREEN + str(win) + Fore.RESET + " zu " + Fore.RED + str(loose) + Fore.RESET + " gewonnen!")
                elif loose > win:
                    seperator()
                    print("Schade, du hast " + Fore.GREEN + str(win) + Fore.RESET + " zu " + Fore.RED + str(loose) + Fore.RESET + " verloren!")
                elif win == loose and selection_player == 0:
                    pass

                # Enscheidungsrunde bei Unentschieden
                else:
                    clear_line()
                    print("Es steht unentschieden.")
                    # print("Du: ", win, "Gegner: ", loose)
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
                            clear_line()
                            print(Fore.RED + "Ungültige Auswahl!")

                        # Ausgabe Spielergeste
                        clear_line()
                        print("Du hast '", selection[selection_player - 1], "' gewählt.")

                        # Ausgabe Computergeste
                        selection_computer = random.randint(1, 3)
                        print("Dein Gegner hat'", selection[selection_computer - 1], "' gewählt.")
                        clear_line()

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
                        seperator()
                        print("Super, du hast " + Fore.GREEN + str(win) + \
                            Fore.RESET + " zu " + Fore.RED + str(loose) + \
                                Fore.RESET + " gewonnen!")
                    elif loose > win:
                        seperator()
                        print("Schade, du hast " + Fore.GREEN + str(win) + \
                            Fore.RESET + " zu " + Fore.RED + str(loose) + \
                                Fore.RESET + " verloren!")

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
                        # repeat = 0
                        choice_mode = 0
                        selection_player = 9999
                        clear_line()
                        print("Das Spiel wird beendet!")
                        seperator()
                        clear_line()

                except:
                    clear_line()
                    print(Fore.RED + "*** Ungültig Eingabe ***")
                    clear_line()
                    repeat = 0

            # Hauptmenü
            main_menu()

    def scoreboard():
        print("Noch in Arbeit")
        main_menu()


main_menu()
