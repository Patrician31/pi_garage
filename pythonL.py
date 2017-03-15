#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pin = 17

# loop through pins and set mode and state to 'low'

GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin, GPIO.HIGH)

def trigger():
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2) 
    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

try: 
    trigger()
         
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
