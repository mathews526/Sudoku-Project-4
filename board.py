import pygame, sys
from cell import Cell

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
