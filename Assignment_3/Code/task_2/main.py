from machine import Pin # type: ignore
import time

led_green  = Pin(13, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_red    = Pin(14, Pin.OUT)
button     = Pin(21, Pin.IN, Pin.PULL_UP)

leds = [led_green, led_yellow, led_red]
current = 0

def set_led(index):
    for i, led in enumerate(leds):
        led.value(1 if i == index else 0)

set_led(0)

while True:
    if button.value() == 0:
        while button.value() == 0:
            time.sleep(0.01)
        current = (current + 1) % 3
        set_led(current)
    time.sleep(0.01)

# ampy --port /dev/cu.usbserial-0143503E --baud 115200 put main.py