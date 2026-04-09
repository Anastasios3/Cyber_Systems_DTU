from machine import Pin, I2C # type: ignore
import time

led_green  = Pin(13, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_red    = Pin(14, Pin.OUT)

i2c = I2C(0, sda=Pin(27), scl=Pin(33), freq=400000)

MCP9808_ADDR = 0x18

def read_temp():
    data = i2c.readfrom_mem(MCP9808_ADDR, 0x05, 2)
    temp = ((data[0] & 0x1F) << 8) | data[1]
    if data[0] & 0x10:
        temp -= 0x2000
    return temp * 0.0625

def set_led(green, yellow, red):
    led_green.value(green)
    led_yellow.value(yellow)
    led_red.value(red)

THRESHOLD_YELLOW = 26.4
THRESHOLD_RED    = 26.5

while True:
    temp = read_temp()
    print(temp)
    if temp >= THRESHOLD_RED:
        set_led(0, 0, 1)
    elif temp >= THRESHOLD_YELLOW:
        set_led(0, 1, 0)
    else:
        set_led(1, 0, 0)
    time.sleep(0.1)

# ampy --port /dev/cu.usbserial-0143503E --baud 115200 put main.py
# screen /dev/cu.usbserial-0143503E 115200