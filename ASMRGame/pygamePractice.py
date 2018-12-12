# import pygame and sys module
# for exiting the window we create
import pygame, sys
import screens
from screens import titleScreen

# import some useful constants
from pygame.locals import *

# initialize pygame and font module
pygame.init()

titleScreen()

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
