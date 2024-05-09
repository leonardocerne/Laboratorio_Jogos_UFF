from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *

janela = Window(800, 600)
teclado = janela.get_keyboard()
fundo = GameImage("assets\\fundo.png")
janela.set_title("Pong_Leonardo_Brasil")
bolinha = Sprite("assets\\bolinha.png")
bolinha.set_position((janela.width - bolinha.width) / 2, (janela.height - bolinha.height) / 2)
pad1 = Sprite("assets\\pad.png")
pad2 = Sprite("assets\\pad.png")
pad1.set_position(50, (janela.height - pad1.height) / 2)
pad2.set_position((janela.width - pad2.width - 50), (janela.height - pad1.height) / 2)
velx = 0
vely = 0
vpad1 = 400
vpad2 = 400
pont1 = 0
pont2 = 0
contador = 0
tempoInicial = time.time()
x = 1
y = 0
z = 0
cont2 = 0
while True:
    tempoAtual = time.time()
    deltaTime = tempoAtual - tempoInicial
    tempoInicial = tempoAtual
    bolinha.x += velx * deltaTime
    bolinha.y += vely * deltaTime
    if (bolinha.x < 0):
        bolinha.x = (janela.width - bolinha.width) / 2
        bolinha.y = (janela.height - bolinha.height) / 2
        velx = 0
        vely = 0
        pont1 +=1
    if (bolinha.x + bolinha.width > janela.width):
        bolinha.x = (janela.width - bolinha.width) / 2
        bolinha.y = (janela.height - bolinha.height) / 2
        pont2 += 1    
        velx = 0
        vely = 0
    if (bolinha.y < 0):
        vely *= -1
        bolinha.y += 2
    if (bolinha.y + bolinha.height > janela.height):
        vely *= -1
        bolinha.y -= 2    
    if (teclado.key_pressed("w")) and (pad1.y>0):
        pad1.y -= vpad1 * deltaTime
    if (teclado.key_pressed("s")) and (pad1.y <= janela.height - pad1.height):
        pad1.y += vpad1 * deltaTime

    if (pad2.y > bolinha.y and abs(pad2.y - bolinha.y) > 10) and (pad2.y>0): 
        pad2.y -= vpad2 * deltaTime 
    if (pad2.y < bolinha.y and abs(pad2.y - bolinha.y) > 10) and (pad2.y <= janela.height - pad1.height):
        pad2.y += vpad2 * deltaTime
    if (bolinha.collided(pad1)):
        velx *= -1
        bolinha.x += 2
        if y == 1:
            cont2 += 1
        elif z == 1:
            cont2 += 1
        else:
            contador += 1
    if (bolinha.collided(pad2)):
        velx *= -1    
        bolinha.x -= 2
        if y == 1:
            cont2 += 1
        elif z == 1:
            cont2 += 1
        else:
            contador += 1
    if (teclado.key_pressed("space")):
        velx = 400
        vely = 400
        x = randint(1, 2)
    if pont1>=5 or pont2>=5:
        time.sleep(1)
        janela.close()   
    if contador == 3:
        if x == 1:
            pad1.height /= 2
            x = 0
            y = 1
        if x == 2:
            pad2.height /= 2 
            x = 0
            z = 1
        x = randint(1, 2)
        contador = 0
    if cont2 == 2:
        if y == 1:
            pad1.height *= 2
            y = 0
        if z == 1:
            pad2.height *= 2
            z = 0
        cont2 = 0
    fundo.draw()
    bolinha.draw()
    pad1.draw()
    pad2.draw()
    janela.draw_text(str(pont2), (janela.width / 2) - 40, 30, size=48, font_name="ComicSans", bold=True,color=[255, 0, 0])
    janela.draw_text(str(pont1), (janela.width / 2) + 40, 30, size=48, font_name="ComicSans", bold=True,color=[0, 255, 0])
    janela.draw_text("player", (janela.width / 2) - 300, 30, size=30, font_name="ComicSans", bold=True, color=[0,0,0])
    janela.draw_text("IA", (janela.width / 2) + 200, 30, size=30, font_name="ComicSans", bold=True, color=[0,0,0])
    janela.update()