from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def Dificuldade():
    janela = Window(1100, 761)
    janela.set_title("DIFICULDADE KIRIKU")
    mouse = janela.get_mouse()
    fundo = GameImage("Assets\\Difi1.png")
    botaofacil = Sprite("Assets\\BotaoFacil.png")
    botaomedio = Sprite("Assets\\BotaoMedio.png")
    botaodificil = Sprite("Assets\\BotaoDificil.png")
    voltar = Sprite("Assets\\Voltar.png")
    teclado = janela.get_keyboard()
    voltar.set_position(10, 10)
    botaofacil.set_position(120,250)
    botaomedio.set_position(janela.width - botaomedio.width - 120,250)
    botaodificil.set_position((janela.width - botaodificil.width) / 2, 500)
    while True:
        if teclado.key_pressed("esc"):
            import Menu
            Menu.menu()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(voltar):
                import Menu
                Menu.menu()
            if mouse.is_over_object(botaofacil):
                import Game
                Game.game(velper = 400, veladd = 1000, limite = janela.width)
            if mouse.is_over_object(botaomedio):
                import Game
                Game.game(velper = 400, veladd = 750, limite = 150)
            if mouse.is_over_object(botaodificil):
                import Game
                Game.game(velper = 0, veladd = 500, limite = 150)
        fundo.draw()
        botaofacil.draw()
        botaomedio.draw()
        botaodificil.draw()
        voltar.draw()
        janela.update()