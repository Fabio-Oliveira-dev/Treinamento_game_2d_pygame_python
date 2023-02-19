#biblioteca
# Importar uma função de fechar a janela que esta dentro do modulo sys
# Sortear vcalores aleatorios
from random import randint
from sys import exit

import pygame
# Submodulo dentro da biblioteca pygame com as constantes e funções
from pygame.locals import *

# Inicializar todas as funções e variaveis da biblioteca pygame
pygame.init()

# Objeto que vai ser a tela. Largura e altura
largura = 640
altura = 480
x = largura/2
y = altura/2

# Variaveis que vão representar x e y do retangulo verde
x_verde = randint(40,600)
y_verde = randint(50,430)

fonte = pygame.font.SysFont('verdana', 30, True, False) # Definição de fonte. Fonte, tamanho da fonte, negrito, italico
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game BR City')
velocidade = pygame.time.Clock() # Controlar a velocidade do objeto


# Loop principal do jogo
while True:
    velocidade.tick(60) # Velocidade dos frames, medidos em frames por segundos
    tela.fill((0,0,0)) # Preencher de preto a cada iteração de incremento da veriavel y
    mensagem = f'Pontuação: {pontos}' # Pontuação
    texto_formatado = fonte.render(mensagem, True, (255,255,255)) # O parametro antialaise controla o serrilhamento do texto

    # For para detectar toda vez que um evento ocorre 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        '''
        # Condição que vai reconhecer um comando dado pelo teclado. Dar movimento livre ao meu objeto
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
        if event.type == KEYDOWN:
            if event.key == K_d:
                x = x + 20
        if event.type == KEYDOWN:
            if event.key == K_w:
                y = y - 20
        if event.type == KEYDOWN:
            if event.key == K_s:
                y = y + 20'''

    # Condição de movimentação com tecla pressionada pelo usuario
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    # fazer o desenho retangulo na tela. x,y, largura e altura
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_verde = pygame.draw.rect(tela, (0,255,0), (x_verde,y_verde,40,50))
    #Desenhar um circulo x,y,raio
    #pygame.draw.circle(tela, (0,255,0), (300,260), 40)
    # Desenhar uma linha posição inicial e posisão onde termina a linha x e y e espessura
    #pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5)
    
    '''
    # para repetir o movimento de y
    if y >= altura:
        y = 0
    y += 1 # Incremento da variavel para dar movimento ao objeto
    '''

    # metodo de sobreposição de objetos para simular colisão
    if ret_vermelho.colliderect(ret_verde):
        x_verde = randint(40,600)
        y_verde = randint(50,430)
        pontos += 1

    tela.blit(texto_formatado, (340,30)) # x e y. Para exibir o texto na tela

    pygame.display.update() # Acada iteração do jogador com o jogo, a tela é atualiza
