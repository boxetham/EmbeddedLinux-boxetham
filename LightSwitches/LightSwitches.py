import Adafruit_BBIO.GPIO as GPIO
import sys 

if True:
    GPIO.setup("P9_12", GPIO.OUT)
    GPIO.setup("P9_13", GPIO.OUT)
    GPIO.setup("P9_14", GPIO.OUT)
    GPIO.setup("P9_15", GPIO.OUT)
    GPIO.setup("P9_41", GPIO.IN)
    GPIO.setup("P9_42", GPIO.IN)
    GPIO.setup("P9_21", GPIO.IN)
    GPIO.setup("P9_22", GPIO.IN)
    val = GPIO.input("P9_41")
    print(val)
    GPIO.output("P9_12", val)
    val = GPIO.input("P9_42")
    GPIO.output("P9_13", val)
    val = GPIO.input("P9_21")
    GPIO.output("P9_14", val)
    val = GPIO.input("P9_22")
    GPIO.output("P9_15", val)
    GPIO.cleanup()
