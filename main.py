import machine
import utime

pled=machine.Pin(13,machine.Pin.OUT)

while True:
	pled.value(1)
	utime.sleep(1)
	pled.value(0)
	utime.sleep(1)

