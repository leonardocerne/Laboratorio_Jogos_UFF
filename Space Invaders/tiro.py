from PPlay.sprite import*

def criaProjNave(player,listaProjeteis):
    # Crio o projetil
    projetil = Sprite("assets\\tiro.png",1)
    projetil.x = player.x + 28
    projetil.y = player.y - projetil.height
    listaProjeteis.append(projetil)

def tiroPlayer(janela,listaProjeteis,velProjetil):
    for i in listaProjeteis:
        i.y -= velProjetil*janela.delta_time()
        i.draw()
        if (i.y<-50):
            listaProjeteis.remove(i)
