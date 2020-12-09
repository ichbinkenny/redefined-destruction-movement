import RPi.GPIO as GPIO
import sys

align_servo = 25
full_left = 2.0
straight = 7.0
full_right = 12.0
fragment_amount = 10.0

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

motor = GPIO.setup(align_servo, GPIO.OUT)

align = GPIO.PWM(align_servo, 50)

### Test notes
# Wheels center on call: TRUE
# Passed: 1 Failed: 0
def stop():
    centerWheels(straight)
### Test notes
# Joystick fully left: Expected: Wheels full left Got: Wheels full left
# Joystick barely left: Expected: Slight wheels left Got: slight wheels left
# Passed: 2 Failed: 0
def turnLeft(val):
    direction = (straight + (val * 5))
#((straight - full_left) / fragment_amount) * abs(val)
    align.ChangeDutyCycle(direction)

### Test notes
# Joystick fully right: Expected: Wheels full right Got: Wheels full right
# Joystick barely right: Expected: Slight wheels right Got: slight wheels right
# Passed: 2 Failed: 0
def turnRight(val):
    direction = (straight + (val * 5))
#((full_right - straight) / fragment_amount) * abs(val)
    align.ChangeDutyCycle(direction)

### Test notes
# Wheels centered on call: TRUE
# Passed: 1 Failed: 0
def centerWheels(val):
    align.ChangeDutyCycle(straight)

### Test notes
# non-numeric value: Expected: Unexpected number format Got: Unexpected number format
# Val == 0: Expected: Centered Wheels Got: Centered Wheels
# Val >> 0: Expected: Full Right wheels Got: Full Right Wheels
# Val > 0: Expected: Slight Right Wheels Got: Slight Right Wheels
# Val < 0: Expected: Slight Left Wheels Got: Slight Left Wheels
# Val << 0: Expected: Full Left Wheels Got: Full Left Wheels.
# Passing: 6 Failing: 0
def loopForCommand():
    line = sys.stdin.readline().strip()
    try:
        val = float(line)
        if val > 0:
            turnRight(val)
        elif val < 0:
            turnLeft(val)
        else:
            centerWheels(val)
    except:
        print("Unexpected number format")
### Test notes
# Bot centers front wheels on run?: TRUE
# Passing: 1 Failing: 0
if __name__ == "__main__":
    align.start(straight)
    while True:
        loopForCommand()
