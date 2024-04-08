import colorsys
import pygame
import random

pygame.init()

HEIGHT: int
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Customized Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (148, 0, 211)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 2.5

BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

background_colors = [BLACK, BLUE, GREEN, PURPLE, ORANGE, PINK, CYAN]
current_color_index = 0
color_change_interval = 500
frame_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_y = pygame.mouse.get_pos()[1]

    player_paddle.y = mouse_y - PADDLE_HEIGHT // 2
    if player_paddle.top < 0:
        player_paddle.top = 0
    if player_paddle.bottom > HEIGHT:
        player_paddle.bottom = HEIGHT

    opponent_paddle.y = ball.y - PADDLE_HEIGHT // 2
    if opponent_paddle.top < 0:
        opponent_paddle.top = 0
    if opponent_paddle.bottom > HEIGHT:
        opponent_paddle.bottom = HEIGHT

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
        PADDLE_SPEED = 7
    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    PADDLE_SPEED += 1

    hue = (frame_count % 360) / 360.0
    ball_color = colorsys.hsv_to_rgb(hue, 1, 1)
    ball_color = (int(ball_color[0] * 255), int(ball_color[1] * 255), int(ball_color[2] * 255))

    frame_count += 1
    if frame_count >= color_change_interval:
        frame_count = 0
        current_color_index = (current_color_index + 1) % len(background_colors)

    SCREEN.fill(background_colors[current_color_index])

    pygame.draw.rect(SCREEN, WHITE, player_paddle)
    pygame.draw.rect(SCREEN, WHITE, opponent_paddle)
    pygame.draw.ellipse(SCREEN, ball_color, ball)

    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    SCREEN.blit(player_text, (WIDTH // 4, 50))
    SCREEN.blit(opponent_text, (WIDTH * 3 // 4, 50))

    if game_over:
        winner_text = font.render("Player 1 Wins!" if player_score == winning_score else "Player 2 Wins!", True, WHITE)
        SCREEN.blit(winner_text, (WIDTH // 2 - 120, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)  # Pause for 2 seconds before quitting
        break

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
