import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 0)
GPIO.output(17, GPIO.LOW)
# GPIO.cleanup()
