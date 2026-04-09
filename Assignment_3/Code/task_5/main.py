from machine import Pin, PWM, ADC # type: ignore
import time

pot = ADC(Pin(12))
pot.atten(ADC.ATTN_11DB)  

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(32), freq=1000)
b = PWM(Pin(14), freq=1000)

while True:
    val = pot.read()
    duty = 1023 - (val // 4)
    r.duty(duty)
    g.duty(duty)
    b.duty(duty)
    time.sleep(0.05)

# ampy --port /dev/cu.usbserial-0143503E --baud 115200 put main.py