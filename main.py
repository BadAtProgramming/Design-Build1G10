import machine
import time
from machine import ADC
import math

redLed=machine.Pin(15,machine.Pin.OUT)
blueLed=machine.Pin(27,machine.Pin.OUT)
greenLed=machine.Pin(33,machine.Pin.OUT)
button1=machine.Pin(36,machine.Pin.IN)
button2=machine.Pin(39,machine.Pin.IN)

#Turn on only blue LED
redLed.value(1)
greenLed.value(1)

data=machine.ADC(machine.Pin(32))
data.atten(ADC.ATTN_11DB)

mainLed=machine.PWM(machine.Pin(13))
mainLed.freq(78000)
mainLed.duty(600)

timer=0

while True:
    if button1.value()!=0:
        blueLed.value(1)
        greenLed.value(0)
        clock=time.time()

        while True:
            if button2.value()!=0:
                redLed.value(0)
                greenLed.value(1)
                break

            elif timer==100: #for sleep(0.01), 1 second interval -> timer=100
                file=open('datafile.txt','a')
                k=0
                r=[]
                acu=0
                cal=0
                while k<100:
                    d=data.read()
                    r.append(d)
                    acu+=d
                    k+=1
                    time.sleep(0.001)
                acu=acu/100
                for el in r:
                    cal+=(float(el)-acu)**2
                cal=math.sqrt(cal/100)
                file.write(repr(time.time()-clock) + ',' + repr(acu) + ',' + repr(cal) + '\n')
                file.close()
                r.clear()
                timer=10

            else:
                timer+=1
                time.sleep(0.01)
    elif button2.value()!=0:
        redLed.value(0)
        blueLed.value(1)
        greenLed.value(1)
        break
    else:
        time.sleep(0.1)
