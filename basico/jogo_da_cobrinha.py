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
pygame.mixer.music.set_volume(0)
#pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('songs/fundo.wav')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('songs/coin.wav')
som_colisao.set_volume(0.5)

#cores
cor = {
    'preto': (0, 0, 0),
    'branco': (255,255,255),
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0)
}
#posições da venenosa
x = (largura / 2) - 25
y = (altura / 2) - 25
#velocidade da venenosa
vel = 2
#tamanho do corpo da cobra
corpo_venenosa = []

#direção da cobra
x_controle = -vel
y_controle = 0

#tamanhos tanto da venenosa quanto da maça
per_tam = 20

#posição da maça
x_maça = randint(40, 600)
y_maça = randint(40, 400)

pontos = 0
morreu = False

def desenha_cobra(lista_corpo):
    for xey in lista_corpo:
        pygame.draw.rect(tela, cor['verde'], (xey[0], xey[1], per_tam, per_tam))

def reinicia():
    global pontos, x, y, x_maça, y_maça, corpo_venenosa, morreu
    pontos = 0
    x = (largura / 2) - 25
    y = (altura / 2) - 25
    corpo_venenosa = []
    x_maça = randint(40, 600)
    y_maça = randint(40, 400)
    morreu = False


while True:
    relogio.tick(60)

    tela.fill(cor['preto'])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a and x_controle == 0:
                x_controle = vel*(-1)
                y_controle = 0
            if event.key == K_d and x_controle == 0:
                x_controle = vel
                y_controle = 0
            if event.key == K_w and y_controle == 0:
                x_controle = 0
                y_controle = vel*(-1)
            if event.key == K_s and y_controle == 0:
                x_controle = 0
                y_controle = vel

    x += x_controle
    y += y_controle

    if x < 0:
        x = largura
    if x > largura:
        x = 0
    if y < 0:
        y = altura
    if y > altura:
        y = 0

    venenosa = pygame.draw.rect(tela, cor['verde'], (x, y, per_tam, per_tam))
    maça = pygame.draw.rect(tela, cor['vermelho'], (x_maça, y_maça, per_tam, per_tam))

    corpo_venenosa.append((x, y))

    if corpo_venenosa.count((x, y)) > 1:
        morreu = True
        while morreu:
            tela.fill(cor['preto'])

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reinicia()

            texto_gameOver = fonte.render('reiniciar? tecle R', True, cor['branco'])
            rect = texto_gameOver.get_rect()
            rect.center = (largura//2, altura//2)

            tela.blit(texto_gameOver, rect)
            pygame.display.update()

    desenha_cobra(corpo_venenosa)

    if len(corpo_venenosa) > pontos+50:
        corpo_venenosa.pop(0)

    if venenosa.colliderect(maça):
        x_maça = randint(40, 600)
        y_maça = randint(40, 400)
        pontos += 1
        som_colisao.play()

    tela.blit(fonte.render(f'Pontos: {pontos}', True, cor['branco']), (50, 40))
    pygame.display.update()
