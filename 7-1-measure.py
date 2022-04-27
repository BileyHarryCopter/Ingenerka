import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

comp = 4
troyka = 17
maxvolt = 3.3

GPIO.setmode(GPIO.BCM)


dac  = [26, 19, 13, 6, 5, 11, 9, 10]
non  = [ 0,  0,  0, 0, 0,  0, 0,  0]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
data = [0]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

# measured_data = [10, 23, 45, 50, 62, 73, 90]
# plt.plot(measured_data)
# plt.show()

def dec2bin (val):
    return bin(val)[2:].zfill(8)

def bin2gpio (val):
    bin = [int (elem) for elem in dec2bin(val)]
    GPIO.output(dac, bin)
    return bin

def bin2leds (val):
    bits = 0
    state = [0, 0, 0, 0, 0, 0, 0, 0]
    bits = int (8 * val / 256)
    for i in range (bits):
        state[i] = 1
    GPIO.output(leds, state)

def adc():
    for value in range(256):
        signal = bin2gpio(value)
        time.sleep(0.001)
        volt = value / 256 * maxvolt
        compval = GPIO.input(comp)
        if compval == 0:
            # print ("ADC value = {:^3} -> {}, Voltage on C = {:.2f}" .format(value, signal, volt))
            return value

try:
    time_init = time.time()
    value = adc ()
    print ("Charhing of C is started from voltage: {:.4} V" .format(value / 256 * 3.3))
    while value < 240:
        value = adc ()
        bin2leds(value)
        data.append(value / 256 * 3.3)
        # print ("Data in the list: {:^3}" .format(value))

    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)

    print ("Recharhing of C is started from voltage: {:.4} V" .format(value / 256 * 3.3))
    while value > 5:
        value = adc ()
        bin2leds(value)
        data.append(value / 256 * 3.3)
        # print ("Data in the list: {:^3}" .format(value))
    print ("Voltage of C finally: {:.2} V" .format(value / 256 * 3.3))

    time = time.time()
    data_str = [str(item) for item in data]
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str))

    time = time - time_init
    print ("Time of the process: {:.3} c" .format(time))
    print ("Period of a measure: {:.3} c" .format(0.001))
    print ("Frequency of a measure: {:^3} КГц". format(1))
    print ("Step discretization: {:.3} В" .format(3.3 / 256))

    plt.plot(data)
    plt.show()

except KeyboardInterrupt:
    print ('\n INPUT ERROR')
    GPIO.cleanup()

finally:
    GPIO.output(dac, non)
    GPIO.cleanup()

