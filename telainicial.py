# A classe inicial, que abre o jogo.
import sys
import pygame as pg

from classes import Botoes, Rotulo, Seguir
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
        nome = Rotulo('Jogo da Velha', 1.2, 80)
        self.grupo.add(nome)
    
    def botoes(self):
        seguir = Seguir()
        b1 = Botoes(TAM, POS, 3, COR, 'Jogar', NUM, seguir)
        b2 = Botoes(TAM, POS, 4.5, COR, 'Como Jogar', NUM, seguir)
        b3 = Botoes(TAM, POS, 6, COR, 'Configurações', NUM, seguir)
        b4 = Botoes(TAM, POS, 7.5, COR, 'Créditos', NUM, seguir)
        self.grupo.add(b1, b2, b3, b4)
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

