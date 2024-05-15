from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from PPlay.mouse import *
from PPlay.keyboard import *
import main
dificuldade = 0

def MainMenu():
    janela = Window(1000, 600)
    mouse = janela.get_mouse()
    janela.set_title("MENU SPACE INVADERS LEONARDO BRASIL")
    fundo = GameImage("assets\\fundo.png")
    botao1 = Sprite("assets\\botao.png")
    botao2 = Sprite("assets\\botao2.png")
    botao3 = Sprite("assets\\botao3.png")
    botao4 = Sprite("assets\\botao4.png")
    titulo = Sprite("assets\\titulo.png")
    titulo.set_position(100, (janela.height - titulo.height)/2)
    botao1.set_position((janela.width - botao1.width) - 100, botao1.height * 2)
    botao2.set_position((janela.width - botao2.width) - 100, botao2.height * 4)
    botao3.set_position((janela.width - botao3.width) - 100, botao3.height * 6)
    botao4.set_position((janela.width - botao1.width) - 100, botao1.height * 8)

    while True:
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botao1):
                main.jogo(dificuldade = 1, delayest = 40, velprojetil=900)
            if mouse.is_over_object(botao3):
                dificuldade()
            if mouse.is_over_object(botao4):
                janela.close()
        fundo.draw()
        titulo.draw()
        botao1.draw()
        botao2.draw()
        botao3.draw()
        botao4.draw()
        janela.update()
def dificuldade():
    janela = Window(1000, 600)
    fundo = GameImage("assets\\fundo.png")
    janela.set_title("DIFICULDADES SPACE INVADERS LEONARDO BRASIL")
    teclado = janela.get_keyboard()
    mouse = janela.get_mouse()
    botaofacil = Sprite("assets\\botaofacil.png")
    botaomedio = Sprite("assets\\botaomedio.png")
    botaodificil = Sprite("assets\\botaodificil.png")
    botaofacil.set_position((janela.width - botaofacil.width) / 2, botaofacil.height * 2)
    botaomedio.set_position((janela.width - botaomedio.width) / 2, botaomedio.height * 5)
    botaodificil.set_position((janela.width - botaodificil.width) / 2, botaodificil.height * 8)
    while True:
        fundo.draw()
        if teclado.key_pressed("esc"):
            MainMenu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaofacil):
                main.jogo(dificuldade = 1, delayest = 40, velprojetil = 900)
            if mouse.is_over_object(botaomedio):
                main.jogo(dificuldade = 1, delayest = 80, velprojetil = 900)
            if mouse.is_over_object(botaodificil):
                main.jogo(dificuldade = 1, delayest = 120, velprojetil = 900)
        botaofacil.draw()
        botaomedio.draw()
        botaodificil.draw()
        janela.update()
MainMenu()
