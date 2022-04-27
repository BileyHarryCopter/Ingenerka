import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin (val):
    return bin(val)[2:].zfill(8)

def bin2gpio (val):
    bin = [int (elem) for elem in dec2bin(val)]
    GPIO.output(dac, bin)

try:
    print ("Введите период работы пилы: ")
    per = int(input ())
    while (True):
        for i in range (0, 255):
            bin2gpio(i)
            time.sleep(per/255)

finally:
    for i in range (8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup()