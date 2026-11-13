# Passive buzzer on GP1 -> GND; button GP0 -> GND
# Melody loops while button is held; stops when released.
import board
import digitalio
import pwmio
import time

button = digitalio.DigitalInOut(board.GP0)
button.switch_to_input(pull=digitalio.Pull.UP)
buzzer = pwmio.PWMOut(board.GP1, frequency=440,
                       duty_cycle=0, variable_frequency=True)
# (frequency in Hz, duration in seconds)
MELODY = [(261, 0.36), (262, 0.36), (392, 0.36), (393, 0.36),
        (440, 0.36), (441, 0.36), (392, 0.72), (349, 0.36), (350, 0.36), (329, 0.36), 
        (330, 0.36), (293, 0.36), (294, 0.36), (261, 0.72)]
index = 0
note_started = time.monotonic()

while True:
    now = time.monotonic()
    if button.value:  # released
        buzzer.duty_cycle = 0
        index = 0
        note_started = now
    else:  # held
        frequency, duration = MELODY[index]
        buzzer.frequency = frequency
        buzzer.duty_cycle = 32768
        if now - note_started >= duration:
            index = (index + 1) % len(MELODY)
            note_started = now
    time.sleep(0.01)