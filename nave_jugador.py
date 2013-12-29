# coding: latin-1
import sys, pygame
from nave import Nave
class NaveJugador(Nave):
      """

      """
      def __init__(self,screen,figura,bala,bomba,vida):
          Nave.__init__(self,screen,figura,bala,bomba,vida)
	  self.leftSigueApretada      = False
	  self.upSigueApretada        = False
	  self.downSigueApretada      = False
	  self.rightSigueApretada     = False
          self.velocidad              = 12
          self.vx,self.vy             = 0,0
	  self.cnt_disparo            = 0

      def update(self,naves_enemigas,tiempo):
	  if not self.muerta:
             #si la nave colisiona con algún enemigo o alguna bala de ese enemigo le quito una vida
             self.colision_con_nave(naves_enemigas)
             #dibujo la vida de este jugador
             self.dibujar_vida(10,630)
             # si no le queda vida muere
             if self.vida <= 0: self.morir()
             #Muevo la nave
             self.mover_diagonal(self.screen,self.vx,self.vy) 
	     #dispara 
	     vx,vy=-12,-12
	     tipo_disparo=0
	     separacion=1
	     self.disparar(vx,vy,tipo_disparo,separacion,tiempo,10,"negy",5,True)

      def evenKeydownUp(self):
          self.upSigueApretada    = True
          self.vy                 = -self.velocidad
      def evenKeydownDown(self):
          self.downSigueApretada  = True
          self.vy                 = self.velocidad
      def evenKeydownLeft(self):
          self.leftSigueApretada  = True
          self.vx                 = -self.velocidad
      def evenKeydownRight(self):
          self.rightSigueApretada = True
          self.vx                 = self.velocidad
      def evenKeyupUp(self):
          self.upSigueApretada = False
          if self.downSigueApretada: self.vy = self.velocidad
          else: self.vy = 0
      def evenKeyupDown(self):
          self.downSigueApretada = False
          if self.upSigueApretada: self.vx = -self.velocidad
          else: self.vy = 0
      def evenKeyupLeft(self):
          self.leftSigueApretada = False
          if self.rightSigueApretada: self.vx = self.velocidad
          else: self.vx = 0
      def evenKeyupRight(self):
          self.rightSigueApretada = False
          if  self.leftSigueApretada: self.vx = -self.velocidad
          else: self.vx = 0
