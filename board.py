import pygame, sys
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # How many cells to remove depending on difficulty
        self.removed_cells = {"easy": 20, "medium": 40, "hard": 50}[difficulty]

        self.board = generate_sudoku(9, self.removed_cells)
        self.cells = [
            [Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)
        ]


    def draw(self):
        pass


    def select(self, row, col):
        pass


    def click(self, x, y):
        pass


    def clear(self):
        pass


    def sketch(self, value):
        pass


    def place_number(self, value):
        pass


    def reset_to_original(self):
        pass


    def is_full(self):
        #checks if board is completely filled
        for row in self.board:
            for cell in row:
                if cell == 0: #if cell is 0, it's empty
                    return False
        return True

    def update_board(self):
        self.board = [
            [self.cells[row][col].value for col in range(9)] for row in range(9)
        ]


    def find_empty(self):
        pass


    def check_board(self):
        pass
