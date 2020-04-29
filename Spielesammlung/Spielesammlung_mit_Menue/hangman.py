# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = hangman.py
# __version__   = v_1.0

# 2Do:
# - Merkmale farblich hervorheben
# - Wörter hinzufügen, löschen oder anzeigen

# Import Module
import random
from colorama import init, Fore

# Startwerte Variablen
init(autoreset=True)                            # Farbe automatisch zurücksetzen
random.seed()                                   # Random initialisieren
wdh = 1                                         #
repeat = 1                                      # erneute Runde
tries = 10                                      # Versuche
hangman = 0                                     # Hangman Bilderauswahl
letter = 1                                      # Spielereingabe Buchstabe
choice_word = []                                # ausgewähltes Wort
code = []                                       # codiertes Wort
hint = 2                                        # Hinweis

# Funktionen
def seperator():
    print("****************************************")

def clear_line():
    print()

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
            wordlist = ["hallo", "baum", "haus", "spielplatz", "garten", "wolke", "schere",     # gesuchte Worte
                        "badezimmer", "kastanie", "laugenbrezel"]
            letter_allow = "abcdefghijklmnopqrstuvwxyz0"                                        # erlaubte Zeichen
            letter_used = []                                                                    # geratene Buchstaben

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
                    elif tries in (3,4,5):
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
                                    print("Drücke die '" + Fore.MAGENTA + "1" + Fore.RESET + "' , um bereits verwendete Buchstaben einmalig zu sehen.")
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
                                print("Der Buchstabe " + Fore.RED + "kommt nicht" + Fore.RESET + " im gesuchten Wort" + Fore.RED + " vor!")
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
                            print("Es sind nur einzelne Buchstaben erlaubt!")
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
                break
        except:
            clear_line()
            print("*** Ungültig Eingabe ***")
            repeat = 0