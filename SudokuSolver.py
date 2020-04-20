import numpy as np

result = np.zeros(shape = (9, 9))

# Find all possible values for current square
def findPossValues(y, x, sudoku):
    possVals = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    possVals = possVals - vertVals(x, sudoku)
    possVals = possVals - hztlVals(y, sudoku)
    possVals = possVals - squareVals(y, x, sudoku)
    return possVals

# Find all values in current column
def vertVals(x, sudoku):
    values = set()

    for i in range(9):
        if sudoku[i][x] != 0:
            values.add(sudoku[i][x])

    return values

# Find all values in current row
def hztlVals(y, sudoku):
    values = set()

    for i in range(9):
        if sudoku[y][i] != 0:
            values.add(sudoku[y][i])

    return values

# Find all values in current square
def squareVals(y, x, sudoku):
    values = set()
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] != 0:
                values.add(sudoku[y0 + i][x0 + j])

    return values

# Find first available empty space
def findEmpty(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)

    return None

def solve(solved_sudoku):
    global result

    empty = findEmpty(solved_sudoku)

    if not empty:
        return True

    y, x = empty
    possVals = findPossValues(y, x, solved_sudoku)

    for i in possVals:
        solved_sudoku[y][x] = i

        if solve(solved_sudoku):
            result = solved_sudoku
            return True

        solved_sudoku[y][x] = 0

    return False

# Solves a Sudoku puzzle and returns its unique solution.
def sudoku_solver(sudoku):
    solved_sudoku = sudoku

    if solve(solved_sudoku):
        return result
    else:
        for i in range(9):
            for j in range(9):
                solved_sudoku[i][j] = -1

        return solved_sudoku
