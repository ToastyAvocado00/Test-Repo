import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Customized Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

player_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    if ball.y < opponent_paddle.y + opponent_paddle.height // 2:
        opponent_paddle.y -= PADDLE_SPEED
    if ball.y > opponent_paddle.y + opponent_paddle.height // 2:
        opponent_paddle.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
        PADDLE_SPEED = 7
    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    PADDLE_SPEED += 1

    SCREEN.fill(BLACK)

    pygame.draw.rect(SCREEN, WHITE, player_paddle)
    pygame.draw.rect(SCREEN, WHITE, opponent_paddle)
    pygame.draw.ellipse(SCREEN, RED, ball)

    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    SCREEN.blit(player_text, (WIDTH//4, 50))
    SCREEN.blit(opponent_text, (WIDTH*3//4, 50))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
