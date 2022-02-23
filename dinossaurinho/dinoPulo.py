#verificar por #MUDAR AKI
import pygame
import os
from pygame.locals import *
from random import randrange, choice
from sys import exit

pygame.init()
pygame.mixer.init()

largura_tela = 640
altura_tela = 480
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'ciano': (0, 130, 160)
}
diretório_principal = os.path.dirname(__file__)
diretório_imagens = os.path.join(diretório_principal, 'imagens')
diretório_sons = os.path.join(diretório_principal, 'sons')

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Dinossaurinho')

sprite_sheet = pygame.image.load(os.path.join(diretório_imagens, 'dino2.png')).convert_alpha()

somColisão = pygame.mixer.Sound(os.path.join(diretório_sons, 'death_sound.wav'))
somColisão.set_volume(1)
somPontuação = pygame.mixer.Sound(os.path.join(diretório_sons, 'score_sound.wav'))
somPontuação.set_volume(1)

colidiu = False
escolhaObstáculo = choice([0, 1])
G = 2
V = 10
alturaChão = altura_tela - 64
velocidadeCorrida = 8
pontos = 0

def reiniciarJogo():
    global colidiu, pontos, velocidadeCorrida, escolhaObstáculo
    colidiu = False
    pontos = 0
    velocidadeCorrida = 8
    escolhaObstáculo = choice([0, 1])
    voador.rect.x = largura_tela + 100
    cacto.rect.x = largura_tela + 100
    dino.pulo = False
    dino.rect.centery = alturaChão


def mostraMensagem(msg, tamFont, cor):
    fonte = pygame.font.SysFont('Pixels', tamFont, False, False)
    mensagem = fonte.render(f'{msg}', False, cor)
    return mensagem

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.somPulo = pygame.mixer.Sound(os.path.join(diretório_sons, 'jump_sound.wav'))
        self.somPulo.set_volume(1)
        self.dino_img = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.dino_img.append(img)
        self.index = 0
        self.image = self.dino_img[self.index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100, alturaChão)
        self.pulo = False
        self.vel = V

    def pular(self):
        self.pulo = True
        self.somPulo.play()

    def update(self):
        if self.pulo:
            if self.rect.y <= 260:
                self.pulo = False
            self.vel = -V
            self.rect.y += self.vel
        else:
            if self.rect.center[1] < alturaChão:
                self.vel += G
                self.rect.y += self.vel
            else:
                self.vel = V
                self.rect.center = (100, alturaChão)

        if self.index > 2:
            self.index = 0
        self.index += 0.25
        self.image = self.dino_img[int(self.index)]

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*7, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        #self.rect.center = (100, 100)
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = largura_tela - randrange(30, 300, 90)
    def update(self):
        self.rect.x -= 5
        if self.rect.topright[0] < 0:
            self.rect.y = randrange(50, 200, 50)
            self.rect.x = largura_tela-10

class Chao(pygame.sprite.Sprite):
    def __init__(self, posX):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*6, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.x = posX * 64
        self.rect.y = altura_tela - 64
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura_tela-10
        self.rect.x -= velocidadeCorrida

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32 * 5, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolhaObstáculo
        self.rect.center = (largura_tela + 100, altura_tela - 64)
    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura_tela-10
            self.rect.x -= velocidadeCorrida

class Voador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.voador_img = []
        for i in range(3, 5):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.voador_img.append(img)
        self.index = 0
        self.image = self.voador_img[self.index]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolhaObstáculo
        self.rect = self.image.get_rect()
        self.rect.center = (largura_tela + 100, 300)

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura_tela-10
            self.rect.x -= velocidadeCorrida

            if self.index > 1:
                self.index = 0
            self.index += 0.25
            self.image = self.voador_img[int(self.index)]

todasAsSprite = pygame.sprite.Group()
grupoObstaculos = pygame.sprite.Group()

dino = Dino()
todasAsSprite.add(dino)

cacto = Cacto()
todasAsSprite.add(cacto)
grupoObstaculos.add(cacto)

voador = Voador()
todasAsSprite.add(voador)
grupoObstaculos.add(voador)

for i in range(largura_tela*4//64):
    chao = Chao(i/2)
    todasAsSprite.add(chao)

for i in range(3):
    nuvem = Nuvens()
    todasAsSprite.add(nuvem)

relógio = pygame.time.Clock()

while True:
    relógio.tick(30)
    tela.fill(cor['preto'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and dino.rect.centery == altura_tela - 64 and not colidiu:
                dino.pular()
            if event.key == K_r and colidiu:
                reiniciarJogo()

    colisões = pygame.sprite.spritecollide(dino, grupoObstaculos, False, pygame.sprite.collide_mask)

    todasAsSprite.draw(tela)

    if cacto.rect.topright[0] <= 0 or voador.rect.topright[0] <= 0:
        escolhaObstáculo = choice([0, 1])
        cacto.escolha = escolhaObstáculo
        voador.escolha = escolhaObstáculo
        cacto.rect.x = largura_tela
        voador.rect.x = largura_tela

    if not colisões:
        todasAsSprite.update()
        pontos += 1
        pontuação = mostraMensagem(pontos, 80, cor['branco'])
        pontuação_centro = pontuação.get_rect()
        pontuação_centro.center = (580, 30)
    elif colisões and not colidiu:
        somColisão.play()
        colidiu = True

    #faleceu
    if colidiu:
        fimDeJogo = mostraMensagem('GAME OVER', 80, cor['branco'])
        fimDeJogo_centro = fimDeJogo.get_rect()
        fimDeJogo_centro.center = (largura_tela//2, 20)

        reiniciar = mostraMensagem('\'R\' para Reiniciar', 60, cor['branco'])
        reiniciar_centro = reiniciar.get_rect()
        reiniciar_centro.center = (largura_tela//2, (altura_tela//2)+40)

        tela.blit(fimDeJogo, fimDeJogo_centro)
        tela.blit(reiniciar, reiniciar_centro)

    if pontos%100 == 0 and not colisões:
        somPontuação.play()
        if velocidadeCorrida < 24:
            velocidadeCorrida += 2

    tela.blit(pontuação, pontuação_centro)
    pygame.display.flip()
