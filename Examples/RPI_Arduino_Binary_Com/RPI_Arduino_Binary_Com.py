# Demo binary communication between Raspberry Pi and Arduino
# 4 bit Raspberry --> Arduino
# 4 bit Arduino --> Raspberry

# General Cycle
# 1.    [Raspberry] Enable GPIO 26                              [Arduino] Start test signal
# 2.    [Raspberry] Read IN bits                                [Arduino] Write OUT bits
# 3.    [Raspberry] Write OUT bits                              [Arduino] Read IN bits
# 4.    [Raspberry] Print IN bits                               [Arduino] Serial print IN bits

# WIRING

# [RPI Level Shifter Hat]         [Arduino]
# [GPIO; 5V Side]                 [Pin Nr]
# 26             -->              4     ENABLE
# 0              -->              14
# 1              -->              15
# 2              -->              32
# 3              -->              34

# 4              <--              36
# 5              <--              12
# 6              <--              10
# 7              <--              17

import time
import RPi.GPIO as GPIO

TEST_DURATION = 1  # Signal High duration

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("Initialising")
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

GPIO.setup(4, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(7, GPIO.IN)

outPin0 = True
outPin1 = True
outPin2 = False
outPin3 = False

print("=== Starting test batch ====")

while True:

    # Run 10 cycles before resetting
    for _ in range(10):

        # STEP 1
        # Enable RPI Logic Level Shifter (GPIO 26)
        GPIO.setup(26, GPIO.OUT)
        GPIO.output(26, True)

        time.sleep(0.1)

        # STEP 2
        # Read IN bits
        print("\nReading IN pins\n")

        print("Reading GPIO Pin 4: {}".format(GPIO.input(4)))
        print("Reading GPIO Pin 5: {}".format(GPIO.input(5)))
        print("Reading GPIO Pin 6: {}".format(GPIO.input(6)))
        print("Reading GPIO Pin 7: {}".format(GPIO.input(7)))

        # STEP 3
        # Write OUT bits

        print("\nWriting OUT pins\n")
        print("PIN0: {}\nPIN1: {}\nPIN2: {}\nPIN3: {}\n".format(outPin0, outPin1, outPin2, outPin3))

        GPIO.output(0, outPin0)
        GPIO.output(1, outPin1)
        GPIO.output(2, outPin2)
        GPIO.output(3, outPin3)

        # invert OUT bits for next cycle
        outPin0 = not outPin0
        outPin1 = not outPin1
        outPin2 = not outPin2
        outPin3 = not outPin3

        print("---- Cycle complete ----")

        time.sleep(TEST_DURATION)

    print("\n ==== Batch complete ====\n")
    GPIO.output(26, False)
    time.sleep(TEST_DURATION)
