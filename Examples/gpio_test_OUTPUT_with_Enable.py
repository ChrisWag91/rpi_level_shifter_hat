import RPi.GPIO as GPIO
import time

gpio_start = 1
gpio_end = 27

GPIO.setmode(GPIO.BCM)

for x in range(gpio_start, gpio_end):
    GPIO.setup(x, GPIO.OUT)

# Enable rpi level shifter hat
GPIO.output(26, True)

while True:

    for y in range(gpio_start, gpio_end):
        GPIO.output(y, True)
        print('on ', y)
    time.sleep(1)

    for z in range(gpio_start, gpio_end):
        if z != 26:
            GPIO.output(z, False)
            print('off ', z)
    time.sleep(1)
