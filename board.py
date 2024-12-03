import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0


    def set_cell_value(self, value):
        self.value = value


    def set_sketched_value(self, value):
        self.sketched_value = value


    def draw(self):
        pass


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty


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
        pass


    def find_empty(self):
        pass


    def check_board(self):
        pass
