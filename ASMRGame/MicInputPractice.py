import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

r.recognize_google()


# # import pygame and sys module
# # for exiting the window we create
# import pygame, sys
# from letras import textToScreen
#
# # import some useful constants
# from pygame.locals import *
#
# # initialize pygame and font module
# pygame.init()
#
# # new drawing surface with width: 300 and height: 300
# displaySurface = pygame.display.set_mode((300, 300))
# # a caption for the window
# pygame.display.set_caption("my first game")
#
# # text on screen to be changed
# textToScreen(displaySurface, 'HOLA', 0, 0)
#
# # update display every run through, will slow down framrate if always updating
# # so I placed all drawing before checking for quit
# pygame.display.update()
#
# # will always loop
# while True:
#     # get all user events
#     for event in pygame.event.get():
#         # if quit, then end game and close window
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
