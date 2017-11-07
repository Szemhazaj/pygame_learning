import pygame, sys, time
from pygame.locals import *
pygame.init()

BLUE = ( 0, 0, 255)
GREEN = ( 0, 128, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((900, 600))
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277)))
pygame.draw.line(DISPLAYSURF, YELLOW ,(400, 0) , (400,600), 5)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 1)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
pixObj = pygame.PixelArray(DISPLAYSURF)
textRectObj = textSurfaceObj.get_rect()
textRectObj.topleft = (0, 0)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
del pixObj
pygame.display.set_caption('Hello World!')

file = 'kastenfrosch__sound3.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)


while True: # main game loop
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    
    pygame.mixer.music.play()
    time.sleep(1)
    soundObj.stop()
    for event in pygame.event.get():
        
        if event.type == QUIT: #from pygame.locals it's pygame.locals.event.type
            pygame.quit()
            sys.exit() 
    pygame.display.update()