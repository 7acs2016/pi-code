#!/usr/local/bin/python
# This program reads a switch which is activated
# ONLY when a plug is inserted inside the wall socket
# This means the wall socket will be safe for kids
# and will only be activated (electricity ON) when a plug is inserted

import RPi.GPIO as GPIO, time, os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
#check if switch is pressed i.e if a plug is inserted in the socket wall

while True:
    if (GPIO.input(4)==False):
        GPIO.output(18, GPIO.HIGH)# this will turn ON the red LED       
                                  # this also means wall socket is LIVE!!
        GPIO.output(17, GPIO.LOW)
        os.system('clear')
        print (" CAUTION!! wall socket is LIVE!!")
    else:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        os.system('clear')
        print(" wall socket is safe")
