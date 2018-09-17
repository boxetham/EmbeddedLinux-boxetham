#!/usr/bin/env python3
# From: https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/Encoder.html
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import time
import smbus

GPIO.setup("P9_23", GPIO.IN)
GPIO.setup("P9_42", GPIO.IN)

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70  # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)  # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)  # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)  # Full brightness (page 15)

# Instantiate the class to access channel eQEP, and initialize
# that channel
leftRightEncoder = RotaryEncoder(eQEP1)
leftRightEncoder.setAbsolute()  # set to 0 position
leftRightEncoder.enable()

upDownEncoder = RotaryEncoder(eQEP2)
upDownEncoder.setAbsolute()  # set to 0 position
upDownEncoder.enable()

col = 0
row = 0
mapping = [0, 1, 2, 4, 8, 16, 32, 64]
board = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
while True:
    stop = GPIO.input("P9_23")
    clear = GPIO.input("P9_42")
    if clear == 1:
        board = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    if stop == 1:
        break
    board[col * 2] = mapping[row] | board[col * 2]  # turn path green to stay 
    board[(col * 2) - 1] = mapping[row]  # turn current position orange
    bus.write_i2c_block_data(matrix, 0, board)
    # check to see if the position has changed
    leftRightPosition = leftRightEncoder.position
    if leftRightPosition > 0:
        col = col + 1
        leftRightEncoder.setAbsolute()
    elif leftRightPosition < 0: 
        col = col - 1
        leftRightEncoder.setAbsolute()
    upDownPosition = upDownEncoder.position
    if upDownPosition > 0:
        row = row + 1
        upDownEncoder.setAbsolute() 
    elif upDownPosition < 0: 
        row = row - 1
        upDownEncoder.setAbsolute()
GPIO.cleanup()
