import pygame, sys
from pygame.locals import *
# Set up pygame.
pygame.init()
# Set up the window.
windowSurface = pygame.display.set_mode((1000, 500), 0, 32)
pygame.display.set_caption('Hello world!')
# Set up the colors.

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)
# Set up the text.
text = basicFont.render('puto el que lo lea', True, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
# Draw the white background onto the surface.
windowSurface.fill(WHITE)
# Draw the text's background rectangle onto the surface.
pygame.draw.rect(windowSurface, RED, (textRect.left ,textRect.top , textRect.width, textRect.height ))

# Draw the text onto the surface.
windowSurface.blit(text, textRect)
# Draw the window onto the screen.
pygame.display.update()
# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
             sys.exit()