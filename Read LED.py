import machine
from machine import ADC
import time

#power LED and sensor
p12=machine.Pin(12,machine.Pin.OUT)
p12.value(1)

#the recording starts when button is pressed (A4 slot is 36)
start=machine.Pin(36,machine.Pin.IN)
#if A4.value()==1 It's pressed down, 0 if not
#indicator to show recording has started(not sure if this works)
#write a code to save if the button has been pressed or not
if :
    green.value(0)
    red.value(1)


#power green and red light: red:data is receiving, green:okay to disconnect
green=machine.Pin(32,machine.Pin.OUT)
red=machine.Pin(14,machine.Pin.OUT)

#assign variable to receive data (blue line)
data=machine.ADC(machine.Pin(33))
#data.read()
#this will give a high value (maximum value of 4095)

#set attenuation(scaling voltage) and width
#At this stage we don't know what gives the best data, or the least noise, so change accordingly
data.atten(ADC.ATTN_11DB)
#or adc.atten(ADC.ATTN_6DB)
#now read!
data.read()

#To change setting of LED: digital to analog
led=machine.PWM(machine.Pin(12))
#set intensity 1000
led.duty(100)
#set frequency upper bound 78000
led.freq(70000)

#define a function to receive data continuously and break when button is pressed
#variable "value" is used as an indicator
end=0
value=0
def getData(data):
    while True:
        print(data.read())
        time.sleep(0.5)
        end=machine.Pin(36,machine.Pin.IN)
        if end==1:
            value=1
            break

#indicator to show recording has stopped
if value==1:
    green.value(1)
    red.value(0)

#save data somewhere
