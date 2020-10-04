""" all this code was taken from https://towardsdatascience.com/solve-sudokus-automatically-4032b2203b64 """


def printsudoku(sudoku):
    """print out our sudoky in this state"""
    print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j]) + " "
        print(line)


def findNextCellToFill(sudoku):
    """find all positions with 0 to fill other number"""
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    """check if e is valid number for this position now"""
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0):
    """https://towardsdatascience.com/solve-sudokus-automatically-4032b2203b64"""
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


def checkifsudoku(sudoku):
    """check if user give right input"""
    """changes values with temp so I don't need to change other person code
    Can change this TODO"""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] > 0:
                temp = sudoku[i][j]
                sudoku[i][j] = 0
                if not isValid(sudoku, i, j, temp):
                    sudoku[i][j] = temp
                    return False
                sudoku[i][j] = temp
    return True
