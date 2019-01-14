import machine
import time
from machine import ADC
import utime

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
mainLed.duty(0)
mainLed.freq(78000)

timer=0
k=0
r=0

while True:
    if button1.value()!=0:
        blueLed.value(1)
        redLed.value(0)

        while True:
            if button2.value()!=0:
                redLed.value(1)
                greenLed.value(0)
                break
            elif timer==100: #for sleep(0.01), 1 second interval -> timer=100
                while k<10:
                    r+=data.read
                    k+=1
                    time.sleep(0.001)
                file.write(repr(r/10)+';')
                timer=1
            else:
                timer+=1
                time.sleep(0.01)
        break

file.close()
