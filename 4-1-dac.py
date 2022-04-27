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
    while True:
        print("\nВведите целое число от 0 до 255:")
        input_val = input()

        if (input_val == 'q'):
            break
        else:
            val = int(input_val)
            if val > 255:
                print ("Пожалуйста, введите число от 0 до 255")
                continue
            volt = 3.3 * val / 256
            print("Ваше число в двоичной системе счисления:", dec2bin(val))
            print("Предполагаемое напряжение:", volt, "В")
            bin2gpio(val)

except ValueError:
    print ("\nINPUT ERROR: Введен символ неправильного типа")

finally:
    for i in range (8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup()