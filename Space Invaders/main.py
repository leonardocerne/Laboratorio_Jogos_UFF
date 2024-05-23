from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from pygame import mixer
import time
import inimigo
import tiro

def jogo(velplayer, delayest , velprojetil, velinimigo, linha):
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("JOGO SPACE INVADERS LEONARDO BRASIL")
    teclado = janela.get_keyboard()
    player = Sprite("assets\\player.png")
    player.set_position((janela.width - player.width)/2, (janela.height - player.height) - 20)
    listaProjeteis = []
    matrizDeInimigos = []
    tempoInicial = time.time()
    fps = 60
    clock = pygame.time.Clock()
    delay = delayest
    score = 0
    while True:
        tempoAtual = time.time()
        deltaTime = tempoAtual - tempoInicial
        tempoInicial = tempoAtual
        fundo.draw()
        clock.tick(fps)
        if teclado.key_pressed("esc"):
            import menu
            menu.MainMenu()
        if (teclado.key_pressed("right")) and (player.x < janela.width - player.width):
            player.x += velplayer * deltaTime
        if (teclado.key_pressed("left")) and (player.x > 0):
            player.x -= velplayer * deltaTime
        if (teclado.key_pressed("SPACE") and delay==0):
            tiro.criaProjNave(player,listaProjeteis)
        tiro.tiroPlayer(janela,listaProjeteis,velprojetil)
        if (len(matrizDeInimigos)==0):
            inimigo.spawn(linha, matrizDeInimigos)

        for i in matrizDeInimigos:
            if (len(i)==0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:
            youwin(score)

        for i in range(len(matrizDeInimigos)-1,-1,-1):
            for j in matrizDeInimigos[i]:
                if j[0].collided(player) or j[0].y>=player.y:
                    gameover(score)
        velinimigo = inimigo.moveInimigos(janela, matrizDeInimigos, velinimigo)

        if delay>=0:
            delay-=1
        if delay < 0:
            delay = delayest
        score = inimigo.kill(listaProjeteis,matrizDeInimigos,score,linha)
        inimigo.draw(matrizDeInimigos)
        janela.draw_text("SCORE: ", 20, 10, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), 100, 10, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(int(clock.get_fps())), janela.width-50, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        player.draw()
        janela.update()
def gameover(score):
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("GAMEOVER")
    mouse = janela.get_mouse()
    botaomenu = Sprite("assets\\botaomenu.png")
    botaosair = Sprite("assets\\botao4.png")
    gotitulo = Sprite("assets\\gameover.png")
    gotitulo.set_position((janela.width - gotitulo.width) / 2, 100)
    botaomenu.set_position(100, 400)
    botaosair.set_position(janela.width - 100 - botaosair.width, 400)
    while True:
        fundo.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import menu
                menu.MainMenu()
            if mouse.is_over_object(botaosair):
                janela.close
        janela.draw_text("YOUR SCORE: ", gotitulo.x + 110, gotitulo.y + gotitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score),gotitulo.x + 260, gotitulo.y + gotitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        gotitulo.draw()
        botaosair.draw()
        botaomenu.draw()
        janela.update()

def youwin(score):
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("GAMEOVER")
    mouse = janela.get_mouse()
    botaomenu = Sprite("assets\\botaomenu.png")
    botaosair = Sprite("assets\\botao4.png")
    ywtitulo = Sprite("assets\\youwin.png")
    ywtitulo.set_position((janela.width - ywtitulo.width) / 2, 100)
    botaomenu.set_position(100, 400)
    botaosair.set_position(janela.width - 100 - botaosair.width, 400)
    while True:
        fundo.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import menu
                menu.MainMenu()
            if mouse.is_over_object(botaosair):
                janela.close
        janela.draw_text("YOUR SCORE: ", ywtitulo.x + 110, ywtitulo.y + ywtitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score),ywtitulo.x + 260, ywtitulo.y + ywtitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        ywtitulo.draw()
        botaosair.draw()
        botaomenu.draw()
        janela.update()