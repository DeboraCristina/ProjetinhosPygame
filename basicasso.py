import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#variaveis
dimensãoTela = (640, 480)
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0),
}

#definições
tela = pygame.display.set_mode(dimensãoTela)
pygame.display.set_caption('Sprites')
relógio = pygame.time.Clock()

#funções

#objetos
class objeto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass
    def update(self):
        pass

#grupos

#chamadas

#jogo
while True:
    relógio.tick(60)
    tela.fill(cor['preto'])

    #eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #updates e desenhos
    pygame.display.flip()
