import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

# Pin configuration using BCM numbering (same pins as in your C code)
LCD_RS = 11  # WiringPi 11 corresponds to BCM 17
LCD_E = 10   # WiringPi 10 corresponds to BCM 27
LCD_D4 = 6   # WiringPi 6 corresponds to BCM 22
LCD_D5 = 5   # WiringPi 5 corresponds to BCM 24
LCD_D6 = 4   # WiringPi 4 corresponds to BCM 23
LCD_D7 = 1   # WiringPi 1 corresponds to BCM 18

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

# Initialize the LCD using the pins above.
lcd = CharLCD(cols=16, rows=2, pin_rs=LCD_RS, pin_e=LCD_E, pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7], numbering_mode=GPIO.BCM)

# Wait for LCD to initialize
time.sleep(1)

# Clear the LCD screen before writing
lcd.clear()

# Display text on the LCD
lcd.write_string("HELLO WORLD")

# Wait for user input
input("Press Enter to continue...")

# Clear the LCD screen
lcd.clear()

# Clean up GPIO
GPIO.cleanup()







# import wiringpi as wp
# from time import sleep

# LCD_RS = 11
# LCD_E = 10
# LCD_D4 = 6
# LCD_D5 = 5
# LCD_D6 = 4
# LCD_D7 = 1

# # Initialize wiringPi
# wp.wiringPiSetup()

# # Initialize the LCD
# lcd = wp.lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0)

# if lcd == -1:
#     print("lcd init failed!")
#     exit(1)

# # Set the cursor to the first position (0, 0)
# wp.lcdPosition(lcd, 0, 0)

# # Print the message to the LCD
# wp.lcdPuts(lcd, "HELLO WORLD")

# # Wait for user input
# input("Press Enter to clear the LCD...")

# # Clear the LCD
# wp.lcdClear(lcd)
