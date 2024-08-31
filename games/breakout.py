import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

width = 800
height = 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Breakout Game')

clock = pygame.time.Clock()
paddle_width = 100
paddle_height = 15
ball_size = 10
brick_width = 60
brick_height = 20
paddle_speed = 15
ball_speed = 5

def draw_paddle(x, y):
    pygame.draw.rect(dis, white, [x, y, paddle_width, paddle_height])

def draw_ball(x, y):
    pygame.draw.circle(dis, white, [x, y], ball_size)

def draw_brick(x, y):
    pygame.draw.rect(dis, red, [x, y, brick_width, brick_height])

def breakout_game():
    game_over = False

    paddle_x = width // 2 - paddle_width // 2
    paddle_y = height - paddle_height - 10

    ball_x = width // 2
    ball_y = height - paddle_height - 30
    ball_x_speed = ball_speed
    ball_y_speed = -ball_speed

    bricks = []
    for i in range(0, width, brick_width + 10):
        for j in range(0, height // 3, brick_height + 10):
            bricks.append(pygame.Rect(i, j, brick_width, brick_height))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
            paddle_x += paddle_speed

        ball_x += ball_x_speed
        ball_y += ball_y_speed

        if ball_x <= 0 or ball_x >= width:
            ball_x_speed = -ball_x_speed
        if ball_y <= 0:
            ball_y_speed = -ball_y_speed
        if ball_y >= height:
            game_over = True

        if paddle_y < ball_y + ball_size < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
            ball_y_speed = -ball_y_speed

        ball_rect = pygame.Rect(ball_x - ball_size, ball_y - ball_size, ball_size * 2, ball_size * 2)
        for brick in bricks[:]:
            if brick.colliderect(ball_rect):
                bricks.remove(brick)
                ball_y_speed = -ball_y_speed
                break

        dis.fill(black)
        draw_paddle(paddle_x, paddle_y)
        draw_ball(ball_x, ball_y)
        for brick in bricks:
            draw_brick(brick.x, brick.y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

breakout_game()
