import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('gravidade')

tempo = pygame.time.Clock()

acelaração_y = 0
acelaração_x = 0
posição = [100, 100]
gravidade = 5

while True:
    tempo.tick(30)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            acelaração_y = -5

    T = tempo.get_time()/1000

    F = gravidade*T
    acelaração_y += F

    posição[1] += acelaração_y

    pygame.draw.rect(tela, (255, 0, 0), (posição[0], posição[1], 50, 50))

    if posição[1] > 400:
        posição[1] = 400
        acelaração_y = 0
        tempo = pygame.time.Clock()

    pygame.display.update()
