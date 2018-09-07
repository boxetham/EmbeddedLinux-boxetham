import sys

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
    inputChar = sys.stdin.read(1)
    board[row][col] = 1
    if inputChar == 'u':  
        if row != 0:
            row = row - 1
        somethingChanged = True
    if inputChar == 'd':
        if row != 7:  
            row = row + 1
        somethingChanged = True
    if inputChar == 'r':  
        if col != 7:
            col = col + 1
        somethingChanged = True
    if inputChar == 'l':  
        if col != 0:
            col = col - 1
        somethingChanged = True
    if inputChar == 'c':
        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                board[x][y] = 0
        somethingChanged = True
