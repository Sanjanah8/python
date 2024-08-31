import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

width = 600
height = 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Memory Puzzle')

clock = pygame.time.Clock()
card_width = 100
card_height = 100
card_gap = 10
cards = [(i // 2) + 1 for i in range(16)]
random.shuffle(cards)

def draw_card(x, y, number, show):
    pygame.draw.rect(dis, green, [x, y, card_width, card_height])
    if show:
        font = pygame.font.SysFont(None, 55)
        text = font.render(str(number), True, black)
        dis.blit(text, [x + card_width // 3, y + card_height // 3])

def memory_puzzle_game():
    revealed = [[False for _ in range(4)] for _ in range(4)]
    first_card = None
    second_card = None
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= (card_width + card_gap)
                y //= (card_height + card_gap)
                if not revealed[x][y]:
                    if first_card is None:
                        first_card = (x, y)
                    elif second_card is None:
                        second_card = (x, y)
                        if cards[first_card[0] * 4 + first_card[1]] == cards[second_card[0] * 4 + second_card[1]]:
                            revealed[first_card[0]][first_card[1]] = True
                            revealed[second_card[0]][second_card[1]] = True
                        else:
                            pygame.time.wait(500)
                        first_card = None
                        second_card = None

        dis.fill(black)
        for x in range(4):
            for y in range(4):
                draw_card(x * (card_width + card_gap), y * (card_height + card_gap), cards[x * 4 + y], revealed[x][y] or (first_card == (x, y) or second_card == (x, y)))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

memory_puzzle_game()
