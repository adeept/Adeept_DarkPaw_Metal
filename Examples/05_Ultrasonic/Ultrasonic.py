#!/usr/bin/env/python
# File name   : Ultrasonic.py
# Website     : www.Adeept.com
# Author      : Adeept
# Date        : 2025/04/22
from gpiozero import DistanceSensor
from time import sleep

Tr = 23
Ec = 24
sensor = DistanceSensor(echo=Ec, trigger=Tr,max_distance=2) # Maximum detection distance 2m.

# Get the distance of ultrasonic detection.
def checkdist():
    return (sensor.distance) *100 # Unit: cm

if __name__ == "__main__":
    while True:
        distance = checkdist() 
        print("%.2f cm" %distance)
        sleep(0.5)
