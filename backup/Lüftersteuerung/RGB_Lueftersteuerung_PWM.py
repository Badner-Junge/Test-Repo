# !/usr/bin/python
# -*- coding: utf-8 -*-

# Lüftersteuerung PWM
# Version 0.2
# Geschrieben von: Fabian Riegeer

# Bibliotheken importieren
import RPi.GPIO as GPIO
import time
import sys

# Pinbelegung
LED_RED_PIN = 23  # rote LED
LED_GREEN_PIN = 24  # grüne LED
LED_BLUE_PIN = 25  # blaue LED
FAN_1_PIN = 17  # Lüfter 1
FAN_2_PIN = 4  # Lüfter 2

# Mindestgeschwindigkeit Lüfter
FAN_1_MIN = 30  # [%] Lüfter 1
FAN_2_MIN = 30  # [%] Lüfter 2

# Taktfrequenz und Intervallabstand
PWM_FREQ = 50  # [Hz]
WAIT_TIME = 1  # [s]

# Temperaturspanne und Lüftergeschwindigkeit Schritte
tempSteps = [50, 65]  # [°C]
speedSteps = [0, 100]  # [%]

# Die Lüfterdrehzahl ändert sich nur, wenn die Temperaturdifferenz höher ist
# als hyst
hyst = 1

i = 0
cpuTemp = 0
fanSpeed = 0
cpuTempOld = 0
fanSpeedOld = 0

# GPIO Startwerte
GPIO.setmode(GPIO.BCM)  # Auswahl Pinbelegung
GPIO.setwarnings(False)  # Warnungen Pinbelegung/-zustand
GPIO.setup(LED_RED_PIN, GPIO.OUT, initial=GPIO.LOW)  # LED rot
GPIO.setup(LED_GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)  # LED grün
GPIO.setup(LED_BLUE_PIN, GPIO.OUT, initial=GPIO.LOW)  # LED blau
GPIO.setup(FAN_1_PIN, GPIO.OUT, initial=GPIO.LOW)  # Lüfter 1
GPIO.setup(FAN_2_PIN, GPIO.OUT, initial=GPIO.LOW)  # Lüfter 2

LED_RED = GPIO.PWM(LED_RED_PIN, PWM_FREQ)
LED_GREEN = GPIO.PWM(LED_GREEN_PIN, PWM_FREQ)
LED_BLUE = GPIO.PWM(LED_BLUE_PIN, PWM_FREQ)

LED_RED.start(0)
LED_GREEN.start(0)
LED_BLUE.start(0)

fan_1 = GPIO.PWM(FAN_1_PIN, PWM_FREQ)
fan_2 = GPIO.PWM(FAN_2_PIN, PWM_FREQ)

fan_1.start(0)
fan_2.start(0)

# We must set a speed value for each temperature step
if len(speedSteps) != len(tempSteps):
    print("Numbers of temp steps and speed steps are different")
    exit(0)

try:
    while 1:
        # Temperatur auslesen
        cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
        cpuTemp = round(float(cpuTempFile.read()) / 1000, 1)
        cpuTempFile.close()
        print("CPU " + str(cpuTemp) + "°C")

        # LED Farbgebung
        LED_RED.ChangeDutyCycle(fanSpeed)
        LED_GREEN.ChangeDutyCycle(100 - fanSpeed)

        # Calculate desired fan speed
        if abs(cpuTemp - cpuTempOld) > hyst:
            # Below first value, fan will run at min speed.
            if cpuTemp < tempSteps[0]:
                fanSpeed = speedSteps[0]
            # Above last value, fan will run at max speed
            elif cpuTemp >= tempSteps[len(tempSteps) - 1]:
                fanSpeed = speedSteps[len(tempSteps) - 1]
            # If temperature is between 2 steps, fan speed is calculated by
            # linear interpolation
            else:
                for i in range(0, len(tempSteps) - 1):
                    if (cpuTemp >= tempSteps[i]) and (cpuTemp < tempSteps[i + 1]):
                        fanSpeed = round(
                            (speedSteps[i + 1] - speedSteps[i])
                            / (tempSteps[i + 1] - tempSteps[i])
                            * (cpuTemp - tempSteps[i])
                            + speedSteps[i],
                            1,
                        )

            if fanSpeed != fanSpeedOld:
                if fanSpeed != fanSpeedOld and (fanSpeed >= FAN_1_MIN or fanSpeed == 0):
                    fan_1.ChangeDutyCycle(fanSpeed)
                    fanSpeedOld = fanSpeed
                    fan_2.ChangeDutyCycle(fanSpeed)
                    fanSpeedOld = fanSpeed
            cpuTempOld = cpuTemp

        time.sleep(WAIT_TIME)  # Intervall

# Bei KeyboardInterrupt (ctrl + c) GPIO auf 0 setzen und Programmende
except KeyboardInterrupt:
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()
