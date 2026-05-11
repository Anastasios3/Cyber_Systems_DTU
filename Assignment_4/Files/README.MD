# Wiring

# Button

1. TopLeftLeg >>> E20 > D20 jumping wire to Blue Negative rail
2. TopRightLeg >>> F20 > J20 jumping wire to GPIO_21 (B16)
3. ButtomLeftLeg >>> E22
4. ButtomRightLeg >>> F22

# RGB LED

1. Red channel >>> C25 > resistor from D25 to F25 > Jumping wire from H25 to GPIO_12 at J9
2. CND >>> C26 > Jumping wire from B26 to blue negative rail
3. Green channel >>> C27 > resistor from D27 to F27 > Jumping wire from H27 to GPIO_27 at J10
4. Blue channel >>> C28 > resistor from D28 to F28 > Jumping wire from H28 to GPIO_15 at J12

# Red LED

1. Long leg >>> I30 > jumping wire J30 to GPIO_13 (J8)
2. Short leg >>> I31 > Resistor 330 Ohm - one leg J31 and the other blue negative rail

# Potentiometer

1. Left Leg >>> A41 > Jumping wire (C41 to red positive rail)
2. Middle Leg >>> A43 > Jumping wire (C43 to GPIO_33 at J11)
3. Right Leg >>> A45 > Jumping wire (C45 to blue negative rail)

# Temperature sensor

1. Vdd >>> A57 > Jumping wire (C57 to red positive rail)
2. Gnd >>> A56 > Jumping wire (C56 to blue negative rail)
3. SCL >>> A55 > Jumping wire (C55 to SCL_pin at J15)
4. SDA >>> A54 > Jumping wire (C54 to SDA_pin at J16)
5. Alert >>> leave unconnected
6. A0 >>> leave unconnected
7. A1 >>> leave unconnected
8. A2 >>> leave unconnected

# URLs

http://192.168.4.1/pins
http://192.168.4.1/sensors
http://192.168.4.1/pin/led
http://192.168.4.1/sensor/temp
http://192.168.4.1/sensor/pot
http://192.168.4.1/pin/led/set/high
http://192.168.4.1/pin/led/set/low
http://192.168.4.1/rgb/1/0/0
http://192.168.4.1/rgb/0/1/0
http://192.168.4.1/rgb/0/0/1

# Commands

1. ampy --port /dev/tty.usbserial-0143503E --baud 115200 put main.py main.py
2. picocom -b 115200 /dev/tty.usbserial-0143503E
3. Restart the ESP
4. Connect to the ESP32 network
