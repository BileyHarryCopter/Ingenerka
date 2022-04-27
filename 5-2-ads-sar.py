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
    value = 128
    des = 64
    for i in range(8):
        signal = bin2gpio(value)
        time.sleep(0.001)
        compval = GPIO.input(comp)
        if compval == 1:
            value = value + des
        else:
            value = value - des
        des = int (des / 2)
    signal = bin2gpio(value)
    volt = value / 256 * maxvolt
    print ("ADS value = {:^3} -> {}, input voltage = {:.2f}" .format(value, signal, volt))       

try:
    while True:
        ads()


except KeyboardInterrupt:
    print ('\n INPUT ERROR')
    GPIO.cleanup()

finally:
    GPIO.output(dac, non)
    GPIO.cleanup()
