# O arquivo com as classes, se ficar grande vou dividir.
from abc import ABC, abstractmethod
from pathlib import Path
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
    def __init__(self, texto, nun, quadro, letra=60):
        pg.sprite.Sprite.__init__(self)
        fonte = pg.font.SysFont('Times New Roma', letra)
        self.image = fonte.render(texto, True, BRANCO)
        self.rect = self.image.get_rect()
        l = (quadro[0] - self.image.get_width())/2
        h = (quadro[1]/10)*nun
        self.rect.left = l
        self.rect.top = h



class Janela(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def janela(self):
        pass

    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def opcoes(self):
        pass

    @abstractmethod
    def botoes(self):
        pass

    @abstractmethod
    def loop(self):
        pass



class ManiArq:
    def __init__(self, arquivo):
        self.arquivo = self._conferir(arquivo)
        if not self._conferir_arquivo(self.arquivo):
            self._criar(self.arquivo)

    def _criar(self, nome):
        with open(nome, 'w') as arq:
            pass
    
    def escrever(self, escrevi):
        with open(self.arquivo, 'w') as arq:
            arq.write(f'{escrevi} \n')

    def ler(self):
        with open(self.arquivo, 'r') as arq:
            linha = arq.readline()
            linha = linha.replace('\n', '')
        return linha
    
    def _conferir(self, nome):
        if not '.txt' in nome:
            nome = nome + '.txt'
        return nome
    
    def _conferir_arquivo(self, nome):
        arquivo = Path(nome)
        if arquivo.is_file():
            return True
    

