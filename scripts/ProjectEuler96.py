import time
start = time.time()

# Print the Sudoku Board
def printBoard(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col],end='')
        print()

# Calculate the 3-digit number from each board
def calculateSum(board):
    return 100*board[0][0] + 10*board[0][1] + board[0][2]

# Read file, parse sudoku board and call corresponding functions
def getBoard():
    with open(r'C:\Users\Vangelis\Desktop\p096_sudoku.txt','r') as file:
        line = True
        totalSum = 0
        counter = 0
        while line:
            board = []
            line = file.readline()
            for i in range(9):
                column = []
                row = file.readline().replace('\n','')
                for character in row:
                    digit = int(character)
                    column.append(digit)
                board.append(column)
            solve(board)
            printBoard(board)
            totalSum += calculateSum(board)
            counter += 1
            if counter == 50:
                break
        print(totalSum)

# Find next empty space in Sudoku board and return dimensions
def findEmpty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 :
                return row,col
    return None

# Check whether a specific number can be used for specific dimensions
def isValid(board, num, pos):

    row, col = pos
    # Check if all row elements include this number
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check if all column elements include this number
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already included in the block
    rowBlockStart = 3* (row // 3)
    colBlockStart = 3* (col // 3)

    rowBlockEnd = rowBlockStart + 3
    colBlockEnd = colBlockStart + 3
    for i in range(rowBlockStart, rowBlockEnd):
        for j in range(colBlockStart, colBlockEnd):
            if board[i][j] == num:
                return False

    return True

# Solve Sudoku using backtracking
def solve(board):
    blank = findEmpty(board)
    if not blank:
        return True
    else:
        row, col = blank

    for i in range(1,10):
        if isValid(board, i, blank):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

getBoard()
end = time.time()
print("The time of execution of above program is :", end-start, 's')
