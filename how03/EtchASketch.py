#!/usr/bin/env python3
# From: https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/Encoder.html
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import time
import smbus

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
board = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
while True: 
    bus.write_i2c_block_data(matrix, 0, board)
    time.sleep(5)
    board[0] = 0x0F
    bus.write_i2c_block_data(matrix, 0, board)
    # check to see if the position has changed
    leftRightPosition = leftRightEncoder.position
    if leftRightPosition > 0:
        prevCol = col
        col = col + 1
    elif leftRightPosition < 0: 
        prevCol = col
        col = col - 1
    upDownPosition = upDownEncoder.position
    if upDownPosition > 0:
        prevRow = row
        row = row + 1
    elif upDownPosition < 0: 
        prevRow = row
        row = row - 1
