from machine import Pin, I2C # type: ignore
import time

i2c = I2C(0, sda=Pin(27), scl=Pin(33), freq=400000)
MCP9808_ADDR = 0x18

pin_r = Pin(13, Pin.OUT)
pin_g = Pin(32, Pin.OUT)
pin_b = Pin(14, Pin.OUT)

COMMON_ANODE = True

def set_color(r, g, b):
    pin_r.value(not r)
    pin_g.value(not g)
    pin_b.value(not b)

def read_temp():
    data = i2c.readfrom_mem(MCP9808_ADDR, 0x05, 2)
    temp = ((data[0] & 0x1F) << 8) | data[1]
    if data[0] & 0x10:
        temp -= 0x2000
    return temp * 0.0625

THRESHOLD_BLUE  = 27.7
THRESHOLD_RED    = 29.0

while True:
    temp = read_temp()
    print(temp)
    if temp >= THRESHOLD_RED:
        set_color(1, 0, 0)
    elif temp >= THRESHOLD_BLUE:
        set_color(0, 0, 1)
    else:
        set_color(0, 1, 0)
    time.sleep(0.1)

# ampy --port /dev/cu.usbserial-0143503E --baud 115200 put main.py

# screen /dev/cu.usbserial-0143503E 115200c