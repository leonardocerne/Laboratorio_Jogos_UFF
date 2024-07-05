from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import datetime

def game(velper, veladd, limite, dificuldade):
    janela = Window(1100, 619)
    hora = datetime.datetime.now().time()
    y = hora.hour
    if(y > 18 or y < 6):
        fundo = GameImage("Assets\\Fundonoite.png")
        fundo2 = GameImage("Assets\\Fundonoite.png")
    if(y > 6 and y < 18):
        fundo = GameImage("Assets\\Fundoteste.png")
        fundo2 = GameImage("Assets\\Fundoteste.png")
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
    velini1 = 1
    velini2 = 1
    teclado = janela.get_keyboard()
    # Define a velocidade de pulo
    velocidade_pulo = 7.3

    # Define a gravidade
    gravidade = 0.15

    # Define a velocidade vertical inicial
    velocidade_vertical = 0

    # Define se o personagem está no chão
    no_chao = True
    velocidade_fundo = 100

    pygame.mixer.init()

    # Carregue a música
    pygame.mixer.music.load('Assets\\Musica.mp3')
    pygame.mixer.music.set_volume(0.7)
    efeito = pygame.mixer.Sound('Assets\\efeitojs.wav')
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
        if int(x) % veladd == 0 and x<6050 and x>50:
            velini1 += 0.3
            velini2 += 0.3
            velocidade_fundo += 10
        if int(x) % 7000 == 0:
            velini1 += 0.6
            velini2 += 0.6
        if personagem.collided(jumpskill):
            gravidade = 0.080
            velocidade_pulo = 8
            jumpskill.x = janela.width
            veljs = 0
            efeito.play()
        if (int(x) - 1500) % 2000 == 0:
            velocidade_pulo = 7.3
            gravidade = 0.15
        # Se a tecla de pulo for pressionada e o personagem estiver no chão
        if (teclado.key_pressed("UP") or teclado.key_pressed("W") or teclado.key_pressed("SPACE")) and no_chao:
                # Faz o personagem pular
            velocidade_vertical = -velocidade_pulo
            no_chao = False
        if (int(x) - 1000) % 2000 == 0 and int(x) != 0:
            jumpskill.x = janela.width
            veljs = velini2
        if jumpskill.x < 0:
            jumpskill.x = janela.width
            veljs = 0
        jumpskill.x -= veljs
            # Aplica a gravidade
        velocidade_vertical += gravidade
        if int(x) == 10000 and dificuldade == 3:
            easteregg()
            # Atualiza a posição vertical do personagem
        personagem.y += velocidade_vertical

            # Se o personagem estiver abaixo do chão
        if personagem.y > janela.height - personagem.height:
                # Coloca o personagem no chão
            personagem.y = janela.height - personagem.height
            no_chao = True
        if personagem.collided(inimigo):
            pygame.mixer.music.stop()
            gameover()
        if personagem.collided(inimigo2):
            pygame.mixer.music.stop()
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
    pygame.mixer.init()
    efeitobotao = pygame.mixer.Sound('Assets\\efeitobotao.flac')
    while True:
        fundo.draw()
        botaomenu.draw()
        botaosair.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import Menu
                efeitobotao.play()
                Menu.menu()
            if mouse.is_over_object(botaosair):
                janela.close()
        if teclado.key_pressed("esc"):
            import Menu
            efeitobotao.play()
            Menu.menu()
        janela.update()

def easteregg():
    janela = Window(1100, 619)
    fundo = GameImage("Assets/fundoee.jpg")
    janela.set_title("easteregg")
    mouse = janela.get_mouse()
    teclado = janela.get_keyboard()
    botaomenu = Sprite("Assets\\BotaoMenu.png")
    botaosair = Sprite("Assets\\BotaoSair.png")
    botaomenu.set_position(200, 200)
    botaosair.set_position(800, 200)
    pygame.mixer.init()
    pygame.mixer.music.load('Assets\\kiriku.mp3')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    efeitobotao = pygame.mixer.Sound('Assets\\efeitobotao.flac')
    while True:
        fundo.draw()
        botaomenu.draw()
        botaosair.draw()
        if mouse.is_button_pressed(1):
            if mouse.is_over_object(botaomenu):
                import Menu
                efeitobotao.play()
                Menu.menu()
            if mouse.is_over_object(botaosair):
                janela.close()
        if teclado.key_pressed("esc"):
            import Menu
            efeitobotao.play()
            Menu.menu()
        janela.update()