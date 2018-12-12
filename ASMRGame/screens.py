import pygame
from assetHelp import textToScreen#, loadBG

# declare variables below
screenWidth = 605
screenHeight = 340

#animated backgrounds
#titleBG = [pygame.image.load('data/sprites/title1.png'), pygame.image.load('data/sprites/title2.png'), pygame.image.load('data/sprites/title3.png'), pygame.image.load('data/sprites/title4.png')]

# new drawing surface with width: 605 and height: 340
displaySurface = pygame.display.set_mode((screenWidth, screenHeight)) #16:9 aspect ratio
# a caption for the window
pygame.display.set_caption("Shhh...")

def titleScreen():
    #blit bg onto main surface
    titleImg = pygame.image.load('data/sprites/title1.png')
    titleImg = pygame.transform.scale(titleImg, (screenWidth, screenHeight))
    displaySurface.blit(titleImg, [0, 0])

    # blit the title onto main surface
    textToScreen(displaySurface, 'Shhh...', screenWidth/2-10, screenHeight/2)

def playScreen():
    #blit bg onto main surface
    playImg = pygame.image.load('data/sprites/awake-1.png')
    playImg = pygame.transform.scale(playImg, (screenWidth, screenHeight))
    displaySurface.blit(playImg, [0, 0])

    # blit heart onto main surface
    heartImg = pygame.image.load('data/sprites/heart.png')
    heartImg = pygame.transform.scale(heartImg, (200, 150))
    displaySurface.blit(heartImg, [0, 0])

def endScreen():
    #blit bg onto main surface
    endImg = pygame.image.load('data/sprites/sleeping.png')
    endImg = pygame.transform.scale(endImg, (screenWidth, screenHeight))
    displaySurface.blit(endImg, [0, 0])

def creditScreen():
    #blit bg onto main surface
    creditImg = pygame.image.load('data/sprites/title4.png')
    creditImg = pygame.transform.scale(creditImg, (screenWidth, screenHeight))
    displaySurface.blit(creditImg, [0, 0])

    # blit the text onto main surface
    textToScreen(displaySurface, 'made by Bex', 150, screenHeight-175)
