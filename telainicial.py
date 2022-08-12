# A classe inicial, que abre o jogo.
import sys
import os
import pygame as pg

from classes import Botoes, Janela, Rotulo, Seguir, ManiArq
from variaveis import *




pg.init()



class Controladora(Janela):
    def __init__(self):
        self.janela()
        self.arq = ManiArq(ARQUIVO)
        self.grupo = pg.sprite.Group()
        self.botoes()
        self.nome()
        self.loop()
        
    def janela(self):
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption('Jogo da Velha')
        icon = pg.image.load('imagens/icone.png')
        pg.display.set_icon(icon)
        
    def nome(self):
        nome = Rotulo('Jogo da Velha', 1.2, (LARGURA, ALTURA), 80)
        self.grupo.add(nome)
    
    def opcoes(self):
        if pg.mouse.get_pressed() == (1, 0, 0):
            if pg.sprite.collide_rect(self.b1, self.seguir):
                pass
            elif pg.sprite.collide_rect(self.b2, self.seguir):
                pass
            elif pg.sprite.collide_rect(self.b3, self.seguir):
                pass
            elif pg.sprite.collide_rect(self.b4, self.seguir):
                ...
            elif pg.sprite.collide_rect(self.b5, self.seguir):
                self.sair_jogo()
    
    def sair_jogo(self):
        os.startfile('telasair.py')
    
    def encerrar(self):
        self.arq.escrever('nao')
        self.continuar = False
        pg.quit()
        sys.exit()
    
    def botoes(self):
        self.seguir = Seguir()
        self.b1 = Botoes(TAM, POS, 3, COR, 'Jogar', NUM, self.seguir)
        self.b2 = Botoes(TAM, POS, 4.5, COR, 'Como Jogar', NUM, self.seguir)
        self.b3 = Botoes(TAM, POS, 6, COR, 'Configurações', NUM, self.seguir)
        self.b4 = Botoes(TAM, POS, 7.5, COR, 'Créditos', NUM, self.seguir)
        self.b5 = Botoes((60, 30), POS2, 9.3, COR, 'Sair', 30, self.seguir)
        self.grupo.add(self.b1, self.b2, self.b3, self.b4, self.b5)
        self.grupo.add(self.seguir)
    
    def loop(self):
        self.continuar = True
        self.relogio = pg.time.Clock()
        while self.continuar:
            self.relogio.tick(24)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair_jogo()
                if 'sim' in self.arq.ler():
                    self.encerrar()
                
                self.tela.fill(CINZA)
                self.grupo.draw(self.tela)
                self.grupo.update()
                self.opcoes()

                pg.display.update()
