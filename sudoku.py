import pygame, sys
from board import Board
from sudoku_generator import generate_sudoku

WIDTH = 638
HEIGHT = 708
BG_COLOR = (255, 255, 245)
DIFFICULTY = "medium"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

board = Board(9, 9, screen, DIFFICULTY)
board.draw()


def draw_game_over():
    pass


while True:
    screen.fill(BG_COLOR)
    board.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            clicked_cell = board.click(x, y)
            if clicked_cell:
                row, col = clicked_cell
                board.select(row, col)

    pygame.display.update()
