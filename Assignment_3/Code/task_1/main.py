from machine import Pin  # type: ignore
import time

led = Pin(13, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    if button.value() == 0:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
    else:
        led.value(0)

# ampy --port /dev/cu.usbserial-0143503E --baud 115200 put main.py