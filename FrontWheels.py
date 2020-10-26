import RPi.GPIO as GPIO
import sys

align_servo = 17
full_left = 2.0
straight = 7.0
full_right = 12.0
fragment_amount = 100.0

GPIO.setmode(GPIO.BCM)

motor = GPIO.setup(align_servo, GPIO.OUT)

align = GPIO.PWM(align_servo, 50)

def turnLeft(val):
    direction = ((straight - full_left) / fragment_amount) * abs(val)
    align.ChangeDutyCycle(direction)

def turnRight(val):
    direction = ((full_right - straight) / fragment_amount) * abs(val)
    align.ChangeDutyCycle(direction)

def centerWheels(val):
    align.ChangeDutyCycle(straight)

def loopForCommand():
    for line in sys.stdin:
        print(line)
        if int(line.strip()) is not None:
            val = int(line.strip())
            if val < 0:
                turnLeft(val)
            elif val > 0:
                turnRight(val)
            else:
                centerWheels(val)

if __name__ == "__main__":
    align.start(straight)
    loopForCommand()
