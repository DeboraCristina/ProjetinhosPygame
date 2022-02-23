import pygame
from pygame.locals import *
from sys import exit
from PIL import Image

pygame.init()

#variaveis
dimensãoTela = (1204, 832)
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0),
    'céu': (146, 244, 255),
}

playerImage = pygame.image.load('img/ani_01.png')
andandoPraDireita = False
andandoPraEsquerda = False
playerCoordinates = [50, 50]
player_y_momentum = 0 #impulso vertical (aceleração)
playerRect = pygame.Rect(playerCoordinates[0], playerCoordinates[1], playerImage.get_width(), playerImage.get_height())
testeRect = pygame.Rect(100, 100, 100, 50)

dirt_img = pygame.image.load('img/frente.png')
grass_img = pygame.image.load('img/traz.png')

#fase
fase = Image.open('img/faseteste.png')
fasePaleta = []
for c in fase.getdata():
    fasePaleta.append(c)
conrvert = []
coresDeConversão = {
    'red': (255, 0, 0, 255),
    'blue': (0, 0, 255, 255),
    'green': (0, 255, 0, 255),
    'ciano': (0, 255, 255, 255),
    'black': (0, 0, 0, 255),
}
for c in fasePaleta:
    if c == coresDeConversão['black']:
        conrvert.append('0')
    else:
        if c == coresDeConversão['red']:
            conrvert.append('1')
        if c == coresDeConversão['green']:
            conrvert.append('2')
        if c == coresDeConversão['blue']:
            conrvert.append('azul')
        if c == coresDeConversão['ciano']:
            conrvert.append('aki')
tabela = []
for i in range(0, len(conrvert), 19):
    tabela.append(list(conrvert[i: i+19]))

#definições
tela = pygame.display.set_mode(dimensãoTela)
display = pygame.Surface((608, 416))
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
    display.fill(cor['céu'])
    for linha in range(0, len(tabela)):
        for coluna in range(0, len(tabela[linha])):
            cel = tabela[linha][coluna]
            if cel == '1':
                display.blit(dirt_img, (coluna * 32, linha * 32))
            elif cel == '2':
                display.blit(grass_img, (coluna * 32, linha * 32))

    display.blit(playerImage, playerCoordinates)

    #player_y_momentum += 0.2
    playerCoordinates[1] += player_y_momentum

    if andandoPraDireita:
        playerCoordinates[0] += 4
    if andandoPraEsquerda:
        playerCoordinates[0] -= 4

    playerRect.x = playerCoordinates[0]
    playerRect.y = playerCoordinates[1]

    for event in pygame.event.get():
        evento = event.type
        if evento == QUIT:
            pygame.quit()
            exit()
        if evento == KEYDOWN:
            if event.key == K_RIGHT:
                andandoPraDireita = True
            if event.key == K_LEFT:
                andandoPraEsquerda = True
        if evento == KEYUP:
            if event.key == K_RIGHT:
                andandoPraDireita = False
            if event.key == K_LEFT:
                andandoPraEsquerda = False

    surf = pygame.transform.scale(display, dimensãoTela)
    tela.blit(surf, (0,0))
    pygame.display.flip()
    relógio.tick(60)
