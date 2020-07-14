# Lüftersteuerung
# Version 0.2
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time

# Variablen
fan = -1                    # Lüfter Startwert aus (-1)
sec = 2                     # Intervall für Messungen in Sekunden
timer = 20                  # Nachlaufzeit Lüfter wenn rote LED aus in Sekunden
fan_on = int(timer/sec)     # Berechnung für Lüfternachlaufzeit

# Temperaturen
normal = 56
warm = 58
heiss = 60

# GPIO Startwerte setzen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)    # LED rot
GPIO.setup(24, GPIO.OUT)    # LED grün
GPIO.setup(25, GPIO.OUT)    # LED blau
GPIO.setup(17, GPIO.OUT)    # Lüfter 1
GPIO.setup(4, GPIO.OUT)     # Lüfter 2

# GPIO auf 0 setzen
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(4, GPIO.LOW)

# Programmstart
while 1:

    # Temperatur abfragen, umwandeln und ausgeben
    tempData = "/sys/class/thermal/thermal_zone0/temp"
    dateilesen = open(tempData, "r")
    temperatur = dateilesen.readline(2)
    dateilesen.close()
    print("Deine CPU hat " + temperatur + " Grad")
    temperatur = int(temperatur)

    # Zustandsabfrage für LED und Lüfter
    # Abfrage bei Lüfter aus
    if fan == -1:
        if temperatur <= normal:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(4, GPIO.LOW)
        elif temperatur > normal and temperatur < heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(4, GPIO.HIGH)
        elif temperatur >= heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            fan = 0
    # Abfrage bei Lüfter an
    else:
        fan += 1
        if temperatur <= normal:
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
        elif temperatur > normal and temperatur < heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
        elif temperatur >= heiss:
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            fan = 0

    # Lüfter nachlaufen lassen
    if fan > fan_on and GPIO.input(23) == GPIO.HIGH \
            and GPIO.input(24) == GPIO.HIGH:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        fan = -1

    # Ausgabe Lüfternachlauf
    if fan != -1:
        print(fan * sec, "Sek.")

    # Zeit zwischen erneuter Abfrage
    time.sleep(sec)

# GPIO Zustand zurücksetzen
GPIO.cleanup()
