import pygame
from pygame.locals import *
from sys import exit
from PIL import Image

pygame.init()

#definições
dimensãoTela = (640, 480)
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0),
}
tela = pygame.display.set_mode(dimensãoTela)
pygame.display.set_caption('Criando Chão')
relógio = pygame.time.Clock()

fase = Image.open('img/faseteste.png')
fasePaleta = []
for c in fase.getdata():
    fasePaleta.append(c)
conrvert = []
coresDeConversão = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'ciano': (0, 255, 255),
    'black': (0, 0, 0),
}
for c in fasePaleta:
    if c[3] != 0:
        if c[0:3] == coresDeConversão['red']:
            conrvert.append('terra')
        if c[0:3] == coresDeConversão['blue']:
            conrvert.append('aki')
        if c[0:3] == coresDeConversão['green']:
            conrvert.append('grama')
        if c[0:3] == coresDeConversão['black']:
            conrvert.append('aki')
        if c[0:3] == coresDeConversão['ciano']:
            conrvert.append('player')
    else:
        conrvert.append('none')
tabela = []
for i in range(0, len(conrvert), 20):
    tabela.append(list(conrvert[i: i+20]))

#variaveis

#funções

#objetos
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/ani_01.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Terra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/traz.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

class Grama(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/frente.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#grupos
todasAsSprites = pygame.sprite.Group()
paredesEchao = pygame.sprite.Group()

#chamadas
for linha in range(0, len(tabela)):
    for coluna in range(0, len(tabela[linha])):
        if tabela[linha][coluna] != 'none':
            if tabela[linha][coluna] == 'grama':
                grama = Grama(coluna*32, linha*32)
                todasAsSprites.add(grama)
                paredesEchao.add(grama)
            if tabela[linha][coluna] == 'terra':
                terra = Terra(coluna*32, linha*32)
                todasAsSprites.add(terra)
                paredesEchao.add(terra)
            if tabela[linha][coluna] == 'player':
                player = Player(coluna*32, linha*32)
                todasAsSprites.add(player)

while True:
    relógio.tick(60)
    tela.fill(cor['preto'])
    for event in pygame.event.get():
        evento = event.type
        if evento == QUIT:
            pygame.quit()
            exit()
        if evento == KEYDOWN:
            if event.key == K_SPACE and colidiu:
                player.rect.y -= 20

    colidiu = pygame.sprite.spritecollide(player, paredesEchao, False)
    if not colidiu:
        player.rect.y += 10
    if pygame.key.get_pressed()[K_LEFT]:
        player.rect.x -= 10
    if pygame.key.get_pressed()[K_RIGHT]:
        player.rect.x += 10

    todasAsSprites.draw(tela)
    todasAsSprites.update()
    pygame.display.flip()
