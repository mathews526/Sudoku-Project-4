import pygame
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

        # Generates the board and stores it
        self.board = generate_sudoku(9, self.removed_cells)
        # The board without any user changes
        self.unedited_board = [row[:] for row in self.board]

        self.selected_cell = None
        self.cells = [
            [Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)
        ]


    def draw(self):
        # code referenced from mod9 videos by the professor
        square_size = 60
        line_color = (0, 0, 0)  # black

        # draws an outline of the sudoku grid, with bold lines to delineate the 3x3 boxes
        for i in range(10):
            line_width = 5 if i % 3 == 0 else 2
            pygame.draw.line(self.screen, line_color, (0, i * square_size), (self.width, i * square_size), line_width)
            pygame.draw.line(self.screen, line_color, (i * square_size, 0), (i * square_size, self.height), line_width)

        # Draws all cells onto the board
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()


    def select(self, row, col):
        # Deselect all cells
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False

        # Selects specific cell
        self.selected_cell = self.cells[row][col]
        self.cells[row][col].selected = True


    # Returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None
    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            row = y // (self.height // 9)
            col = x // (self.width // 9)
            return row, col
        return None


    # Clears the value cell if that value was originally empty in the unedited board
    def clear(self):
        if self.selected_cell and self.unedited_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)


    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.
    def sketch(self, value):
        rows = len(self.board)
        cols = len(self.board[0])
        for row in range(rows):
            for col in range(cols):
                if self.cells[row][col].selected:
                    if self.board[row][col] == 0:
                        self.cells[row][col].set_sketched_value(value)


    # Sets the value of the current selected cell equal to user entered value if it is empty in the unedited board.
    # Called when the user presses the Enter key and clears the sketched value afterward.
    def place_number(self, value):
        if self.selected_cell and self.unedited_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(value) # Places entered value
            self.selected_cell.set_sketched_value(0) # Removes sketch


    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
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


    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        self.board = [
            [self.cells[row][col].value for col in range(9)] for row in range(9)
        ]


    def find_empty(self):
        # finds an empty cell and returns its row and col as a tuple (x, y)
        rows = len(self.board)
        cols = len(self.board[0])
        for row in range(rows):
            for col in range(cols):
                if self.cells[row][col] != 0:
                    return row, col
        return None


    # Checks whether the Sudoku board is solved correctly.
    def check_board(self):
        self.update_board()

        # Validate each row
        for row in self.board:
            # Converts the row into a set to check for duplicates and if there are any 0s (empty cells).
            if len(set(row)) != 9 or 0 in row:
                return False

            # Validate each column
            for col in range(9):
                column = [self.board[row][col] for row in range(9)]
                # Converts the col into a set to check for duplicates and if there are any 0s (empty cells).
                if len(set(column)) != 9 or 0 in column:
                    return False

            # Validate each box/subgrid
            for row_start in range(0, 9, 3):
                for col_start in range(0, 9, 3):
                    sub_grid = []
                    for r in range(row_start, row_start + 3): # Rows in the subgrid
                        for c in range(col_start, col_start + 3): # Cols in the subgrid
                            sub_grid.append(self.board[r][c])

                    # Checks for duplicates or empty cells
                    if len(set(sub_grid)) != 9 or 0 in sub_grid:
                        return False
        return True

