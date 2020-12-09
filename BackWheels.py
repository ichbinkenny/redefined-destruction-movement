import RPi.GPIO as GPIO
import sys
import re

motorPin = 18
revPin = 27

maxCycle = 12

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorPin, GPIO.OUT)
GPIO.setup(revPin, GPIO.OUT)

#motor = GPIO.PWM(motorPin, 50)
#rev = GPIO.PWM(revPin, 50)

### Test notes
# when called, motor stops moving. 
def stop():
    GPIO.output(motorPin, GPIO.LOW)
    GPIO.output(revPin, GPIO.LOW)
### Test notes
# when position is positive, device moves forward.
# when negative, output is present but motor does not move. Likely HW problem.
# Unknown values cause device to stop?: YES
# Passed: 2 Failed: 1
def speedControl():
    while True:
        line = re.sub(r"-?\D", "", sys.stdin.readline().strip())
        val = 0.0
        if 'world!' in line:
            continue
        #debug = open('back_debug.txt', 'a')
        try:
        #    with open('test.txt', 'a') as f:
       #         f.write(line)
            val = float(line)
        except ValueError:
            val = 0
            with open('test.txt', 'a') as f:
                f.write("ERRR: %s\n" % line)
        finally:
           # debug.close()
            if val > 0.0:
                GPIO.output(motorPin, GPIO.HIGH)
                GPIO.output(revPin, GPIO.LOW)
            elif val < 0.0:
                GPIO.output(motorPin, GPIO.LOW)
                GPIO.output(revPin, GPIO.HIGH)
            else:
                stop()

if __name__ == "__main__":
    speedControl()
