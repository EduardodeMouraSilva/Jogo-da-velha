# O arquivo com as classes, se ficar grande vou dividir.
from re import X
import sys
import pygame as pg

from variaveis import *


pg.init()



class Controladora:
    def __init__(self):
        self.janela()
        self.grupo = pg.sprite.Group()
        self.botoes()
        self.nome_jogo()
        self.loop()
        
    def janela(self):
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption('Jogo da Velha')
        icon = pg.image.load('imagens/icone.png')
        pg.display.set_icon(icon)
    
    def nome_jogo(self):
        nome = Rotulo('Jogo da Velha', 10)
        self.grupo.add(nome)
    
    def botoes(self):
        seguir = Seguir()
        b1 = Botoes(TAM, POS, 5, COR, 'Jogar', NUM, seguir)
        b2 = Botoes(TAM, POS, 4, COR, 'Como Jogar', NUM, seguir)
        b3 = Botoes(TAM, POS, 3, COR, 'Configurações', NUM, seguir)
        b4 = Botoes(TAM, POS, 2, COR, 'Créditos', NUM, seguir)
        self.grupo.add(b1)
        self.grupo.add(seguir)
    
    def loop(self):
        continuar = True
        while continuar:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    continuar = False
                    pg.quit()
                    sys.exit()
                
                self.tela.fill(CINZA)
                self.grupo.draw(self.tela)
                self.grupo.update()
                pg.display.update()



class Botoes(pg.sprite.Sprite):
    def __init__(self, tam, pos, num, cor, texto, letra, mouse):
        pg.sprite.Sprite.__init__(self)
        self.cor = cor
        self.image = pg.Surface(tam)
        self.image.fill(self.cor[1])
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = int(pos[1]/num)
        
        self.fonte = pg.font.SysFont('Times New Roma', letra)
        self.texto = self.fonte.render(texto, True, self.cor[0])
        self.l = (tam[0] - self.texto.get_width())/2
        self.h = (tam[1] - self.texto.get_height())/2
        self.image.blit(self.texto, ((self.l, self.h)))
        self.mouse = mouse

    def update(self):
        colidiu = pg.sprite.collide_rect(self, self.mouse)
        if colidiu:
            self.image.fill(self.cor[2])
        else:
            self.image.fill(self.cor[1])
        self.image.blit(self.texto, ((self.l, self.h)))



class Seguir(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1, 1))
        self.image.set_colorkey(PRETO)
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = 0, 0
    
    def update(self):
        x, y = pg.mouse.get_pos()
        self.rect.left = x
        self.rect.top = y
        
        

class Rotulo(pg.sprite.Sprite):
    def __init__(self, texto, nun):
        pg.sprite.Sprite.__init__(self)
        fonte = pg.font.SysFont('Times New Roma', 60)
        self.image = fonte.render(texto, True, BRANCO)
        self.rect = self.image.get_rect()
        l = (LARGURA - self.image.get_width())/2
        h = 640/nun
        print(self.image.get_height())
        self.rect.left = l
        self.rect.top = h


Controladora()
