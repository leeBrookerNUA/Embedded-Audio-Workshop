# Passive buzzer connected to GP1 and GND
# Button connected to GP0 and GND
# A 440 Hz tone plays only while the button is held down.

import board       # Allows access to the Raspberry Pi Pico's GPIO pins
import digitalio   # Allows us to use digital input and output pins
import pwmio       # Allows us to control the buzzer using PWM
import time        # Allows us to add delays

# Set up the button on GPIO pin GP0
button = digitalio.DigitalInOut(board.GP0)

# Configure the button as an input with an internal pull-up resistor
button.switch_to_input(pull=digitalio.Pull.UP)

# Set up the buzzer on GPIO pin GP1
# Set the frequency to 440 Hz and start with the buzzer switched off
buzzer = pwmio.PWMOut(board.GP1, frequency=440, duty_cycle=0)

# Repeat the following instructions continuously
while True:

    # Check if the button is pressed
    # button.value is False when pressed because the button uses a pull-up resistor
    # If pressed, set the duty cycle to 32768 to turn the buzzer on
    # If not pressed, set the duty cycle to 0 to turn the buzzer off
    buzzer.duty_cycle = 32768 if not button.value else 0

    # Wait 0.01 seconds before checking the button again
    time.sleep(0.01)