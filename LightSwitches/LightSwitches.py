import Adafruit_BBIO.GPIO as GPIO
 
GPIO.setup("gpio1_28", GPIO.OUT)
GPIO.output("gpio1_28", GPIO.HIGH)
GPIO.cleanup()