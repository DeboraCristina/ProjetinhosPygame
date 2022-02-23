import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 320
altura_tela = 240
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'azul': (0, 0, 255),
}

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Sprites')

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(2):
            self.sprites.append(pygame.image.load(f'sprite_um/{i}.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 130
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

    def update(self):
        self.atual += 0.15
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))

todasAsSprite = pygame.sprite.Group()
personagem = Personagem()
todasAsSprite.add(personagem)

img_fundo = pygame.image.load('fundo.jpg').convert()
img_fundo = pygame.transform.scale(img_fundo, (largura_tela, altura_tela))
relógio = pygame.time.Clock()

while True:
    relógio.tick(60)
    tela.fill(cor['preto'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(img_fundo, (0,0))
    todasAsSprite.draw(tela)
    todasAsSprite.update()
    pygame.display.flip()
