# coding: latin-1
from rectangulo import Rectangulo
from movimiento import Movimiento
from bala import Bala
from nave_enemiga import NaveEnemiga
from nave_jugador import NaveJugador
import pygame,sys
from fondo import Fondo

class Etapa():
      """

      """

      def __init__(self,screen):
          self.fondo                      = Fondo(screen)
	  self.screen                     = screen
	  self.naves_enemigas             = []

      def etapa1(self):
	  num_naves_enemigos = 40
	  tiempo_de_salida   = 100 # multiplo del tiempo del juego
          #creo a los enemigos
	  for num in range(num_naves_enemigos):
              figura_enemigo1=Rectangulo("enemigo1.png",100,-20,50,50)
              bala_enemigo1=Bala([Rectangulo("b.png",100,-20,5,5) for i in range(4)],4)
              self.naves_enemigas.insert(0,NaveEnemiga(self.screen,figura_enemigo1,bala_enemigo1,None,500))

      def update(self,tiempo,jugadores): 
          self.fondo.update() 
	  for nav_enem in self.naves_enemigas:
              nav_enem.update(jugadores,4,4,tiempo,10,4)
	  for jugador in jugadores:
              jugador.update(self.naves_enemigas,tiempo)
	  
