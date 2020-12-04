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

def weapon_reset():
    global weapon
    weapon.ChangeDutyCycle(weapon_min_duty)

def start_attacking():
    global should_attack
    should_attack = True
    weapon.ChangeDutyCycle(12.0)

def stop_attacking():
    global should_attack
    should_attack = False
    sys.stdout.write("Stopping")
    sys.stdout.flush()
    weapon_reset()

def parseCommand(cmd):
    global should_attack
    global weapon
    test = open('cmd_debug.txt', 'a')
    if 'pressed' in cmd:
        weapon.ChangeDutyCycle(12.0)
        test.write("Attacking!\n")
#        weapon_movement_proc.start()
    elif 'released' in cmd:
        weapon.ChangeDutyCycle(2.0)
        test.write("Stopping!\n")
        #stop_attacking()
    else: # Assume we got a weapon type
        global weapon_type
        weapon_type = cmd
    test.close()

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
#    sys.stdout.write(bytes("GOT HERE", "utf-8"))
#    sys.stdout.flush()
    global weapon_movement_proc
    #weapon_movement_proc = multiprocessing.Process(target=attackLoop, args=(should_attack, weapon))
    #weapon_movement_proc.start()
    while True:
        #debug = open('debug.txt', 'a')
        cmd = sys.stdin.readline().strip()
        #debug.write(cmd)
        #debug.close()
        parseCommand(cmd)

if __name__ == "__main__":
    setup()
