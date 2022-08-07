# O arquivo com as classes, se ficar grande vou dividir.
import pygame as pg

from variaveis import *


pg.init()



class Botoes(pg.sprite.Sprite):
    def __init__(self, tam, pos, num, cor, texto, letra, mouse):
        pg.sprite.Sprite.__init__(self)
        self.cor = cor
        self.image = pg.Surface(tam)
        self.image.fill(self.cor[1])
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = int((pos[1]/10)*num)
        
        self.fonte = pg.font.SysFont('Times New Roma', letra)  #FontError
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
    def __init__(self, texto, nun, letra=60):
        pg.sprite.Sprite.__init__(self)
        fonte = pg.font.SysFont('Times New Roma', letra)
        self.image = fonte.render(texto, True, BRANCO)
        self.rect = self.image.get_rect()
        l = (LARGURA - self.image.get_width())/2
        h = (ALTURA/10)*nun
        self.rect.left = l
        self.rect.top = h

