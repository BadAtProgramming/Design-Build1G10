import machine
import time
from machine import ADC

redLed=machine.Pin(15,machine.Pin.OUT)
blueLed=machine.Pin(27,machine.Pin.OUT)
greenLed=machine.Pin(33,machine.Pin.OUT)
button1=machine.Pin(36,machine.Pin.IN,machine.Pin.PULL_UP)
button2=machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_UP)
dataIn=machine.ADC(machine.Pin(34))
dataIn.atten(ADC.ATTN_11DB)

mainLed=machine.PWM(machine.Pin(12))
mainLed.duty(100)
mainLed.freq(78000)
dataIn.atten(ADC.ATTN_11DB)


while True:
	while not button1.value()==0:
		time.sleep(0.01)
	print("hello")
	first=button1.value()
	time.sleep(0.01)
	second=button1.value()
	if first and not second:
		print("hello")
		break
