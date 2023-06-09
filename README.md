# Sudoku-Solver
This repository contains two main files. 
- One file is the original sudoku solver that I wrote, which is capable of solving any sudoku board using the backtracking algorithm. This code uses 3 main functions: One function to find the first empty slot on the board, one function to verify the validity of a value being entered into a certain position on the board, and a solve function which uses the first two as well as the back tracking algorithm to solve the entire board.
- The second file was added in to create a Graphical User Interface where a user can play sudoku. This script uses pygame along with the time module to create a functioning Sudoku game that can be solved at any time by using the original Sudoku Solver functions. 

# Instructions to play
- Launch the Sudoku game by running the SudokuGUI.py Python script.  
- The game window will open, displaying the Sudoku grid.  
- Use the mouse cursor to navigate and interact with the game.

![SudokuUnsolved](SudokuUnsolved.png)
![SudokuSolving](SudokuSolving.png)

## Buttons and their purposes:

- Number Keys (1-9): Press any number key to select the corresponding digit as the input value.  
- Delete Key: Press the Delete key to clear the selected cell's value.  
- Spacebar: Press the Spacebar to automatically solve the Sudoku puzzle.  
- Return/Enter Key: Press the Return/Enter key to enter the selected digit into the Sudoku grid.

## Gameplay:

- Select a cell by clicking on it. The selected cell will be highlighted in red.  
- Choose a number (1-9) to input into the selected cell. The selected digit will be displayed in the cell.  
- If you want to change or clear a value, either select the cell again and enter a different number or press the Delete key to clear the cell.  
- To check if the number entered in the cell is correct, press the Return/Enter key. If the number is correct, it will be displayed in black. Otherwise, an 'X' will be displayed in red.  
- Continue filling in the cells with the correct numbers based on the Sudoku rules.  
- If you get stuck or want to see the solution, press the Spacebar to automatically solve the Sudoku puzzle.  
- The game will end when all cells are filled correctly and the entire Sudoku grid is solved.  
- Remember to pay attention to the strikes (X) displayed at the bottom. Strikes are counted when an incorrect number is entered in a cell.  

Enjoy playing Sudoku and have fun!




