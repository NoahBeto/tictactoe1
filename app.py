import pygame, sys
pygame.init()

WIDTH, HEIGHT, LINE_WIDTH = 600, 700, 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE, CIRCLE_RADIUS = WITH // BOARD_COLS, WIDTH // (3 * BOARD_CLS)
CIRCLE_WIDTH, CROSS_WIDTH = 15, 25
SPACE = SQUARE_SIZE // 4

WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), 255, 0, 0), (0, 255, 0), (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe"
font = pygame.font.SysFont(None, 50)

board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player:
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return all(board[row][col] != 0 for row in range(BOARD_ROWS for col in range(BOARD_COLS))

def restart():
    screen.fill(WHITE)
    draw_lines(
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[rw][col] = 0

def show_play_again():
    play_again_text = font.render("Press 'R' to play again", True, BLACK)
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT - 50))

player, game_over, score = 1, False, {1: 0, 2: 0}

while True:
    screen.fill(WHITE)
    draw_lines(
    draw_figures(

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row, clicked_col = mouseY // SQUARE_SIZE, mouseX // SQUARE_SIZE
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if (all(board[clicked_row][j] == player for j in range(BOARD_COLS)) or
                    all(board[i][clicked_col] == player for i in range(BOARD_ROWS)) o
                    all(board[i][i] == player for i in range(BOARD_ROWS)) or
                    all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS))):
                    game_over = True
                    score[player] += 1
                elif is_board_full():
                    game_over = Tru
                player = player % 2 + 1
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = Fals
    if game_over:
        show_play_again()
    score_text = font.render(f"Player O: {score[1]}   Player X: {score[2]}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT - 100))
    pygame.display.update()