import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.15)
musica = pygame.mixer.music.load('Gigakoops-Good-Grief.wav')
pygame.mixer.music.play(loops=-1)

pontuou = pygame.mixer.Sound('smw_kick.wav')


largura = 640
altura = 480
x_cobrinha = int(largura/2)
y_cobrinha = int(altura/2)

velocidade = 15
x_controle = 20
y_controle = 0


x_frutinha = randint(40, 600)
y_frutinha = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 30, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Projeto em Python - CobrinhaPy')
relogio = pygame.time.Clock()

lista_cobrinha = []
comprimento_inicial = 5

morreu = False

def cobrinha_cresce(lista_cobrinha):
    for XeY in lista_cobrinha:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobrinha, y_cobrinha, lista_cabeca, lista_cobrinha, x_frutinha, y_frutinha, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobrinha = int(largura/2)
    y_cobrinha = int(altura/2)
    lista_cobrinha = []
    lista_cabeca = []
    x_frutinha = randint(40, 600)
    y_frutinha = randint(50, 430)
    morreu = False


while True:

    relogio.tick(20)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    pontos_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0


    cobrinha = pygame.draw.rect(tela, (0, 255, 0), (x_cobrinha, y_cobrinha, 20, 20))
    frutinha = pygame.draw.rect(tela, (255, 0, 0), (x_frutinha, y_frutinha, 15, 15))

    x_cobrinha = x_cobrinha + x_controle
    y_cobrinha = y_cobrinha + y_controle


    if cobrinha.colliderect(frutinha):
        x_frutinha = randint(40, 600)
        y_frutinha = randint(50, 430)
        pontos = pontos + 1
        pontuou.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobrinha)
    lista_cabeca.append(y_cobrinha)

    lista_cobrinha.append(lista_cabeca)


    if lista_cobrinha.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Aperte R para jogar de novo.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        fonte3 = pygame.font.SysFont('arial', 10, True, False)
        mensagem2 = 'Desenvolvido por: Fábio Vaz e Iohana Salvador!'
        formatado_texto = fonte3.render(mensagem2, True, (255,0,0))
        retangulo_texto = formatado_texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            

            retangulo_texto.center = (150, 20)
            tela.blit(formatado_texto, retangulo_texto)            
            pygame.display.update()

    if x_cobrinha > largura:

        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Aperte R para jogar de novo.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        fonte3 = pygame.font.SysFont('arial', 10, True, False)
        mensagem2 = 'Desenvolvido por: Fábio Vaz e Iohana Salvador!'
        formatado_texto = fonte3.render(mensagem2, True, (255,0,0))
        retangulo_texto = formatado_texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            

            retangulo_texto.center = (150, 20)
            tela.blit(formatado_texto, retangulo_texto)            
            pygame.display.update()

    if x_cobrinha < 0:

        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Aperte R para jogar de novo.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        fonte3 = pygame.font.SysFont('arial', 10, True, False)
        mensagem2 = 'Desenvolvido por: Fábio Vaz e Iohana Salvador!'
        formatado_texto = fonte3.render(mensagem2, True, (255,0,0))
        retangulo_texto = formatado_texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            

            retangulo_texto.center = (150, 20)
            tela.blit(formatado_texto, retangulo_texto)            
            pygame.display.update()

    if y_cobrinha < 0:

        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Aperte R para jogar de novo.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        fonte3 = pygame.font.SysFont('arial', 10, True, False)
        mensagem2 = 'Desenvolvido por: Fábio Vaz e Iohana Salvador!'
        formatado_texto = fonte3.render(mensagem2, True, (255,0,0))
        retangulo_texto = formatado_texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            

            retangulo_texto.center = (150, 20)
            tela.blit(formatado_texto, retangulo_texto)            
            pygame.display.update()

    if y_cobrinha > altura:

        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Aperte R para jogar de novo.'
        texto_formatado = fonte2.render(mensagem, True, (255,255,255))
        ret_texto = texto_formatado.get_rect()

        fonte3 = pygame.font.SysFont('arial', 10, True, False)
        mensagem2 = 'Desenvolvido por: Fábio Vaz e Iohana Salvador!'
        formatado_texto = fonte3.render(mensagem2, True, (255,0,0))
        retangulo_texto = formatado_texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            

            retangulo_texto.center = (150, 20)
            tela.blit(formatado_texto, retangulo_texto)            
            pygame.display.update()

    if len(lista_cobrinha) > comprimento_inicial:
        del lista_cobrinha[0]

    cobrinha_cresce(lista_cobrinha)

    tela.blit(pontos_formatado, (480, 0))
    pygame.display.update()