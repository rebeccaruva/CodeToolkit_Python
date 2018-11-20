# import pygame and sys module
# for exiting the window we create
import pygame, sys
from letras import textToScreen

# import some useful constants
from pygame.locals import *
# get some pi
from math import pi

# make some variables
#int checker = 0;

# initialize pygame and font module
pygame.init()

# new drawing surface with width: 300 and height: 300
displaySurface = pygame.display.set_mode((300, 300))
# a caption for the window
pygame.display.set_caption("my first game")
# new text surface to write on
# textSurface = myFont.render('hola', False, (255, 255, 255))

# add a blue square (surface, color, position&size)
pygame.draw.rect(displaySurface, (0, 0, 255), (0, 0, 50, 50))
# blit the text surface onto main screen
# displaySurface.blit(textSurface, (0, 0))
textToScreen(displaySurface, 'HOLA', 0, 0)
# arcs to make an eclipse (surface, color, area eclipse fills/rect, start angle, stop angle, width)
pygame.draw.arc(displaySurface, (255, 255, 255), (110, 75, 150, 125), 0, pi/2, 2)
pygame.draw.arc(displaySurface, (0, 255, 0), (110, 75, 150, 125), pi/2, pi, 2)
pygame.draw.arc(displaySurface, (0, 0, 255), (110, 75, 150, 125), pi,3*pi/2, 2)
pygame.draw.arc(displaySurface, (255, 0, 0),  (110, 75, 150, 125), 3*pi/2, 2*pi, 2)

# update display every run through, will slow down framrate if always updating
# so I placed all drawing before checking for quit
pygame.display.update()

# will always loop
while True:
    # get all user events
    for event in pygame.event.get():
        # if quit, then end game and close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
