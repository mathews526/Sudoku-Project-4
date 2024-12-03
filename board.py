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
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False

        if 0 <= row < 9 and 0 <= col < 9:
            self.cells[row][col].selected = True

    def click(self, x, y):
        pass


    def clear(self):
        pass


    def sketch(self, value):
        pass


    def place_number(self, value):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].selected:
                    if self.cells[row][col] == 0:
                        self.cells[row][col].value = value
                    return

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
        self.update_board()

        for row in self.board:
            if len(set(row)) != 9 or 0 in row:
                return False

            for col in range(9):
                column = [self.board[row][col] for row in range(9)]
                if len(set(column)) != 9 or 0 in column:
                    return False

            for row_start in range(0, 9, 3):
                for col_start in range(0, 9, 3):
                    sub_grid = []
                    for r in range(row_start, row_start + 3):
                        for c in range(col_start, col_start + 3):
                            sub_grid.append(self.board[r][c])

                    if len(set(sub_grid)) != 9 or 0 in sub_grid:
                        return False
        return True

