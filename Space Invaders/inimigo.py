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

def kill(listaProjeteis,matrizDeInimigos,score,linha,dificuldade, escudo1, escudo2, escudo3):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                    if (projetil.collided(inimigo[0])) and dificuldade == 1:
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                score+=30
                            elif k==linha-1:
                                score+=10
                            else:
                                score+=20
                    if (projetil.collided(inimigo[0])) and dificuldade == 2:
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                score+=40
                            elif k==linha-1:
                                score+=20
                            else:
                                score+=30
                    if (projetil.collided(inimigo[0])) and dificuldade == 3:
                        listaProjeteis.pop(j)
                        linhaDeInimigos[i]=(inimigo[0],inimigo[1]-1)
                        if linhaDeInimigos[i][1]<=0:
                            linhaDeInimigos.pop(i)
                            if k==0:
                                score+=50
                            elif k==linha-1:
                                score+=30
                            else:
                                score+=40
                    if (projetil.collided(escudo1) or projetil.collided(escudo2) or projetil.collided(escudo3)):
                        listaProjeteis.pop(j)                                                              
    return score

def hit(vidas,player,listaDeInimigos,listaProjeteisInimigos,score):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vidas-=1    
    return vidas

def hite1(listaProjeteisInimigos, escudo1, vidase1):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(escudo1)):
            listaProjeteisInimigos.pop(i)
            vidase1-=1    
    return vidase1

def hite2(listaProjeteisInimigos, escudo2, vidase2):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(escudo2)):
            listaProjeteisInimigos.pop(i)
            vidase2-=1    
    return vidase2

def hite3(listaProjeteisInimigos, escudo3, vidase3):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(escudo3)):
            listaProjeteisInimigos.pop(i)
            vidase3-=1    
    return vidase3