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

data=machine.ADC(machine.Pin(32))
data.atten(ADC.ATTN_11DB)
#data.width(ADC.WIDTH_11BIT)

mainLed=machine.PWM(machine.Pin(13))
mainLed.freq(78000)
mea=0
k=0
r=0

while True:
    if button1.value()!=0:
        blueLed.value(1)
        redLed.value(0)

        while mea<=1023:
            mainLed.duty(mea)
            time.sleep(0.01)
            while k<10:
                r+=data.read()
                k+=1
                time.sleep(0.001)
            r=r/10
            file.write(repr(r)+ (';' if mea != 1023 else ''))
            r=0
            k=0
            mea+=1
        break

file.close()
