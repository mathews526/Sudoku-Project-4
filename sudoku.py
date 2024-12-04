import pygame, sys
from board import Board
from sudoku_generator import generate_sudoku

WIDTH = 540
HEIGHT = 640
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)


def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surf = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surf, title_rect)

    # Initialize text
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surf.fill(LINE_COLOR)
    easy_surf.blit(easy_text, (10,10))
    medium_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surf.fill(LINE_COLOR)
    medium_surf.blit(medium_text, (10, 10))
    hard_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surf.fill(LINE_COLOR)
    hard_surf.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rect = easy_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    medium_rect = medium_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rect = hard_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))

    # Draw buttons
    screen.blit(easy_surf, easy_rect)
    screen.blit(medium_surf, medium_rect)
    screen.blit(hard_surf, hard_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    difficulty = "easy"
                    return difficulty
                elif medium_rect.collidepoint(event.pos):
                    difficulty = "medium"
                    return difficulty
                elif hard_rect.collidepoint(event.pos):
                    difficulty = "hard"
                    return difficulty
        pygame.display.update()


def success(board):
    if board.is_full():
        if board.check_board():
            return True
        else:
            return False
    return None


def draw_game_win():
    pass


def draw_game_over(screen, winner):
    game_over_font = pygame.font.Font(None, 100)
    screen.fill(BG_COLOR)

    if winner != 0:
        text = "Game Won!"
    else:
        text = "Game Over :("

    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50)
    )
    screen.blit(game_over_surf, game_over_rect)

    restart_surf = game_over_font.render(
        "RESTART",
        0,
        LINE_COLOR
    )
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150)
    )
    screen.blit(restart_surf, restart_rect)

    pygame.display.update()



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


if __name__ == '__main__':
    game_over = False
    winner = 0

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    difficulty = draw_game_start(screen) # Calls function to draw start screen
    sudoku_board = generate_sudoku(9, difficulty) # From sudoku_generator

    board = Board(WIDTH, 540, screen, difficulty)
    board.draw()


    while True:
        screen.fill(BG_COLOR)
        board.draw()

        win_status = success(board)

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
        if game_over:
            if board.board == sudoku_board[1]:
                winner = 1
            elif board.board != sudoku_board[1]:
                winner = 0
            pygame.display.update()
            draw_game_over(screen, winner)

        pygame.display.update()
