# General wiring

1. 3V - A_2 to red positive rail
2. GND - B_4 to blue negative rail

# MCP 9808

1. VDD - D_45 to red positive rail
2. GND - D_46 to blue negative rail
3. SCL - D_47 to GPIO_33
4. SDA - D_48 to GPIO_27 + B_48 1kΩ resistor to red positive rail
5. Alert - no connection
6. A0 - D_50 to to blue negative rail
7. A1 - D_51 to to blue negative rail
8. A2 - D_52 to to blue negative rail

# RGB Light

1. Red - C_29 + 330Ω resistor (D_29 to F_29) + Jumping wire (J_29 to GPIO13 at J_8)
2. Common pin - B_30 + Jumping wire (J_30 to red positive rail)
3. Green - C_31 + 330Ω resistor (D_31 to F_31) + Jumping wire (J_31 to GPIO15 at J_13)
4. Blue - C_32 + 330Ω resistor (D_32 to F_32) + Jumping wire (J_32 to GPIO14 at J_14)

# Link to video bellow

https://panopto.dtu.dk/Panopto/Pages/Viewer.aspx?id=4d123f00-a304-4143-9295-b42701439ef5

(I know the assignment said yellow, but because I wanted the differenciation to be more optically recognisable, I made it blue)
