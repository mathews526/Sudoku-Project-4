import pygame, sys
from board import Board

WIDTH = 540
HEIGHT = 640
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)


def draw_game_start(screen):
    # Start menu screen made with the help of the lecture videos from module 9 with the Tic Tac Toe example

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


    while True: # Keeps user in the main menu until a button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos): # If easy button pressed
                    difficulty = "easy"
                    return difficulty # Returns easy difficulty to main
                elif medium_rect.collidepoint(event.pos): # If medium button pressed
                    difficulty = "medium"
                    return difficulty # Returns medium difficulty to main
                elif hard_rect.collidepoint(event.pos): # If hard button pressed
                    difficulty = "hard"
                    return difficulty # Returns hard difficulty to main
        pygame.display.update()


def success(board): # Checks to see if the user meets the win condition or not
    board.update_board()
    if board.is_full(): # Makes sure board is full
        if board.check_board(): # Checks if board is correct
            return "win"  # Game won
        else:
            return "loss"  # Game lost
    return None


def draw_buttons(screen): # Reset, restart, and exit buttons that appear below the sudoku board while playing
    button_font = pygame.font.Font(None, 50)

    # Initialize text
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # Initialize button background color and text
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surf.fill(LINE_COLOR)
    reset_surf.blit(reset_text, (10, 10))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rect = reset_surf.get_rect(center=(WIDTH // 4, HEIGHT - 50))
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    exit_rect = exit_surf.get_rect(center=(3 * WIDTH // 4, HEIGHT - 50))

    # Draw buttons
    screen.blit(reset_surf, reset_rect)
    screen.blit(restart_surf, restart_rect)
    screen.blit(exit_surf, exit_rect)

    return reset_rect, restart_rect, exit_rect


def draw_game_win(screen): # Displays game win screen
    text = "Game Won!"

    game_win_font = pygame.font.Font(None, 100)

    # Color background
    screen.fill(BG_COLOR)

    # initialize and draw title
    game_win_surf = game_win_font.render(text, 0, LINE_COLOR)
    game_win_rect = game_win_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150)
    )
    screen.blit(game_win_surf, game_win_rect)

    # Initialize text
    exit_text = game_win_font.render("Exit", 0, (255, 255, 255))

    #Initialize button background color and text
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))

    # Initialize button rectangle
    exit_rect = exit_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50)
    )

    # Draw button
    screen.blit(exit_surf, exit_rect)

    pygame.display.update()

    return exit_rect


def draw_game_over(screen): # Displays game over screen
    # Title text
    text = "Game Over :("
    game_over_font = pygame.font.Font(None, 100)

    # Color background
    screen.fill(BG_COLOR)

    # initialize and draw title
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150)
    )
    screen.blit(game_over_surf, game_over_rect)

    restart_text = game_over_font.render("Restart", 0, (255, 255, 255))

    # Added button to restart and head back to the main menu
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))

    # Initialize button rectangle
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50)
    )

    # Draw Button
    screen.blit(restart_surf, restart_rect)

    pygame.display.update()
    return restart_rect


def key_events(key_event):
    if board.selected_cell:

        selected_row, selected_col = board.selected_cell.row, board.selected_cell.col

        # Arrow key navigation
        if key_event.key == pygame.K_UP: # Move up
            if selected_row > 0:
                board.select(selected_row -1, selected_col)
        elif key_event.key == pygame.K_DOWN: # Move down
            if selected_row < 8:
                board.select(selected_row + 1, selected_col)
        elif key_event.key == pygame.K_LEFT: # Move left
            if selected_col > 0:
                board.select(selected_row, selected_col - 1)
        elif key_event.key == pygame.K_RIGHT: # Move right
            if selected_col < 8:
                board.select(selected_row, selected_col + 1)

        elif key_event.key == pygame.K_RETURN: # If the user presses enter, the number will change to a regular value
            if board.selected_cell.sketched_value != 0:
                board.place_number(board.selected_cell.sketched_value)
        elif pygame.K_1 <= key_event.key <= pygame.K_9: # Only allows numbers 1 through 9
            sketch_value = key_event.key - pygame.K_0
            board.sketch(sketch_value) # Updates the board with a sketched value
        elif key_event.key == pygame.K_BACKSPACE or key_event.key == pygame.K_DELETE: # Clears the cell value if backspace/delete is pressed
            board.clear()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Calls function to draw start screen and returns difficulty
    difficulty = draw_game_start(screen)

    # Initializes Board class
    board = Board(WIDTH, 540, screen, difficulty)

    run = True
    while run:
        screen.fill(BG_COLOR) # Colors background
        board.draw() # Draws sudoku board
        reset_button, restart_button, exit_button = draw_buttons(screen) # Returns coordinates and dimensions of buttons

        game_over_button = None
        game_win_button = None

        win_status = success(board) # Stores win status
        if win_status == "win":
            game_win_button = draw_game_win(screen) # Sent to game win screen
        elif win_status == "loss":
            game_over_button = draw_game_over(screen) # Sent to game over screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if reset_button.collidepoint(x,y): # On the sudoku screen
                    board.reset_to_original()
                elif restart_button.collidepoint(x, y): # On the sudoku screen
                    difficulty = draw_game_start(screen)
                    board = Board(WIDTH, 540, screen, difficulty)
                elif exit_button.collidepoint(x, y): # On the sudoku screen
                    pygame.quit()
                    sys.exit()
                elif game_over_button is not None and game_over_button.collidepoint(x, y): # On the game over screen
                    difficulty = draw_game_start(screen)
                    board = Board(WIDTH, 540, screen, difficulty)
                elif game_win_button is not None and game_win_button.collidepoint(x, y): # On the game win screen
                    pygame.quit()
                    sys.exit()
                else:
                    clicked_cell = board.click(x, y) # Stores the clicked cell row and col
                    if clicked_cell:
                        row, col = clicked_cell
                        board.select(row, col) # Selects the cell that was clicked on

            elif event.type == pygame.KEYDOWN:
                key_events(event)

        pygame.display.update()