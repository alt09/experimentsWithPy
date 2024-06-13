import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window with a resolution of 1000x500 pixels
windowSurface = pygame.display.set_mode((1000, 500), 0, 32)

# Set the window caption
pygame.display.set_caption('Hello world!')

# Set up the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the fonts with a default system font and size 48
basicFont = pygame.font.SysFont(None, 48)

# Set up the text to be rendered
text = basicFont.render('puto el que lo lea', True, WHITE)

# Get the rectangular area of the text surface
textRect = text.get_rect()

# Center the text rectangle in the window
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill the window surface with the white color
windowSurface.fill(WHITE)

# Draw a red rectangle behind the text for better visibility
pygame.draw.rect(windowSurface, RED, (textRect.left, textRect.top, textRect.width, textRect.height))

# Blit the text onto the window surface at the text rectangle position
windowSurface.blit(text, textRect)

# Update the display to show the drawn content
pygame.display.update()

# Run the game loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # Check if the quit event is triggered
            pygame.quit()  # Quit pygame
            sys.exit()  # Exit the system
