import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup(dac, GPIO.OUT)


for i in range (8):
    GPIO.output(dac[i], number[i]) 

GPIO.cleanup()

try:
    while True:
        for value in range(256):
            signal = bin2gpio(value)
            time.sleep(0.001)
            volt = ads (value)
            compval = GPIO.input(comp)
            if compval == 0:
                print ("ADS value = {:^3} -> {}, input voltage = {:.2f}" .format(value, signal, volt))
                break


except KeyboardInterrupt:
    print ('\n INPUT ERROR')

finally:
    GPIO.output(dac)
    GPIO.cleanup(dac)