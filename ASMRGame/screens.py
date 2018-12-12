import pygame
from letras import textToScreen

# declare variables below
screenWidth = 605
screenHeight = 340

# new drawing surface with width: 605 and height: 340
displaySurface = pygame.display.set_mode((screenWidth, screenHeight)) #16:9 aspect ratio
# a caption for the window
pygame.display.set_caption("Shhh...")

def titleScreen():
    #blit title screen onto main surface
    titleImg = pygame.image.load('data/sprites/hackcooperasmr-title1.png')
    titleImg = pygame.transform.scale(titleImg, (screenWidth, screenHeight))
    displaySurface.blit(titleImg, [0, 0])

    # blit the text onto main surface
    textToScreen(displaySurface, 'HOLA', screenWidth/2, screenHeight/2)
