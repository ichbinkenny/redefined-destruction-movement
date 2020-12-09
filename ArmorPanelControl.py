import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

armor_panel_1_pin = 22
armor_panel_2_pin = 23
armor_panel_3_pin = 24

armor_panel_1 = GPIO.setup(armor_panel_1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
armor_panel_2 = GPIO.setup(armor_panel_2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
armor_panel_3 = GPIO.setup(armor_panel_3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

### Test notes
# no armor connected: Expected: 0:0:0 Got: 0:0:0
# Armor 1 connected: Expected: 1:0:0 Got: 1:0:0
# Armor 2 connected: Expected: 0:1:0 Got: 0:1:0
# Armor 3 connected: Expected: 0:0:1 Got: 0:0:1
# Armor 1 and 3 connected: Expected: 1:0:1 Got: 1:0:1
# Armor 1 and 2 connected: Expected: 1:1:0 Got: 1:1:0
# Armor 2 and 3 connected: Expected: 0:1:1 Got: 0:1:1
# All armor connected: Expected: 1:1:1 Got: 1:1:1
# Passed: 8 Failed: 0
def readArmorStatus():
    armor_status = [int(GPIO.input(armor_panel_1_pin) == GPIO.LOW), int(GPIO.input(armor_panel_2_pin) == GPIO.LOW), int(GPIO.input(armor_panel_3_pin) == GPIO.LOW)]
    print("{}:{}:{}".format(armor_status[0], armor_status[1], armor_status[2]))

if __name__ == "__main__":
    readArmorStatus()
