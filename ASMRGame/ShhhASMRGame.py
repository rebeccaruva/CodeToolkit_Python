# import pygame and sys module
# for exiting the window we create
import pygame, sys
import screens
from screens import titleScreen, playScreen

# import some useful constants
from pygame.locals import *

# initialize pygame and font module
pygame.init()

# declare and initialize list to hold screens and counter for list
# 0-title, 1-play, 2-end, 3-credit
screenList = ["titleScreen", "playScreen", "endScreen", "creditScreen"]
screenCounter = 0

# show title screen at game start
titleScreen()

# update display every run through, will slow down framrate if always updating
# so I placed all drawing before checking for quit
# pygame.display.update()

# will always loop
while True:
    pygame.display.update()
    # get all user events
    for event in pygame.event.get():
        # if quit, then end game and close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # debug if mousepress change screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screenCounter < len(screenList)-1:
                screenCounter += 1
                moveScreen = getattr(screens, screenList[screenCounter])
                moveScreen()
                print(screenList[screenCounter])
            else:
                screenCounter = 0
                moveScreen = getattr(screens, screenList[screenCounter])
                moveScreen()
                print(screenList[screenCounter])
                print(screenCounter)
            print ("mouse pressed at (%d, %d)" % event.pos)
