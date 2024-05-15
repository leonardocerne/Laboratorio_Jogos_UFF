from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
# Criando o Menu
def menu():
    # fazendo o fundo e colocando os assets das configurações no menu com suas respecitivas posições.
    janela = Window(1100, 561)
    mouse = janela.get_mouse()
    janela.set_title("MENU KIRIKU")
    fundo = GameImage("Assets\\Fundo2.jpg")
    ranking = Sprite("Assets\\BotaoRanking.png")
    jogar = Sprite("Assets\\BotaoJogar.png")
    sair = Sprite("Assets\\BotaoSair.png")
    tutorial = Sprite("Assets\\BotaoTutorial.png")
    titulo = Sprite("Assets\\Titulo.png")
    titulo.set_position(10, 10)
    jogar.set_position(68, 205)
    tutorial.set_position(68, 285)
    ranking.set_position(68, 365)
    sair.set_position(68, 445)

    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(jogar):
                import Game
                Game.game(velper = 400, veladd = 750, limite = 150)
            if mouse.is_over_object(sair):
                janela.close()
            if mouse.is_over_object(tutorial):
                Tutorial()
            if mouse.is_over_object(ranking):
                import Dificuldade
                Dificuldade.Dificuldade()
        fundo.draw()
        titulo.draw()
        jogar.draw()
        sair.draw()
        tutorial.draw()
        ranking.draw()
        janela.update()
def Tutorial():
    janela = Window(1100, 619)
    mouse = janela.get_mouse()
    jump = Sprite("Assets\\Jump.png")
    w = Sprite("Assets\\W.png")
    space = Sprite("Assets\\Space.png")
    fundo = GameImage("Assets/TutoF.jpg")
    voltar = Sprite("Assets\\Voltar.png")
    voltar.set_position(10, 10)
    jump.set_position(750, 70)
    space.set_position(700, 140)
    w.set_position(845, 140)
    janela.set_title("TUTORIAL KIRIKU")
    teclado = janela.get_keyboard()
    while True:
        if teclado.key_pressed("esc"):
            menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(voltar):
                menu()
        fundo.draw()
        voltar.draw()
        jump.draw()
        space.draw()
        w.draw()
        janela.draw_text("or", 813, 146, size=16, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])


        janela.update()
menu()