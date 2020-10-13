import pygame
from pygame.locals import *

pygame.init()
done = False

screen = pygame.display.set_mode((640,480))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            done = True
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0),(320,240),25)
    pygame.display.update()
pygame.quit()