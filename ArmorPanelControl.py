import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

armor_panel_1_pin = 22
armor_panel_2_pin = 23
armor_panel_3_pin = 24

armor_panel_1 = GPIO.setup(armor_panel_1_pin, GPIO.IN)
armor_panel_2 = GPIO.setup(armor_panel_2_pin, GPIO.IN)
armor_panel_3 = GPIO.setup(armor_panel_3_pin, GPIO.IN)

def readArmorStatus():
    armor_status = [GPIO.input(armor_panel_1_pin) == GPIO.HIGH, GPIO.input(armor_panel_2_pin) == GPIO.HIGH, GPIO.input(armor_panel_3_pin) == GPIO.HIGH]
    print("{}:{}:{}".format(armor_status[0], armor_status[1], armor_status[2]))

if __name__ == "__main__":
    readArmorStatus()
