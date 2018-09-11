import sys
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_41", GPIO.in)
GPIO.setup("P9_42", GPIO.in)
GPIO.setup("P9_21", GPIO.in)
GPIO.setup("P9_22", GPIO.in)
somethingChanged = True
row = 0
col = 0
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
print("Move by pressing the keyboard button corresponding to the way you")
print("want to move and then hit enter")
print("Directions: u - up, d - down, r - right, l - left c - clear the board")
print("The O is where the curser is currently")
while True:  # making a loop
    # print board here
    if somethingChanged:
        sys.stdout.write("  ")
        for x in range(0, len(board)):
            sys.stdout.write(`x + 1` + " ")
        sys.stdout.write("\n")
        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                if y == 0:
                    sys.stdout.write(`x + 1` + " ")
                if x == row and y == col:
                    sys.stdout.write("O ")
                elif board[x][y] == 1:
                    sys.stdout.write("X ")
                else:
                    sys.stdout.write("  ")
            sys.stdout.write("\n")
        sys.stdout.flush()
        somethingChanged = False
    board[row][col] = 1
    left = GPIO.input("P9_41")
    right = GPIO.input("P9_42")
    up = GPIO.input("P9_21")
    down = GPIO.input("P9_22")
    if up == 1:  
        if row != 0:
            row = row - 1
        somethingChanged = True
    if down == 1:
        if row != 7:  
            row = row + 1
        somethingChanged = True
    if right == 1:  
        if col != 7:
            col = col + 1
        somethingChanged = True
    if left == 1:  
        if col != 0:
            col = col - 1
        somethingChanged = True
