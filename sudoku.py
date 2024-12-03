import pygame, sys
from board import Board

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


def key_events(key_event):
    if board.selected_cell:
        if key_event.key == pygame.K_RETURN:
            if board.selected_cell.sketched_value != 0:
                board.place_number(board.selected_cell.sketched_value)
        elif pygame.K_1 <= key_event.key <= pygame.K_9:
            sketch_value = key_event.key - pygame.K_0
            board.sketch(sketch_value)
        elif key_event.key == pygame.K_BACKSPACE:
            board.clear()


while True:
    screen.fill(BG_COLOR)
    board.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            clicked_cell = board.click(x, y)
            if clicked_cell:
                row, col = clicked_cell
                board.select(row, col)
        elif event.type == pygame.KEYDOWN:
            key_events(event)

    pygame.display.update()
