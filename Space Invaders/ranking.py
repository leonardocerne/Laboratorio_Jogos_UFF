from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from pygame import mixer


def rankingmenu():
    janela = Window(1000, 600)
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    janela.set_title("RANKING SPACE INVADERS LEONARDO BRASIL")
    fundo = GameImage("assets\\fundo.png")
    pontuacao = rankinglista("pontuação.txt")
    altura = 130
    limite=0

    while True:
        fundo.draw()
        if(teclado.key_pressed("ESC")):
            import menu
            menu.Menu()
        for i in range(len(pontuacao)):
            if i < 5:
                janela.draw_text(str(pontuacao[i]), (janela.width/2)- 150, altura + i * 50, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
            janela.draw_text(("RANKING"), (janela.width / 2)-120, 50, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
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
    nome = input("Insira seu nome: ")
    data = input("Insira a data de hoje:")
    arquivo = open("pontuação.txt", "r")
    conteudo = arquivo.readlines()
    conteudo.append(str(score) + " - " + nome + " - " + data + ".")
    arquivo.close()
    arquivo = open("pontuação.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()

    while True:
        fundo.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import menu
                menu.MainMenu()
            if mouse.is_over_object(botaosair):
                janela.close()
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
    nome = input("Insira seu nome: ")
    data = input("Insira a data de hoje:")
    arquivo = open("pontuação.txt", "r")
    conteudo = arquivo.readlines()
    conteudo.append(str(score) + " - " + nome + " - " + data + ".")
    arquivo.close()
    arquivo = open("pontuação.txt", "w")
    arquivo.writelines(conteudo)
    arquivo.close()
    while True:
        fundo.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import menu
                menu.MainMenu()
            if mouse.is_over_object(botaosair):
                janela.close()
        janela.draw_text("YOUR SCORE: ", ywtitulo.x + 110, ywtitulo.y + ywtitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score),ywtitulo.x + 260, ywtitulo.y + ywtitulo.height + 50, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        ywtitulo.draw()
        botaosair.draw()
        botaomenu.draw()
        janela.update()

def extrair_pontuacao(dado):
    partes = dado.split(" - ")
    pontuacao = int(partes[0])
    return pontuacao

def rankinglista(file):
    arquivo = open(file)
    pontuacao = []
    for i in arquivo:
        temp = i.split(".")
        for j in temp:
            pontuacao.append(j)
    pontuacao.pop(len(pontuacao) - 1)
    pontuacaoord = sorted(pontuacao, key=extrair_pontuacao, reverse=True)
    arquivo.close()
    return pontuacaoord

