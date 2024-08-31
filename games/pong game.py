import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

clock = pygame.time.Clock()
paddle_width = 15
paddle_height = 60
ball_size = 15
paddle_speed = 10
ball_speed = 7

def draw_paddle(x, y):
    pygame.draw.rect(dis, white, [x, y, paddle_width, paddle_height])

def draw_ball(x, y):
    pygame.draw.circle(dis, white, [x, y], ball_size)

def pong_game():
    game_over = False

    # Paddle positions
    player1_x = 10
    player1_y = height // 2 - paddle_height // 2
    player2_x = width - paddle_width - 10
    player2_y = height // 2 - paddle_height // 2

    # Ball position and speed
    ball_x = width // 2
    ball_y = height // 2
    ball_x_speed = ball_speed
    ball_y_speed = ball_speed

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= paddle_speed
        if keys[pygame.K_s] and player1_y < height - paddle_height:
            player1_y += paddle_speed
        if keys[pygame.K_UP] and player2_y > 0:
            player2_y -= paddle_speed
        if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
            player2_y += paddle_speed

        ball_x += ball_x_speed
        ball_y += ball_y_speed

        if ball_y <= 0 or ball_y >= height:
            ball_y_speed = -ball_y_speed
        if ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height:
            ball_x_speed = -ball_x_speed
        if ball_x >= player2_x - ball_size and player2_y < ball_y < player2_y + paddle_height:
            ball_x_speed = -ball_x_speed

        if ball_x < 0 or ball_x > width:
            ball_x = width // 2
            ball_y = height // 2
            ball_x_speed = -ball_x_speed

        dis.fill(black)
        draw_paddle(player1_x, player1_y)
        draw_paddle(player2_x, player2_y)
        draw_ball(ball_x, ball_y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

pong_game()
