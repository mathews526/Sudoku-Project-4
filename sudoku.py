import pygame, sys
from board import Board
from sudoku_generator import generate_sudoku

WIDTH = 638
HEIGHT = 708

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

screen.fill((255, 255, 245))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
