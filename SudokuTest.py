import numpy as np
from SudokuSolver import *

# Load sudokus
sudokus = np.load("data/sudokus.npy")

# Load solutions
solutions = np.load("data/sudoku_solutions.npy")

for i in range(len(sudokus)):
   sudoku = sudokus[i].copy()
   print("This is sudoku number", i)
   print(sudoku)
   your_solution = sudoku_solver(sudokus[i])
   print("This is your solution for sudoku number", i)
   print(your_solution)
   print("Is your solution correct?")
   print(np.array_equal(your_solution, solutions[i]))
