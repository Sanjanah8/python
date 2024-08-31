import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)

width = 800
height = 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

clock = pygame.time.Clock()
player_width = 50
player_height = 30
enemy_width = 50
enemy_height = 30
bullet_width = 5
bullet_height = 10
player_speed = 5
bullet_speed = 7
enemy_speed = 3

def draw_player(x, y):
    pygame.draw.rect(dis, white, [x, y, player_width, player_height])

def draw_enemy(x, y):
    pygame.draw.rect(dis, red, [x, y, enemy_width, enemy_height])

def draw_bullet(x, y):
    pygame.draw.rect(dis, green, [x, y, bullet_width, bullet_height])

def space_invaders_game():
    game_over = False

    player_x = width // 2 - player_width // 2
    player_y = height - player_height - 10

    bullet_x = player_x + player_width // 2 - bullet_width // 2
    bullet_y = player_y - bullet_height
    bullet_fired = False

    enemies = []
    for i in range(5):
        for j in range(6):
            enemies.append(pygame.Rect(i * (enemy_width + 10), j * (enemy_height + 10), enemy_width, enemy_height))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE] and not bullet_fired:
            bullet_x = player_x + player_width // 2 - bullet_width // 2
            bullet_y = player_y - bullet_height
            bullet_fired = True

        if bullet_fired:
            bullet_y -= bullet_speed
            if bullet_y < 0:
                bullet_fired = False

        for enemy in enemies:
            if pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height).colliderect(enemy):
                enemies.remove(enemy)
                bullet_fired = False
                bullet_y = player_y - bullet_height
                break

        dis.fill(black)
        draw_player(player_x, player_y)
        if bullet_fired:
            draw_bullet(bullet_x, bullet_y)
        for enemy in enemies:
            draw_enemy(enemy.x, enemy.y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

space_invaders_game()
