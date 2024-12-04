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
        self.unedited_board = [row[:] for row in self.board]

        self.selected_cell = None
        self.cells = [
            [Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)
        ]


    def draw(self):
        # draws an outline of the sudoku grid, with bold lines to delineate the 3x3 boxes
        # draws every cell on this board
        # code referenced from mod9 videos by the professor
        SQUARE_SIZE = 60
        LINE_COLOR = (0, 0, 0)  # black

        for i in range(10):
            line_width = 5 if i % 3 == 0 else 2
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (self.width, i * SQUARE_SIZE), line_width)
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, self.height), line_width)

        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()


    def select(self, row, col):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False

        self.selected_cell = self.cells[row][col]
        self.cells[row][col].selected = True


    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // (self.height // 9)
            col = x // (self.width // 9)
            return row, col
        return None


    def clear(self):
        if self.selected_cell and self.unedited_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)


    def sketch(self, value):
        # sets the sketched value of the current selected cell equal to user entered value
        # will be displayed in the top left corner of the cell using the draw() function
        rows = len(self.board)
        cols = len(self.board[0])
        for row in range(rows):
            for col in range(cols):
                if self.cells[row][col].selected:
                    if self.board[row][col] == 0:
                        self.cells[row][col].set_sketched_value(value)


    def place_number(self, value):
        if self.selected_cell and self.unedited_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(value) # Places entered value
            self.selected_cell.set_sketched_value(0) # Removes sketch


    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].value = self.unedited_board[row][col]
                self.cells[row][col].sketched_value = 0
                self.cells[row][col].selected = False
        self.update_board()


    def is_full(self):
        #checks if board is completely filled
        self.update_board()  # Sync the Cell values with the board
        for row in self.board:
            if 0 in row:  # Check for any empty cells
                return False
        return True


    def update_board(self):
        self.board = [
            [self.cells[row][col].value for col in range(9)] for row in range(9)
        ]


    def find_empty(self):
        # finds an empty cell and returns its row and col as a tuple (x,y)
        rows = len(self.board)
        cols = len(self.board[0])
        for row in range(rows):
            for col in range(cols):
                if self.cells[row][col] != 0:
                    self.cells[row][col].value = self.cells[row][col].sketched_value


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

