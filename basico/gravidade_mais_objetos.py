import pygame
from pygame.locals import *
from sys import exit
from random import randint

'''
    if pygame.key.get_pressed()[K_a]:
        x -= vel
    if pygame.key.get_pressed()[K_d]:
        x += vel
    if pygame.key.get_pressed()[K_w]:
        y -= vel
    if pygame.key.get_pressed()[K_s]:
        y += vel
'''

pygame.init()

pygame.display.set_caption('Janla')

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

tempo = pygame.time.Clock()

cor = {
    'vermelha': [255, 0, 0],
    'cinza': [100, 100, 100]
}

posição = [100, 100]
aceleraçãoY = 0
G = 10

class Play(pygame.sprite.Sprite):
    def __init__(self, posição):
        pygame.sprite.Sprite.__init__(self)
        self.posiçãoX = posição[0]
        self.posiçãoY = posição[1]
        self.image = pygame.image.load('sprites/attack_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = posição
    def update(self):
        self.rect.center = posição

sprites = pygame.sprite.Group()

per = Play(posição)
sprites.add(per)

while True:
    tempo.tick(60)

    tela.fill(cor['cinza'])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            aceleraçãoY = -5

    T = tempo.get_time()/1000
    F = G * T
    aceleraçãoY += F
    posição[1] += aceleraçãoY

    pygame.draw.rect(tela, cor['vermelha'], (posição[0], posição[1], 50, 50))

    if posição[1] > 400:
        posição[1] = 400
        aceleraçãoY = 0
        tempo = pygame.time.Clock()

    sprites.draw(tela)
    sprites.update()
    pygame.display.update()
