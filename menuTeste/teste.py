import pygame
from pygame.locals import *
from sys import exit

pygame.init()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Sprites')
relógio = pygame.time.Clock()
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0),
}

print()
print()
while True:
    relógio.tick(60)
    tela.fill(cor['preto'])
    for event in pygame.event.get():
        if event.type == QUIT:
            print('sair')
            exit()
        if event.type == MOUSEBUTTONDOWN:
            print('MOUSE')

#print(event)

    pygame.display.flip()

print()
print()
print('rodou')
