import RPi.GPIO as GPIO
import time

comp = 4
troyka = 17
maxvolt = 3.3

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
non = [ 0,  0,  0, 0, 0,  0, 0,  0]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin (val):
    return bin(val)[2:].zfill(8)

def bin2gpio (val):
    bin = [int (elem) for elem in dec2bin(val)]
    GPIO.output(dac, bin)
    return bin

def ads():
    for value in range(256):
        signal = bin2gpio(value)
        time.sleep(0.0001)
        volt = value / 256 * maxvolt
        compval = GPIO.input(comp)
        if compval == 0:
            print ("ADS value = {:^3} -> {}, input voltage = {:.2f}" .format(value, signal, volt))
            return value

try:
    while True:
        ads ()


except KeyboardInterrupt:
    print ('\n INPUT ERROR')
    GPIO.cleanup()

finally:
    GPIO.output(dac)
    GPIO.cleanup()
