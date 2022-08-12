# A tela que aparece quando se aperta o botão de sair ou o "X" da aba.
import sys
import pygame as pg

from classes import Botoes, Janela, ManiArq, Rotulo, Seguir, ManiArq
from variaveis import *


pg.init()



class Sair(Janela):
    def __init__(self):
        self.janela()
        self.grupo = pg.sprite.Group()
        self.botoes()
        self.nome()
        self.loop()

    def janela(self):
        self.tela = pg.display.set_mode((LARGURA_S, ALTURA_S))
        pg.display.set_caption('Jogo da Velha')
        icon = pg.image.load('imagens/icone.png')
        pg.display.set_icon(icon)
    
    def nome(self):
        nome = Rotulo('Deseja Sair?', 1.2, (LARGURA_S, ALTURA_S), 40)
        self.grupo.add(nome)

    def opcoes(self):
        if pg.mouse.get_pressed() == (1, 0, 0):
            if pg.sprite.collide_rect(self.b1, self.seguir):
                self.comunica(1)
                self.sair_jogo()
            elif pg.sprite.collide_rect(self.b2, self.seguir):
                self.comunica()
                self.sair_jogo()
    
    def sair_jogo(self):
        self.continuar = False
        pg.quit()
        sys.exit()
    
    def comunica(self, valor=0):
        arq = ManiArq(ARQUIVO)
        if valor:
            arq.escrever('sim')
        else:
            arq.escrever('nao')

    def botoes(self):
        self.seguir = Seguir()
        self.b1 = Botoes(TAM2, (30, ALTURA_S), 5, COR, 'Sim', 30, self.seguir)
        self.b2 = Botoes(TAM2, (190, ALTURA_S), 5, COR, 'Não', 30, self.seguir)
        self.grupo.add(self.b1, self.b2)
        self.grupo.add(self.seguir)
    
    def loop(self):
        self.continuar = True
        while self.continuar:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.sair_jogo()
                
                self.tela.fill(CINZA)
                self.grupo.draw(self.tela)
                self.grupo.update()
                self.opcoes()

                pg.display.update()



Sair()