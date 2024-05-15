from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*


def criaProjNave(player,listaProjeteis):
    # Crio o projetil
    projetil = Sprite("assets\\tiro.png", 1)
    projetil.x = player.x + 25
    projetil.y = player.y - projetil.height
    listaProjeteis.append(projetil)



def tiroPlayer(janela,listaProjeteis,velProjetil):
    for i in listaProjeteis:
        i.y -= velProjetil*janela.delta_time()
        i.draw()
        if (i.y<-50):
            listaProjeteis.remove(i)


def jogo(dificuldade, delayest , velprojetil):
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("JOGO SPACE INVADERS LEONARDO BRASIL")
    teclado = janela.get_keyboard()
    player = Sprite("assets\\player.png")
    player.set_position((janela.width - player.width)/2, (janela.height - player.width) - 20)
    velplayer = 300 / dificuldade
    listaProjeteis = []
    tempoInicial = time.time()
    delay = delayest
    while True:
        tempoAtual = time.time()
        deltaTime = tempoAtual - tempoInicial
        tempoInicial = tempoAtual
        fundo.draw()
        if teclado.key_pressed("esc"):
            import menu
            menu.MainMenu()
        if teclado.key_pressed("right"):
            player.x += velplayer * deltaTime
        if teclado.key_pressed("left"):
            player.x -= velplayer * deltaTime
        if (teclado.key_pressed("SPACE") and delay==0):
            criaProjNave(player,listaProjeteis)
        tiroPlayer(janela,listaProjeteis,velprojetil)    
        if delay>=0:
            delay-=1
        if delay < 0:
            delay = delayest
        player.draw()
        janela.update()