!apt-get install -y python3-pygame
!apt-get install -y xvfb x11-utils
!pip install pygame

import pygame
import os
import numpy as np
from matplotlib import pyplot as plt

os.environ["DISPLAY"] = ":1"

pygame.init()

width, height = 800, 600
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
font_size = 20
pixel_size = 10

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pixelated Text Example')

def render_pixelated_text(text, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_array = pygame.surfarray.array3d(text_surface)
    
    text_width, text_height = text_surface.get_size()
    
    pixelated_surface = pygame.Surface((text_width * pixel_size, text_height * pixel_size))
    
    for row in range(0, text_height):
        for col in range(0, text_width):
            color = text_array[col, row]
            pygame.draw.rect(pixelated_surface, color, 
                             (col * pixel_size, row * pixel_size, pixel_size, pixel_size))
    
    return pixelated_surface

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        dis.fill(bg_color)
        
        text = "Pixelated Text"
        text_width, text_height = pygame.font.Font(None, font_size).size(text)
        x = (width - text_width * pixel_size) // 2
        y = (height - text_height * pixel_size) // 2
        pixelated_surface = render_pixelated_text(text, x, y)
        
        dis.blit(pixelated_surface, (x, y))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
