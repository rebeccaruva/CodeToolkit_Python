# import pygame and sys module
# for exiting the window we create
import pygame, sys
import screens
from screens import titleScreen, playScreen, endScreen, creditScreen

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

# will always loop
while True:
    #update screen
    pygame.display.update()
    # get all user events
    for event in pygame.event.get():
        # if quit, then end game and close window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # debug if mousepress change screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if mouse pressed and still running through list then change to next screen
            if screenCounter < len(screenList)-1:
                screenCounter += 1
                moveScreen = getattr(screens, screenList[screenCounter])
                moveScreen()
                print(screenList[screenCounter])
            # if mouse pressed and done with list go back to beginning of game
            else:
                screenCounter = 0
                moveScreen = getattr(screens, screenList[screenCounter])
                moveScreen()
                print(screenList[screenCounter])
                print(screenCounter)
            print ("mouse pressed at (%d, %d)" % event.pos)
