import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21

GPIO.setup(led, GPIO.OUT)

def LedOn(val)
    GPIO.output(led,1)
    time.sleep(val)
    GPIO.output(led,0)
