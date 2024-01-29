from machine import Pin
from time import sleep

pin0 = Pin("LED" ,Pin.OUT)
pin1 = Pin("GP15" ,Pin.OUT)

while True:
    pin1.toggle()
    sleep(0.1)
    pin1.toggle()
    sleep(0.4)
    pin0.toggle()
    sleep(0.1)
    pin0.toggle()
    sleep(0.4)
    pin0.toggle()
    sleep(0.1)
    pin0.toggle()
    sleep(0.4)
    pin0.toggle()
    sleep(0.1)
    pin0.toggle()
    sleep(0.4)