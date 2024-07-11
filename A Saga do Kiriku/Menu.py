from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import pygame
# Criando o Menu
def menu():
    # fazendo o fundo e colocando os assets das configurações no menu com suas respecitivas posições.
    janela = Window(1100, 561)
    mouse = janela.get_mouse()
    janela.set_title("MENU KIRIKU")
    fundo = GameImage("Assets\\Fundo2.jpg")
    dificuldade = Sprite("Assets\\Botaodificuldade.png")
    jogar = Sprite("Assets\\BotaoJogar.png")
    sair = Sprite("Assets\\BotaoSair.png")
    tutorial = Sprite("Assets\\BotaoTutorial.png")
    titulo = Sprite("Assets\\Titulo.png")
    titulo.set_position(10, 10)
    jogar.set_position(68, 205)
    tutorial.set_position(68, 285)
    dificuldade.set_position(68, 365)
    sair.set_position(68, 445)
    pygame.mixer.init()
    efeitobotao = pygame.mixer.Sound('Assets\\efeitobotao.flac')

    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(jogar):
                import Game
                Game.game(velper = 400, veladd = 750, limite = 150, dificuldade = 2)
            if mouse.is_over_object(sair):
                janela.close()
            if mouse.is_over_object(tutorial):
                efeitobotao.play()
                Tutorial()
            if mouse.is_over_object(dificuldade):
                import Dificuldade
                efeitobotao.play()
                Dificuldade.Dificuldade()
        fundo.draw()
        titulo.draw()
        jogar.draw()
        sair.draw()
        tutorial.draw()
        dificuldade.draw()
        janela.update()
def Tutorial():
    janela = Window(1100, 619)
    mouse = janela.get_mouse()
    jump = Sprite("Assets\\BotaoPular.png")
    w = Sprite("Assets\\W.png")
    space = Sprite("Assets\\BotaoEspaço.png")
    fundo = GameImage("Assets/TutoF.jpg")
    voltar = Sprite("Assets\\Voltar.png")
    setaD = Sprite("Assets\\BotaosetaD.png")
    setaE = Sprite("Assets\\BotaosetaE.png")
    botaoD = Sprite("Assets\\BotaoD.png")
    botaoA = Sprite("Assets\\BotaoA.png")
    botaocomandos = Sprite("Assets\\Botaocomandos.png")
    botaocomojogardark = Sprite("Assets\\Botaocomojogardark.png")
    botaosetacima = Sprite("Assets\\BotaosetaCima.png")
    ir = Sprite("Assets\\Ir.png")
    ir.set_position(janela.width - ir.width - 10, janela.height - ir.height - 10)
    andar = Sprite("Assets\\BotaoAndar.png")
    botaocomandos.set_position(((janela.width - botaocomandos.width) / 2) - 50, janela.height - botaocomandos.height - 10)
    botaocomojogardark.set_position(((janela.width - botaocomandos.width) / 2) + 50, janela.height - botaocomandos.height - 10)
    botaosetacima.set_position(750, 145)
    setaD.set_position(900, janela.height - setaD.height - 175)
    setaE.set_position(600, janela.height - setaE.height - 175)
    botaoD.set_position(900, janela.height - botaoD.height - 100)
    botaoA.set_position(600, janela.height - botaoD.height - 100)
    voltar.set_position(10, 10)
    jump.set_position(750, 70)
    space.set_position(600, 145)
    andar.set_position(750, janela.height - andar.height - 240)
    w.set_position(900, 145)
    janela.set_title("TUTORIAL KIRIKU")
    teclado = janela.get_keyboard()
    pygame.mixer.init()
    efeitobotao = pygame.mixer.Sound('Assets\\efeitobotao.flac')
    while True:
        if teclado.key_pressed("esc"):
            efeitobotao.play()
            menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(voltar):
                efeitobotao.play()
                menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(ir):
                efeitobotao.play()
                Tutorial2()
        fundo.draw()
        voltar.draw()
        jump.draw()
        space.draw()
        w.draw()
        ir.draw()
        setaD.draw()
        setaE.draw()
        botaoD.draw()
        botaoA.draw()
        andar.draw()
        botaosetacima.draw()
        botaocomojogardark.draw()
        botaocomandos.draw()
        janela.draw_text("para esquerda", 620, janela.height - botaoD.height - 121, size=18, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])
        janela.draw_text("para direita", 925, janela.height - botaoD.height - 121, size=18, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])


        janela.update()


def Tutorial2():
    janela = Window(1100, 619)
    mouse = janela.get_mouse()
    fundo = GameImage("Assets\\TutoF.jpg")
    teclado = janela.get_keyboard()
    voltar = Sprite("Assets\\Voltar.png")
    voltar.set_position(10, janela.height - voltar.height - 10)
    botaocomandosdark = Sprite("Assets\\Botaocomandosdark.png")
    botaocomojogar = Sprite("Assets\\Botaocomojogar.png")
    fundotexto = Sprite("Assets\\fundotexto.png")
    fundotexto.set_position((janela.width / 2) - 40, 40)
    botaocomandosdark.set_position(((janela.width - botaocomandosdark.width) / 2) - 50, janela.height - botaocomandosdark.height - 10)
    botaocomojogar.set_position(((janela.width - botaocomandosdark.width) / 2) + 50, janela.height - botaocomandosdark.height - 10)
    pygame.mixer.init()
    efeitobotao = pygame.mixer.Sound('Assets\\efeitobotao.flac')
    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            efeitobotao.play()
            Tutorial()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(voltar):
                efeitobotao.play()
                Tutorial()
        fundotexto.draw()
        botaocomandosdark.draw()
        botaocomojogar.draw()
        voltar.draw()
        janela.update()