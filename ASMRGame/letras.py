import pygame

def textToScreen(screen, text, x, y, size = 50,
            color = (255, 255, 255), fontType = 'data/fonts/Quicksand_Light.otf'):
    try:
        text = str(text)
        font = pygame.font.Font(fontType, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except Exception as e:
        print ('Font Error TT')
        raise e
