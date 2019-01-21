import machine
import time
from machine import ADC
import utime
import os

redLed=machine.Pin(15,machine.Pin.OUT)
blueLed=machine.Pin(27,machine.Pin.OUT)
greenLed=machine.Pin(33,machine.Pin.OUT)
button1=machine.Pin(36,machine.Pin.IN)
button2=machine.Pin(39,machine.Pin.IN)
file=open('datafile.txt','w')

#Turn on only blue LED
redLed.value(1)
greenLed.value(1)
blueLed.value(0)

data=machine.ADC(machine.Pin(32))
data.atten(ADC.ATTN_11DB)
#data.width(ADC.WIDTH_11BIT)

mainLed=machine.PWM(machine.Pin(13))
mainLed.freq(78000)
mainLed.duty(600)
k=0
r=0



while True:
    if button1.value()!=0:
        blueLed.value(1)
        redLed.value(0)

        while k<100:
            r+=data.read()
            k+=1
            time.sleep(0.01)
        r=r/100
        file.write(repr(r)+'\n')
        print(repr(r))
        r=0
        k=0

        time.sleep(1)

        redLed.value(1)
        greenLed.value(0)

    elif button2.value()!=0:
        greenLed.value(1)
        blueLed.value(0)
        break

    time.sleep(0.1)

file.close()
