import pygame
import sys
import random

# Initialize the game board and variables
board = [[' ' for _ in range(3)] for _ in range(3)]
player_turn = 'X'
difficulty = 'Easy'  # Default difficulty

# Pygame settings
pygame.init()
WIDTH, HEIGHT = 300, 300
SQUARE_SIZE = WIDTH // 3
LINE_WIDTH = 15
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
BUTTON_COLOR = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.Font(None, 36)

# Draw grid lines
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw 'X' and 'O' marks
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Check for a winner
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check for a draw
def is_draw():
    return all([cell != ' ' for row in board for cell in row])

# AI move based on difficulty
def ai_move():
    if difficulty == 'Easy':
        random_move()
    elif difficulty == 'Medium':
        if random.choice([True, False]):
            random_move()
        else:
            optimal_move()
    elif difficulty == 'Hard':
        optimal_move()

# Make a random move for the AI
def random_move():
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = 'O'

# Make the optimal move using Minimax
def optimal_move():
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Difficulty selection popup
def select_difficulty():
    global difficulty
    running = True
    while running:
        screen.fill(BG_COLOR)

        # Draw buttons
        easy_button = pygame.Rect(WIDTH // 2 - 75, 50, 150, 50)
        medium_button = pygame.Rect(WIDTH // 2 - 75, 125, 150, 50)
        hard_button = pygame.Rect(WIDTH // 2 - 75, 200, 150, 50)

        pygame.draw.rect(screen, BUTTON_COLOR, easy_button)
        pygame.draw.rect(screen, BUTTON_COLOR, medium_button)
        pygame.draw.rect(screen, BUTTON_COLOR, hard_button)

        # Draw button text
        draw_text('Easy', font, TEXT_COLOR, screen, easy_button.center)
        draw_text('Medium', font, TEXT_COLOR, screen, medium_button.center)
        draw_text('Hard', font, TEXT_COLOR, screen, hard_button.center)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    difficulty = 'Easy'
                    running = False
                elif medium_button.collidepoint(event.pos):
                    difficulty = 'Medium'
                    running = False
                elif hard_button.collidepoint(event.pos):
                    difficulty = 'Hard'
                    running = False

        pygame.display.update()

    # Clear the screen after choosing the difficulty
    screen.fill(BG_COLOR)

# Draw text centered on a position
def draw_text(text, font, color, surface, position):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=position)
    surface.blit(text_obj, text_rect)

# Display a popup message indicating the result
def show_result_message(message):
    screen.fill(BG_COLOR)
    draw_text(message, font, TEXT_COLOR, screen, (WIDTH // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds

# Main game loop
def main():
    global player_turn
    select_difficulty()  # Show the difficulty selection menu
    draw_lines()         # Draw the grid after clearing the screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle player click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_turn == 'X':
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // SQUARE_SIZE
                    clicked_col = mouseX // SQUARE_SIZE

                    if board[clicked_row][clicked_col] == ' ':
                        board[clicked_row][clicked_col] = 'X'
                        player_turn = 'O'
                        
                        # Redraw the board after the player's move
                        screen.fill(BG_COLOR)
                        draw_lines()
                        draw_figures()

                        if check_winner('X'):
                            show_result_message("Player wins!")
                            pygame.quit()
                            sys.exit()

                        if is_draw():
                            show_result_message("It's a draw!")
                            pygame.quit()
                            sys.exit()

                        # AI move
                        ai_move()
                        player_turn = 'X'
                        
                        # Redraw the board after the AI's move
                        screen.fill(BG_COLOR)
                        draw_lines()
                        draw_figures()

                        if check_winner('O'):
                            show_result_message("AI wins!")
                            pygame.quit()
                            sys.exit()

                        if is_draw():
                            show_result_message("It's a draw!")
                            pygame.quit()
                            sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()
