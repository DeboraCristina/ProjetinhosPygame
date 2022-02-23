import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#configurações
larguraTela = 640
alturaTela = 480
display = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Menus')
relógio = pygame.time.Clock()

#variaveis
cor = {
    'preto': (0, 0, 0),
    'branco': (255, 255, 255),
    'cinza': (100, 100, 100),
    'azul': (0, 0, 255),
    'verde': (0, 255, 0),
    'vermelho': (255, 0, 0),
}
tela = 0

#funções
def comparaLista(listA = [0, 0], listB = [0, 0]):
    if listA[0] in listB[0] and listA[1] in listB[1]:
        return True
    else:
        return False

#objetos

#chamadas de objetos

#telas
def menuPrincipal():
    areaum = [list(range(50, 151)), list(range(200, 251))]
    areadois = [list(range(50, 151)), list(range(270, 321))]
    corum = [0, 255, 0]
    cordois = [0, 255, 255]
    corbotaoUm = corum
    corbotaoDois = corum
    while True:
        relógio.tick(60)
        display.fill(cor['preto'])

        botaoUm = pygame.draw.rect(display, corbotaoUm, (50, 200, 100, 50))
        botaoDois = pygame.draw.rect(display, corbotaoDois, (50, 270, 100, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            #vendo se o mouse passa por cima dos botões
            if event.type == MOUSEMOTION:
                if comparaLista(pygame.mouse.get_pos(), areaum):
                    corbotaoUm = cordois
                else:
                    corbotaoUm = corum
                if comparaLista(pygame.mouse.get_pos(), areadois):
                    corbotaoDois = cordois
                else:
                    corbotaoDois = corum
            #vendo se clicou em algum botão
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons = 5)[0] and comparaLista(pygame.mouse.get_pos(), areaum):
                    print('opções')
                if pygame.mouse.get_pressed(num_buttons = 5)[0] and comparaLista(pygame.mouse.get_pos(), areadois):
                    print('jogo')

                #print('tilt', pygame.mouse.set_pos)

        pygame.display.flip()

def carregaJanelas():
    global tela

    if tela == 0:
        menuPrincipal()
    elif tela == 1:
        pass
    elif tela == 2:
        pass
    elif tela == 3:
        pass
    elif tela == 4:
        pass

carregaJanelas()
