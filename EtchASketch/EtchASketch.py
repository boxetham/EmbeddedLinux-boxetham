import keyboard

row = 0
col = 0
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('u'):  
            if col != 7:
                col = col + 1
        if keyboard.is_pressed('d'):
            if col != 0:  
                col = col - 1
        if keyboard.is_pressed('r'):  
            if row != 7:
                row = row + 1
        if keyboard.is_pressed('l'):  
            if row != 0:
                row = row - 1
        if keyboard.is_pressed('c'):
            for x in range(0, range(len(board))):
                for y in range(0, range(len(board[x]))):
                    board[x][y] = 0
        board[row][col] = 1
    except:
        pass
    finally:
        # print board here
        for x in range(0, range(len(board))):
            for y in range(0, range(len(board[x]))):
                if board[x][y] == 1:
                    print("X ")
                else:
                    print("  ")