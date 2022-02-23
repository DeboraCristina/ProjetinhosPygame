####O que tem aqui
'''
janela,
figuras,
movimentando figuras,
movimentando objetos
'''


import pygame
#importa tudo em locals
from pygame.locals import *
#'exit' vai ser chamado quando a janela for fechada
from sys import exit

from time import sleep

#inicia o pygame
pygame.init()

#muda o título da janla
pygame.display.set_caption('Janla')

#'set_mode' recebe uma tupla de 'largura' e 'altura'
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

#posições do rect
x = (largura / 2) - 25
y = (altura / 2) - 25
#velocidade do rect
vel = 5

#loop principal
while True:
    #x frame por segundo
    relogio.tick(60)

    #limpa a tela
    tela.fill((0,0,0))

    for event in pygame.event.get():
        #fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20'''


    if pygame.key.get_pressed()[K_a]:
        x -= vel
    if pygame.key.get_pressed()[K_d]:
        x += vel
    if pygame.key.get_pressed()[K_w]:
        y -= vel
    if pygame.key.get_pressed()[K_s]:
        y += vel

    #objetos recebem 'onde' 'cor' 'dimenção'
    #desenhar um retangulo. recebem 'onde' 'cor' 'x, y, larg, alt'
    pygame.draw.rect(tela, (255,0,0), (x, y, 50, 50))

    #desenhar um circulo. recebem 'onde' 'cor' 'x, y, raio'
    pygame.draw.circle(tela, (0, 255, 0), (80, 30), 10)

    #desenhar uma reta. recebem 'onde' 'cor' 'pontoA' 'pontoB' 'espessura'
    pygame.draw.line(tela, (0, 255, 255), (110, 40), (150, 40), 5)

    pygame.display.update()
