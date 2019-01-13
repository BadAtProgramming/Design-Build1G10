import machine
import time
from machine import ADC

redLed=machine.Pin(15,machine.Pin.OUT)
blueLed=machine.Pin(27,machine.Pin.OUT)
greenLed=machine.Pin(33,machine.Pin.OUT)
button1=machine.Pin(36,machine.Pin.IN,machine.Pin.PULL_UP)
button2=machine.Pin(39,machine.Pin.IN,machine.Pin.PULL_UP)
file=open('datafile.txt','w')

#Turn on only blue LED
redLed.value(1)
greenLed.value(1)

data=machine.ADC(machine.Pin(32))
data.atten(ADC.ATTN_11DB)
#data.width(ADC.WIDTH_11BIT)

mainLed=machine.PWM(machine.Pin(12))
mainLed.duty(100)
mainLed.freq(78000)

while True:
    if button1.value()!=0:
        blueLed.value(1)
        redLed.value(0)

        while True:
            if button2.value()!=0:
                redLed.value(1)
                greenLed.value(0)
                break
            else:
                #need to do a conversion before recording?
                file.write(repr(data.read())+';')
                time.sleep(10)
        break

file.close()

