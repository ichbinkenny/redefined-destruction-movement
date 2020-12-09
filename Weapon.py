import RPi.GPIO as GPIO
import multiprocessing
import sys

weapon_pin = 17
weapon_min_duty = 2.0
weapon_max_duty = 12.5
weapon_duty = 0
duty_increment = 0.5
increment_delay = 0.1
should_attack = False
weapon_type = "UNDEF"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

weapon_out = GPIO.setup(weapon_pin, GPIO.OUT)
weapon = GPIO.PWM(weapon_pin, 50)

weapon_movement_proc = None

### Testing notes
# Weapon returns to starting position?: TRUE
# Passing: 1 Failing: 0
def weapon_reset():
    global weapon
    weapon.ChangeDutyCycle(weapon_min_duty)

### Testing notes
# Weapon moves to max position?: True
# Passing: 1 Failing: 0
def start_attacking():
    global should_attack
    should_attack = True
    weapon.ChangeDutyCycle(12.0)

### Testing notes
# Weapon returns to starting position?: TRUE
# Passing: 1 Failing: 0
def stop_attacking():
    global should_attack
    should_attack = False
    sys.stdout.write("Stopping")
    sys.stdout.flush()
    weapon_reset()

### Testing notes
# Weapon moves to max on button press?: TRUE
# Weapon resets to min on button release?: TRUE
def parseCommand(cmd):
    global should_attack
    global weapon
#    test = open('cmd_debug.txt', 'a')
    if 'pressed' in cmd:
        weapon.ChangeDutyCycle(12.0)
#        test.write("Attacking!\n")
    elif 'released' in cmd:
        weapon.ChangeDutyCycle(2.0)
#        test.write("Stopping!\n")
    else: # Assume we got a weapon type
        global weapon_type
        weapon_type = cmd
#    test.close()

### Test notes
# Unspecified Weapon moves to mid position: TRUE
# Specified Weapon moves to full attack: TRUE
# Passing: 2 Failing: 0
def attackLoop(should_attack, weapon):
    global weapon_duty
    while True:
        #sys.stdout.write("ATTACKING")
        #sys.stdout.flush()
        if weapon == "Sword" and should_attack:
            weapon.ChangeDutyCycle(2.0)
            #TODO put increment and set max and min vals here
#            if weapon_duty + duty_increment <= weapon_max_duty:
#                weapon_duty += duty_increment
#            else:
#                weapon_duty = weapon_min_duty
#            weapon.ChangeDutyCycle(weapon_duty)
        elif weapon == "Axe" and should_attack:
            weapon.ChangeDutyCycle(2.0)
#            #TODO put increment and set max and min vals here
#            if weapon_duty + duty_increment <= weapon_max_duty:
#                weapon_duty += duty_increment
#            else:
#                weapon_duty = weapon_min_duty
#            weapon.ChangeDutyCycle(weapon_duty)
        elif weapon == "Lifter" and should_attack:
            weapon.ChangeDutyCycle(2.0)
#            #TODO put increment and set max and min vals here
#            if weapon_duty + duty_increment <= weapon_max_duty:
#                weapon_duty += duty_increment
#            else:
#                weapon_duty = weapon_min_duty
#            weapon.ChangeDutyCycle(weapon_duty)
        else:
            print("WEAPON NOT FOUND")
            weapon.ChangeDutyCycle(7.0)

def setup():
    global weapon
    weapon.start(2.0)
    weapon_reset()
    global weapon_movement_proc
    while True:
        cmd = sys.stdin.readline().strip()
        parseCommand(cmd)

if __name__ == "__main__":
    setup()
