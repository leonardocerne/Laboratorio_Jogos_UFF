from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from pygame import mixer
import time
import inimigo
import tiro
import ranking

def jogo(vidas, velplayer, delayest, delayInimigo , velprojetil, velprojetilinimigo, velinimigo, linha, dificuldade):
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("JOGO SPACE INVADERS LEONARDO BRASIL")
    teclado = janela.get_keyboard()
    player = Sprite("assets\\player.png")
    player.set_position((janela.width - player.width)/2, (janela.height - player.height) - 20)
    listaProjeteisInimigos = []
    listaProjeteis = []
    matrizDeInimigos = []
    delayinvencivel = 0
    tempoInicial = time.time()
    fps = 60
    clock = pygame.time.Clock()
    delay = delayest
    score = 0
    dano = False
    fase = 1
    while True:
        tempoAtual = time.time()
        deltaTime = tempoAtual - tempoInicial
        tempoInicial = tempoAtual
        fundo.draw()
        clock.tick(fps)
        if teclado.key_pressed("esc"):
            import menu
            menu.MainMenu()
        
        # movimento do player

        if (teclado.key_pressed("right")) and (player.x < janela.width - player.width):
            player.x += velplayer * deltaTime
        if (teclado.key_pressed("left")) and (player.x > 0):
            player.x -= velplayer * deltaTime
        
        # projeteis do player
        if (teclado.key_pressed("SPACE") and delay==0):
            tiro.criaProjNave(player,listaProjeteis)
        
        # inimigos
        if (len(matrizDeInimigos)==0):
            inimigo.spawn(linha, matrizDeInimigos)
        
        # projeteis dos inimigos
        if (delayInimigo==0):
            for i in matrizDeInimigos:
                for j in i:
                    tiro.criaProjInimigo(j,listaProjeteisInimigos)
            delayInimigo = tiro.delayInimigo(delayInimigo,linha)
        
        # desenho os tiros

        tiro.tiroPlayer(janela,listaProjeteis,velprojetil)
        tiro.tiroInimigo(janela,listaProjeteisInimigos,velprojetilinimigo)
        
        # verifico se o player já matou todos os inimigos

        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio and fase < 3:
            matrizDeInimigos.clear()
            fase += 1
            velinimigo *= 1.03
            velprojetilinimigo *= 1.03
            inimigo.spawn(linha, matrizDeInimigos)
        
        if vazio and fase == 3:
            ranking.youwin(score)

        # aplico o delay nos tiros
        if delay>=0:
            delay-=1
        if delay < 0:
            delay = delayest
        if delayInimigo>0:
            delayInimigo-=1

        # ajusto o tempo que o player fica invencivel

        if delayinvencivel>0:
            delayinvencivel-=1
            if((0 <= delayinvencivel <= 30) or (40 <= delayinvencivel <= 70) or (80 <= delayinvencivel <= 110) or (120 <= delayinvencivel <= 150) or (160 <= delayinvencivel <= 180)):
                player.draw()
        else:
            player.draw()
        
        # verifico se o player tomou dano

        vidastmp = vidas
        if (vidas>0 and delayinvencivel==0):
            for i in matrizDeInimigos:
                vidas = inimigo.hit(vidas, player, i, listaProjeteisInimigos,score)
                if vidas != vidastmp:
                    dano=True
        if dano:
            player.x= janela.width/2-player.width/2
            delayinvencivel=180
            dano=False

        # verifico se o player perdeu 

        if (vidas <= 0):
            ranking.gameover(score) 
        for i in range(len(matrizDeInimigos)-1,-1,-1):
            for j in matrizDeInimigos[i]:
                if j[0].collided(player) or j[0].y>=player.y:
                    ranking.gameover(score)
        velinimigo = inimigo.moveInimigos(janela, matrizDeInimigos, velinimigo)

        # incremento a pontuação a cada kill do player

        score = inimigo.kill(listaProjeteis,matrizDeInimigos,score,linha, dificuldade)
        # desenho os inimigos e todas as informações da tela
        
        inimigo.draw(matrizDeInimigos)
        janela.draw_text("SCORE: ", 20, 10, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), 100, 10, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(int(clock.get_fps())), janela.width-50, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Vidas: "), 20, 40, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(vidas), 90, 40, size=20, font_name="Arial", bold=True,color=[255, 0, 0])
        janela.update()
