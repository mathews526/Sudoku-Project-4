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
            # "Draw the Grid & Tic Tac Toe", "Import Functionalities", "Write the Code"
        SQUARE_SIZE = 60
        BOARD_ROWS = 9
        BOARD_COLS = 9
        LINE_COLOR = (0, 0, 0)  # black
        BORDER_LINE_WIDTH = 2  # skinny line
        BOLDED_LINE_WIDTH = 5
        # draw horizontal lines
        for i in range(1, BOARD_ROWS):
            if i == 3 and i == 6: # bold lines for every big square
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),  # starting position
                    (self.width, i * SQUARE_SIZE),  # ending position
                    BOLDED_LINE_WIDTH # bolded line width
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),  # starting position
                    (self.width, i * SQUARE_SIZE),  # ending position
                    BORDER_LINE_WIDTH # regular line width
                )

        # draw vertical lines
        for j in range(1, BOARD_COLS):
            if j == 3 and j == 6: # bold lines for every big square
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),  # starting position
                    (j * SQUARE_SIZE, self.height),  # ending position
                    BOLDED_LINE_WIDTH # bolded line width
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0), # starting position
                    (j * SQUARE_SIZE, self.height), # ending position
                    BORDER_LINE_WIDTH # regular line width
                )

        # draw cells
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].draw()


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
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].selected:
                    if self.cells[row][col] == 0:
                        self.cells[row][col].value = value
                    return


    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].value = self.board[row][col]
                self.cells[row][col].sketched_value = 0
                self.cells[row][col].selected = False


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

