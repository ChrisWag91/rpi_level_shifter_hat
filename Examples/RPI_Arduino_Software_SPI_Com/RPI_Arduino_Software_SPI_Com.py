#!/usr/bin/env python

# Demo SPI communication between Raspberry Pi and Arduino

# GENERAL FUNCTION
# This is a simple example to demonstrate Software-SPI communication between a Raspberry (Master) with the RPI Level Shifter Hat and Arduino Mega (Slave)

# WIRING
# [RPI Level Shifter Hat]         [Arduino]
# [GPIO; 5V Side]                 [Pin Nr]
# 26             -->              4     ENABLE RPI Level Shifter Hat
# 25             -->              21    CLK (Interrupt 2 Pin)
# 1              <--              15    MISO
# 2              -->              32    MOSI
# 21             -->              3     CS (Interrupt 1 Pin)

import RPi.GPIO as GPIO
import time
import sys

CLK = 25
MISO = 1
MOSI = 2
CS = 21

DEBUG = False
DELAY = 0.5


def setupSpiPins(clkPin, misoPin, mosiPin, csPin):
    ''' Set all pins as an output except MISO (Master Input, Slave Output)'''
    GPIO.setup(clkPin, GPIO.OUT)
    GPIO.setup(misoPin, GPIO.IN)
    GPIO.setup(mosiPin, GPIO.OUT)
    GPIO.setup(csPin, GPIO.OUT)

    # Enable RPI Logic Level Shifter (GPIO 26)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, True)


def sendBits(data, numBits, clkPin, mosiPin):
    ''' Sends 1 Byte or less of data'''

    data <<= (8 - numBits)

    for bit in range(numBits):

        # Set RPi's output bit high or low depending on highest bit of data field
        if data & 0x80:
            GPIO.output(mosiPin, GPIO.HIGH)
            if DEBUG:
                print("Send 1")
        else:
            GPIO.output(mosiPin, GPIO.LOW)
            if DEBUG:
                print("Send 0")

        # Advance data to the next bit
        data <<= 1

        # Pulse the clock pin HIGH then immediately low
        if DEBUG:
            time.sleep(DELAY)

        GPIO.output(clkPin, GPIO.HIGH)

        if DEBUG:
            time.sleep(DELAY)

        GPIO.output(clkPin, GPIO.LOW)
        # print("clk")


def recvBits(numBits, clkPin, misoPin):
    '''Receives arbitrary number of bits'''
    retVal = 0

    for bit in range(numBits):
        # Pulse clock pin
        time.sleep(0.0005)  # THis delay is necessary for the arduino to keep up

        if DEBUG:
            time.sleep(DELAY)

        GPIO.output(clkPin, GPIO.HIGH)

        if DEBUG:
            time.sleep(DELAY)

        GPIO.output(clkPin, GPIO.LOW)

        # Read 1 data bit in
        if GPIO.input(misoPin):
            retVal |= 0x1

        # Advance input to next bit
        retVal <<= 1

    # Divide by two to drop the NULL bit
    return (retVal/2)


if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        setupSpiPins(CLK, MISO, MOSI, CS)

        while True:

            # READ SPI:
            # Start the read with both clock and chip select low
            GPIO.output(CS, GPIO.LOW)

            read_command = 0x55  # 01010101

            print("SPI send read command: {0:b}".format(int(read_command)))
            sendBits(read_command, 8, CLK, MOSI)

            spi_value = recvBits(8, CLK, MISO)
            print("SPI read: {0:b}".format(int(spi_value)))
            # This should read 0xAA = 10101010

            # Set chip select high to end the read
            GPIO.output(CS, GPIO.HIGH)

            time.sleep(1)

    except KeyboardInterrupt:
        # Disable RPI LLS Board
        GPIO.output(26, False)
        GPIO.cleanup()
        sys.exit(0)
