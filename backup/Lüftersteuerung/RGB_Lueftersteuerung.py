# Lüftersteuerung
# Version 0.4
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time


def GPIO_start():  # GPIO Startwerte
    GPIO.setmode(GPIO.BCM)  # Auswahl Pinbelegung
    GPIO.setwarnings(False)  # Warnungen Pinbelegung/-zustand
    GPIO.setup(23, GPIO.OUT)  # LED rot
    GPIO.setup(24, GPIO.OUT)  # LED grün
    GPIO.setup(25, GPIO.OUT)  # LED blau
    GPIO.setup(17, GPIO.OUT)  # Lüfter 1
    GPIO.setup(4, GPIO.OUT)  # Lüfter 2

    GPIO.output(23, GPIO.LOW)  # GPIO auf 0 setzen
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)


class LED:  # Module LED Zustand
    def green():  # LED grün
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)

    def yellow():  # LED gelb
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)

    def red():  # LED rot
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)


class fan:  # Module Lüfter
    def off():  # Lüfter aus
        GPIO.output(17, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)

    def one():  # Nur Lüfter 1 an
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)

    def two():  # Lüfter 1 + 2 an
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)


GPIO_start()  # GPIO auf Startwerte setzen

# Konfiguration
fantime = -1  # Lüfter 1 Startwert aus (-1)
fantime2 = -1  # Lüfter 2 Startwert aus (-1)

sec_short = 5  # Intervall zwischen Messungen in Sekunden
sec = sec_short  # Variable Intervall
sec_long = sec * 3  # Intervallzeit verlängern
timer = 60  # Nachlaufzeit Lüfter wenn rote LED aus (Sek.)
fan_on = int(timer / sec_short)  # Berechnung für Lüfternachlaufzeit

normal = 50  # Temperatur normal
warm = 58  # Temperatur warm
hot = 65  # Temperatur heiß

while 1:  # Schleife zur dauernden Abfrage starten

    tempData = "/sys/class/thermal/thermal_zone0/temp"
    readData = open(tempData, "r")  # Datei öffnen
    temperature = readData.readline(2)  # Temperatur auslesen
    readData.close()  # Datei schließen
    print("CPU " + temperature + "°C (" + str(sec) + ")")  # Ausgabe Temperatur
    temperature = int(temperature)  # Temperatur als Zahl

    # Zustandsabfrage LED + Lüfter
    if fantime2 == -1:  # wenn Lüfter 2 aus
        if temperature < warm:
            LED.green()
            if fantime != -1:  # Wenn Lüfter 1 an
                fan.one()  # Lüfter 1 an
                fantime -= 1  # Lüfter 1 Intervalle -1
            else:
                fan.off()  # Lüfter aus
                fantime = -1  # Lüfter 1 Laufzeit auf 0
                sec = sec_long  # Intervallzeit verlängern
        elif temperature >= warm and temperature < hot:
            LED.yellow()
            fan.one()  # ein Lüfter an
            fantime = fan_on  # Lüfter 1 Laufzeit
            sec = sec_short  # Intervallzeit verlkürzen
        elif temperature >= hot:
            LED.red()
            fan.two()  # beide Lüfter an
            fantime = fan_on  # Lüfter 1 Laufzeit
            fantime2 = fan_on  # Lüfter 2 Laufzeit
            sec = sec_short  # Intervallzeit verlkürzen
    elif fantime2 != -1:  # wenn Lüfter 2 an
        fantime -= 1  # Lüfter 1 Intervalle -1
        fantime2 -= 1  # Lüfter 2 Intervalle -1
        if temperature < warm:
            LED.green()
        elif temperature >= warm and temperature < hot:
            LED.yellow()
        elif temperature >= hot:
            fantime = fan_on  # Lüfter 1 Laufzeit
            fantime2 = fan_on  # Lüfter 2 Laufzeit

    # Ausgabe Lüfternachlauf
    if fantime2 != -1:  # wenn Lüfter 2 nicht -1
        print("Fan 1", fantime * sec, "Sek." + "(", sec, ")")  # Zeit Lüfter 1
        print("Fan 2", fantime2 * sec, "Sek." + "(", sec, ")")  # Zeit Lüfter 2
    elif fantime != -1:  # wenn Lüfter 1 nicht -1
        print("Fan 1", fantime * sec, "Sek." + "(", sec, ")")  # Zeit Lüfter 1

    time.sleep(sec)  # Intervall Abstand

GPIO.cleanup()  # GPIO zurücksetzen
