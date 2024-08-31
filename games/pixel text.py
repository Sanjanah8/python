import matplotlib.pyplot as plt
import numpy as np

def draw_pixelated_text(text, pixel_size=10):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Create a font object with matplotlib
    font_properties = {'verticalalignment': 'center', 'horizontalalignment': 'center', 'fontsize': 50}
    
    # Plot each character as a pixelated block
    for i, char in enumerate(text):
        x = i * pixel_size * 2
        y = pixel_size
        ax.text(x, y, char, fontsize=font_properties['fontsize'], ha='center', va='center', color='white', fontfamily='monospace')

    ax.set_xlim(0, len(text) * pixel_size * 2)
    ax.set_ylim(0, pixel_size * 2)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

draw_pixelated_text("Pixelated Text", pixel_size=20)
