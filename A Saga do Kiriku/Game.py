from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def game(velper, veladd, limite):
    janela = Window(1100, 619)
    fundo = GameImage("Assets/Fundo3.jpg")
    fundo2 = GameImage("Assets/Fundo3.jpg")
    janela.set_title("JOGAR KIRIKU")
    personagem = Sprite("Assets\\KIRIKU.png")
    inimigo2 = Sprite("Assets\\inimigo2.png")
    inimigo = Sprite("Assets\\inimigo1.png")
    jumpskill = Sprite("Assets\\jumpskill.png")
    jumpskill.set_position(janela.width, janela.height - inimigo2.height - 75)
    veljs = 0
    fundo2.x = fundo.width
    personagem.x = 100
    personagem.y = janela.height - personagem.height
    inimigo.x = janela.width
    inimigo.y = janela.height - inimigo.height
    inimigo2.x = janela.width
    inimigo2.y = janela.height - inimigo2.height
    comandos = Window.get_keyboard()
    x = 0000
    velini1 = 0.7
    velini2 = 0.7
    teclado = janela.get_keyboard()
    # Define a velocidade de pulo
    velocidade_pulo = 2.8

    # Define a gravidade
    gravidade = 0.018

    # Define a velocidade vertical inicial
    velocidade_vertical = 0

    # Define se o personagem está no chão
    no_chao = True
    velocidade_fundo = 100

    pygame.mixer.init()

    # Carregue a música
    pygame.mixer.music.load('Assets\\Musica.mp3')

    # Tocar a música
    pygame.mixer.music.play(-1)
    while True:
        fundo.draw()
        fundo2.draw()
        if teclado.key_pressed("esc"):
            import Menu
            Menu.menu()
        if (comandos.key_pressed("left") or comandos.key_pressed("A")):
            personagem.x -= velper * janela.delta_time()
        if ((comandos.key_pressed("right") or comandos.key_pressed("D")) and personagem.x < limite):
            personagem.x += velper * janela.delta_time()
        if (personagem.x <= 0):
            personagem.x = 0.5
        if (personagem.x >= janela.width - personagem.width):
            personagem.x = janela.width - personagem.width

        if x > 70:
            inimigo2.x -= velini2
            if inimigo2.x < -inimigo2.width:
                inimigo2.x = janela.width

        inimigo.x -= velini1
        if inimigo.x < -inimigo.width:
            inimigo.x = janela.width
        if int(x) % veladd == 0 and x<6050 and x!=0:
            velini1 += 0.015
            velini2 += 0.015

        if int(x) % 7000 == 0:
            velini1 += 0.02
            velini2 += 0.02
        if personagem.collided(jumpskill):
            gravidade = 0.012
            velocidade_pulo = 2.8
            jumpskill.x = janela.width
            veljs = 0
        if int(x) - 1500 % 2000 == 0:
            velocidade_pulo = 2.8
            gravidade = 0.018
        # Se a tecla de pulo for pressionada e o personagem estiver no chão
        if (teclado.key_pressed("UP") or teclado.key_pressed("W") or teclado.key_pressed("SPACE")) and no_chao:
                # Faz o personagem pular
            velocidade_vertical = -velocidade_pulo
            no_chao = False
        if int(x) - 1000 % 2000 == 0:
            veljs = velini2
        jumpskill.x -= veljs
            # Aplica a gravidade
        velocidade_vertical += gravidade

            # Atualiza a posição vertical do personagem
        personagem.y += velocidade_vertical

            # Se o personagem estiver abaixo do chão
        if personagem.y > janela.height - personagem.height:
                # Coloca o personagem no chão
            personagem.y = janela.height - personagem.height
            no_chao = True
        if personagem.collided(inimigo):
            gameover()
        if personagem.collided(inimigo2):
            gameover()
        if janela.delta_time() > 0:
            fundo.x -= velocidade_fundo * janela.delta_time()
            fundo2.x -= velocidade_fundo * janela.delta_time()

            if fundo.x <= -fundo.width:
                fundo.x = fundo2.x + fundo2.width

            if fundo2.x <= -fundo2.width:
                fundo2.x = fundo.x + fundo.width
        x+= velini2 / 10
        personagem.draw()
        inimigo2.draw()
        inimigo.draw()
        jumpskill.draw()
        janela.draw_text(str(int(x)) + "m", 900, 50, size=19, font_name="Tempus Sans ITC", bold=True,
                         color=[0, 0, 0])

        janela.update()

def gameover():
    janela = Window(1100, 619)
    fundo = GameImage("Assets/FundoGO.jpg")
    janela.set_title("GAME OVER")
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    botaomenu = Sprite("Assets\\BotaoMenu.png")
    botaosair = Sprite("Assets\\BotaoSair.png")
    botaomenu.set_position(590, 200)
    botaosair.set_position(820, 200)
    while True:
        fundo.draw()
        botaomenu.draw()
        botaosair.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import Menu
                Menu.menu()
            if mouse.is_over_object(botaosair):
                janela.close()
        if teclado.key_pressed("esc"):
            import Menu
            Menu.menu()
        janela.update()