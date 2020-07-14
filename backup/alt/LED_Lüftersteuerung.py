# Lüftersteuerung
# Version 0.1
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
# import RPi.GPIO as GPIO
import time
from RPi import GPIO

# GPIO Startwerte setzen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

# Schleife
while 1:

    # Temperatur abfragen und ausgeben
    tempData = "/sys/class/thermal/thermal_zone0/temp"
    dateilesen = open(tempData, "r")
    temperatur = dateilesen.readline(2)
    dateilesen.close()
    print("Deine CPU hat " + temperatur + " Grad")

    # Temperaturen festlegen und zu Integer umwandeln
    normal = 59
    warm = 63
    heiss = 68

    temperatur = int(temperatur)

    # Zustandsabfrage
    if temperatur <= normal:
        # print("Grüne LED")
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)

        # time.sleep(10)
    elif temperatur > normal and temperatur <= heiss:
        # print("Grüne + gelbe LED")
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)

        # time.sleep(10)
    elif temperatur >= heiss:
        # print("Rote LED + Lüfter")
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)

    time.sleep(3)
GPIO.cleanup()
