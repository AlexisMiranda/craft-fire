# coding: latin-1
from rectangulo import Rectangulo
from movimiento import Movimiento
from bala import Bala
from nave_enemiga import NaveEnemiga
from nave_jugador import NaveJugador
import pygame,sys
class Fondo():
      """

      """

      def __init__(self,screen,url_imagen1 = "fondo1.png",url_imagen2 = "fondo1.png",f1_x = 0,f1_y = 0,f2_x = 0,f2_y = -640,largo = 640,ancho = 640):
	  self.fondo1_posx                = f1_x
	  self.fondo1_posy                = f1_y
	  self.fondo2_posx                = f2_x
	  self.fondo2_posy                = f2_y
	  self.largo                      = largo
	  self.ancho                      = ancho
	  self.fondo1                     = Movimiento(Rectangulo(url_imagen1,self.fondo1_posx,self.fondo1_posy,largo,ancho))
	  self.fondo2                     = Movimiento(Rectangulo(url_imagen2,self.fondo2_posx,self.fondo2_posy,largo,ancho))
	  self.screen                     = screen

      def update(self): 
	  if self.fondo1.figura.rectangulo.y > self.largo:
	     self.fondo1.figura.rectangulo.y=self.fondo1_posy
	  if self.fondo2.figura.rectangulo.y > 0:
	     self.fondo2.figura.rectangulo.y=self.fondo2_posy 
	  self.fondo1.mover_vertical(self.screen,1)
	  self.fondo2.mover_vertical(self.screen,1)
