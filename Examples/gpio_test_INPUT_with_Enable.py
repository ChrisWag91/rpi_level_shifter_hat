import RPi.GPIO as GPIO
import time

gpio_start = 1
gpio_end = 27

GPIO.setmode(GPIO.BCM)

for x in range(gpio_start, gpio_end):
    GPIO.setup(x, GPIO.IN)

# Enable rpi level shifter hat
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, True)

while True:

    for y in range(gpio_start, gpio_end):
        if y != 26:
            print('GPIO Pin {} status -> {}'.format(y, GPIO.input(y)))
    time.sleep(5)
