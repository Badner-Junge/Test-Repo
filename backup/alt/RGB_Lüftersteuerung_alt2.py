# Lüftersteuerung
# Version 0.3
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time


def GPIO_start():               # GPIO Startwerte
    GPIO.setmode(GPIO.BCM)      # Auswahl Pinbelegung
    GPIO.setwarnings(False)     # Warnungen Pinbelegung/-zustand
    GPIO.setup(23, GPIO.OUT)    # LED rot
    GPIO.setup(24, GPIO.OUT)    # LED grün
    GPIO.setup(25, GPIO.OUT)    # LED blau
    GPIO.setup(17, GPIO.OUT)    # Lüfter 1
    GPIO.setup(4, GPIO.OUT)     # Lüfter 2

    GPIO.output(23, GPIO.LOW)   # GPIO auf 0 setzen
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)


class LED:                      # Module LED Zustand

    def green():                # LED grün
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)

    def yellow():               # LED gelb
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)

    def red():                  # LED rot
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)


class fan:                      # Module Lüfter

    def off():                  # Lüfter aus
        GPIO.output(17, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)

    def one():                  # Nur Lüfter 1 an
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)

    def two():                  # Lüfter 1 + 2 an
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)

    def fan1_runon():
        if fantime != -1 and fantime != 0:
            fan.one()
            fantime -= 1
        else:
            fan.off()
            fantime = -1


GPIO_start()                    # GPIO auf Startwerte setzen

# Variablen
fantime = -1                        # Lüfter 1 Startwert aus (-1)
fantime2 = -1                       # Lüfter 2 Startwert aus (-1)

sec = 5                         # Intervall zwischen Messungen in Sekunden
timer = 30                      # Nachlaufzeit Lüfter wenn rote LED aus (Sek.)
fan_on = int(timer/sec)         # Berechnung für Lüfternachlaufzeit

normal = 49                     # Temperatur normal
warm = 51                       # Temperatur warm
hot = 53                        # Temperatur heiß

while 1:                        # Schleife zur dauernden Abfrage starten

    tempData = "/sys/class/thermal/thermal_zone0/temp"
    readData = open(tempData, "r")              # Datei öffnen
    temperature = readData.readline(2)          # Temperatur auslesen
    readData.close()                            # Datei schließen
    print("CPU hat " + temperature + " °C")     # Ausgabe Temperatur
    temperature = int(temperature)              # Temperatur als Zahl

    # Zustandsabfrage LED + Lüfter
    if fantime2 == -1:                          # wenn Lüfter 2 aus
        if temperature <= normal:
            LED.green()
            if fantime != -1 and fan != 0:      # wenn Lüfter 1 an
                fan.one()                       # Nur Lüfter 1 an
                fantime -= 1                    # Lüfter 1 Zähler -1
            else:                               # wenn Lüfter 1 aus
                fan.off()                       # beide Lüfter aus
                fantime = -1                    # Lüfter 1 Zähler zurücksetzen
        elif temperature > normal and temperature < hot:
            LED.yellow()
            fan.one()                           # Nur Lüfter 1 an
            fantime = fan_on                    # Nachlaufintervalle Lüfter 1
        elif temperature >= hot:
            LED.red()
            fan.two()                           # beide Lüfter an
            fantime2 = 0                        # Lüfter 2 Zähler auf 0
            fantime = 0                         # Lüfter 1 Zähler auf 0
    elif fantime2 != -1:                        # wenn Lüfter 2 an
        fantime += 1                            # Lüfter 1 Zähler +1
        fantime2 += 1                           # Lüfter 2 Zähler +1
        if temperature <= normal:
            LED.green()
        elif temperature > normal and temperature < hot:
            LED.yellow()
        elif temperature >= hot:
            fantime = 0                         # Lüfter 2 Zähler auf 0
            fantime2 = 0                        # Lüfter Zähler gleichsetzen

    # Ausgabe Lüfternachlauf
    if fantime2 != -1:                          # wenn Lüfter 2 Zähler nicht -1
        print("Fan 1", fantime * sec, "Sek.")   # Ausgabe Lüfter 1 Zähler
        print("Fan 2", fantime2 * sec, "Sek.")  # Ausgabe Lüfter 2 Zähler
    elif fantime != -1:                         # wenn Lüfter 1 Zähler nicht -1
        print("Fan 1", fantime * sec, "Sek.")   # Ausgabe Lüfter 1 Zähler

    time.sleep(sec)                             # Intervall Abstand

GPIO.cleanup()                                  # GPIO zurücksetzen
