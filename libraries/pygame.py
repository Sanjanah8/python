import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Pygame Drawing')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # Fill background with white
    pygame.draw.circle(screen, (0, 0, 255), (200, 150), 50)  # Draw a blue circle
    pygame.display.flip()

pygame.quit()
