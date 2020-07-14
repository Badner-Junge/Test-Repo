# Lüftersteuerung
# Version 0.4
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time
import sys

# Pinbelegung
LED_RED_PIN = 23        # rote LED
LED_GREEN_PIN = 24      # grüne LED
LED_BLUE_PIN = 25       # blaue LED
FAN_1_PIN = 17          # Lüfter 1
FAN_2_PIN = 4           # Lüfter 2

# Mindestgeschwindigkeit Lüfter
FAN_1_MIN = 20          # [%] Lüfter 1
FAN_2_MIN = 20          # [%] Lüfter 2

# Taktfrequenz und Intervallabstand
PWM_FREQ = 25           # [Hz]
WAIT_TIME = 1           # [s]

# Temperaturspanne und Lüftergeschwindigkeit Schritte
tempSteps = [50, 65]    # [°C]
speedSteps = [0, 100]   # [%]

# Die Lüfterdrehzahl ändert sich nur, wenn die Temperaturdifferenz höher ist
# als hyst
hyst = 1

i = 0
cpuTemp = 0
fanSpeed = 0
cpuTempOld = 0
fanSpeedOld = 0

# GPIO Startwerte
GPIO.setmode(GPIO.BCM)                         # Auswahl Pinbelegung
GPIO.setwarnings(False)                        # Warnungen Pinbelegung/-zustand
GPIO.setup(LED_RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_BLUE_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FAN_1_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FAN_2_PIN, GPIO.OUT, initial=GPIO.LOW)

fan_1 = GPIO.PWM(FAN_1_PIN, PWM_FREQ)
fan_2 = GPIO.PWM(FAN_2_PIN, PWM_FREQ)

fan_1.start(0)
fan_2.start(0)

# Variablen
fantime = -1                    # Lüfter 1 Startwert aus (-1)
fantime2 = -1                   # Lüfter 2 Startwert aus (-1)

sec_short = 5                   # Intervall zwischen Messungen in Sekunden
sec = WAIT_TIME                 # Variable Intervall
sec_long = sec * 3              # Intervallzeit verlängern
timer = 60                      # Nachlaufzeit Lüfter wenn rote LED aus (Sek.)
fan_on = int(timer/sec_short)   # Berechnung für Lüfternachlaufzeit

normal = 50                     # Temperatur normal
warm = 58                       # Temperatur warm
hot = 65                        # Temperatur heiß


class LED:                      # Module LED Zustand

    def green():                # LED grün
        GPIO.output(LED_RED_PIN, GPIO.LOW)
        GPIO.output(LED_GREEN_PIN, GPIO.HIGH)
        GPIO.output(LED_BLUE_PIN, GPIO.LOW)

    def yellow():               # LED gelb
        GPIO.output(LED_RED_PIN, GPIO.HIGH)
        GPIO.output(LED_GREEN_PIN, GPIO.HIGH)
        GPIO.output(LED_BLUE_PIN, GPIO.LOW)

    def red():                  # LED rot
        GPIO.output(LED_RED_PIN, GPIO.HIGH)
        GPIO.output(LED_GREEN_PIN, GPIO.LOW)
        GPIO.output(LED_BLUE_PIN, GPIO.LOW)


class cooling:                      # Module Lüfter

    def off():                  # Lüfter aus
        GPIO.output(FAN_1_PIN, GPIO.LOW)
        GPIO.output(FAN_2_PIN, GPIO.LOW)

    def one():                  # Nur Lüfter 1 an
        GPIO.output(FAN_1_PIN, GPIO.HIGH)
        GPIO.output(FAN_2_PIN, GPIO.LOW)

    def two():                  # Lüfter 1 + 2 an
        GPIO.output(FAN_1_PIN, GPIO.HIGH)
        GPIO.output(FAN_2_PIN, GPIO.HIGH)


# We must set a speed value for each temperature step
if len(speedSteps) != len(tempSteps):
    print("Numbers of temp steps and speed steps are different")
    exit(0)

try:
    while 1:
        # Temperatur auslesen
        tempData = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temperature = float(tempData.read()) / 1000
        tempData.close()
        print("CPU "+str(temperature)+"°C("+str(sec)+")")

        # Zustandsabfrage LED + Lüfter
        if fantime2 == -1:                            # wenn Lüfter 2 aus
            if temperature < warm:
                LED.green()
                if fantime != -1:                     # Wenn Lüfter 1 an
                    cooling.one()                         # Lüfter 1 an
                    fantime -= 1                      # Lüfter 1 Intervalle -1
                else:
                    cooling.off()                         # Lüfter aus
                    fantime = -1                      # Lüfter 1 Laufzeit auf 0
                    sec = sec_long                    # Intervallzeit länger
            elif temperature >= warm and temperature < hot:
                LED.yellow()
                cooling.one()                             # ein Lüfter an
                fantime = fan_on                      # Lüfter 1 Laufzeit
                sec = sec_short                       # Intervallzeit kürzer
            elif temperature >= hot:
                LED.red()
                cooling.two()                             # beide Lüfter an
                fantime = fan_on                      # Lüfter 1 Laufzeit
                fantime2 = fan_on                     # Lüfter 2 Laufzeit
                sec = sec_short                       # Intervallzeit kürzer
        elif fantime2 != -1:                          # wenn Lüfter 2 an
            fantime -= 1                              # Lüfter 1 Intervalle -1
            fantime2 -= 1                             # Lüfter 2 Intervalle -1
            if temperature < warm:
                LED.green()
            elif temperature >= warm and temperature < hot:
                LED.yellow()
            elif temperature >= hot:
                fantime = fan_on                      # Lüfter 1 Laufzeit
                fantime2 = fan_on                     # Lüfter 2 Laufzeit

        # Ausgabe Lüfternachlauf
        if fantime2 != -1:                            # wenn Lüfter 2 nicht -1
            print("Fan 1", fantime*sec, "Sek."+"(", sec, ")")   # Lüfter 1
            print("Fan 2", fantime2*sec, "Sek."+"(", sec, ")")  # Lüfter 2
        elif fantime != -1:                           # wenn Lüfter 1 nicht -1
            print("Fan 1", fantime*sec, "Sek."+"(", sec, ")")   # Lüfter 1

        time.sleep(WAIT_TIME)                         # Intervall

# Bei KeyboardInterrupt (ctrl + c) GPIO auf 0 setzen und Programmende
except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
