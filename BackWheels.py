import RPi.GPIO as GPIO
import sys

motorPin = 18

GPIO.setmode(GPIO.BCM)

motor = GPIO.PWM(motorPin, 50)

def speedControl():
    while True:
        for line in sys.stdin:
            if int(line.strip()) is not None:
                val = int(line.strip())
                motor.ChangeDutyCycle(val)

if __name__ == "__main__":
    motor.start(0)
    speedControl()
