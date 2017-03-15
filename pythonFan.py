#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pin = 22

# loop through pins and set mode and state to 'low'
GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin, GPIO.HIGH)

while True:
	GPIO.output(pin, GPIO.LOW)
        time.sleep(60*15)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(60*60*3)

