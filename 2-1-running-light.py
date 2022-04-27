import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)

j = 0
while j <= 3:
    i = 0
    while i <= 7: 
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)
        i += 1
    j += 1

    