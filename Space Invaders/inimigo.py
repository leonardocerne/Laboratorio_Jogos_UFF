from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*
import random

def spawn(linha,matrizDeInimigos):    
    for i in range(linha):
        linhas = []
        for j in range(10):
            if linha<6:
                alien = Sprite("assets\\inimigo.png")
            alien.x = 80 * j
            alien.y = 55 * i
            linhas.append((alien,1))
        matrizDeInimigos.append(linhas)
    
    i = random.randint(0,linha-1)
    j = random.randint(0,9)
    matrizDeInimigos[i][j][0].x = 80 * j
    matrizDeInimigos[i][j][0].y = 55 * i

def draw(matrizDeInimigos):
    for linha in range(len(matrizDeInimigos)-1,-1,-1):
        for alien in matrizDeInimigos[linha]:
            alien[0].draw()

def moveInimigos(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j[0].x += movimentoInimigo*janela.delta_time()
            if ((j[0].x >= janela.width - j[0].width - 5) or (j[0].x<-5)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j[0].x += movimentoInimigo*janela.delta_time()
                j[0].y += 30
    return movimentoInimigo
