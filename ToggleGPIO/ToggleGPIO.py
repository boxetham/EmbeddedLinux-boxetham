import Adafruit_BBIO.GPIO as GPIO
import sys
import time

toggle = 0
onOffTime = sys.argv[1]
GPIO.setup("gpio1_28", GPIO.OUT)
while True:
    toggle = not toggle
    GPIO.output("gpio1_28", toggle)
    time.sleep(onOffTime)
GPIO.cleanup("gpio1_28")