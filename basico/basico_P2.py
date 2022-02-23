####O que tem aqui
'''
colisões
textos na tela
musicas
sons
'''


import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()

pygame.display.set_caption('Janla')

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()
#SysFont -> 'nome da fonte' 'tamanho' 'negrito [bool]' 'itálico [bool]'
fonte = pygame.font.SysFont('lato', 40, True, False)

#sons
pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('songs/fundo.wav')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('songs/coin.wav')
som_colisao.set_volume(0.5)

#posições do quad_vermelho
x = (largura / 2) - 25
y = (altura / 2) - 25
#velocidade do quad_vermelho
vel = 5

#posição do quad_azul
x_azul = randint(40, 600)
y_azul = randint(40, 400)

pontos = 0

#loop principal
while True:
    relogio.tick(60)

    tela.fill((0,0,0))

    mensagem =  f'Pontos: {pontos}'
    #render -> 'texto' 'anti-aling [bool]'(texto mais pixelado ou não) 'cor'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x -= vel
    if pygame.key.get_pressed()[K_d]:
        x += vel
    if pygame.key.get_pressed()[K_w]:
        y -= vel
    if pygame.key.get_pressed()[K_s]:
        y += vel

    quad_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 50, 50))
    quad_azul = pygame.draw.rect(tela, (0,255,255), (x_azul, y_azul, 50, 50))

    if quad_vermelho.colliderect(quad_azul):
        x_azul = randint(40, 600)
        y_azul = randint(40, 400)
        pontos += 1
        som_colisao.play()

    #blit -> 'texto' 'x e y'
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()
