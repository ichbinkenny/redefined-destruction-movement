import RPi.GPIO as GPIO
import multiprocessing
import sys

weapon_pin = 22
weapon_min_duty = 2.5
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

def reset():
    weapon.ChangeDutyCycle(weapon_min_duty)

def start_attacking():
    global should_attack
    should_attack = True

def stop_attacking():
    global should_attack
    should_attack = False
    reset()

def parseCommand(cmd):
    global should_attack
    if cmd == 'start':
        should_attack = True
        weapon_movement_proc.start()
    elif cmd == 'stop':
        should_attack = False
    else: # Assume we got a weapon type
        global weapon_type
        weapon_type = cmd

def attackLoop(should_attack, weapon):
    global weapon_duty
    while should_attack:
        if weapon == "Sword":
            #TODO put increment and set max and min vals here
            if weapon_duty + duty_increment <= weapon_max_duty:
                weapon_duty += duty_increment
            else:
                weapon_duty = weapon_min_duty
            weapon.ChangeDutyCycle(weapon_duty)
        elif weapon == "Axe":
            #TODO put increment and set max and min vals here
            if weapon_duty + duty_increment <= weapon_max_duty:
                weapon_duty += duty_increment
            else:
                weapon_duty = weapon_min_duty
            weapon.ChangeDutyCycle(weapon_duty)
        elif weapon == "Lifter":
            #TODO put increment and set max and min vals here
            if weapon_duty + duty_increment <= weapon_max_duty:
                weapon_duty += duty_increment
            else:
                weapon_duty = weapon_min_duty
            weapon.ChangeDutyCycle(weapon_duty)
def setup():
    reset()
    global weapon_movement_proc
    global weapon
    weapon_movement_proc = multiprocessing.Process(target=attackLoop, args=(should_attack, weapon))
    weapon_movement_proc.start()
    while True:
        cmd = sys.stdin.readline().strip()
        parseCommand(cmd)

if __name__ == "__main__":
    setup()