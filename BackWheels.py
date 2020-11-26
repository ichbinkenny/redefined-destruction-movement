import RPi.GPIO as GPIO
import sys

motorPin = 18

maxCycle = 12

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorPin, GPIO.OUT)

motor = GPIO.PWM(motorPin, 50)

def stop():
    motor.ChangeDutyCycle(0)

def speedControl():
    while True:
        line = sys.stdin.readline().strip()
        try:
            val = float(line)
            motor.ChangeDutyCycle(val * maxCycle)
        except:
            print("Unexpected value")

if __name__ == "__main__":
    motor.start(0)
    speedControl()
