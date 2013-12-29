# coding: latin-1
import sys, pygame
from nave import Nave
class NaveEnemiga(Nave):
      """

      """

      def __init__(self,screen,figura,bala,bomba,vida):
          Nave.__init__(self,screen,figura,bala,bomba,vida)

      def update(self,naves_jugadores,vx,vy,tiempo,tiempo_de_duracion,tipo_de_movimiento,orientacion='posy',paso=5):
	  if not self.muerta:

             #si la nave colisiona con algún enemigo o alguna bala de ese enemigo le quito una vida
             self.colision_con_nave(naves_jugadores)
             # si no le queda vida muere
             if self.vida <= 0:
                self.morir()
	        self.figura.rectangulo.y=-500
             #Muevo la nave
	     if   tipo_de_movimiento == 0: self.mover_vertical(self.screen,vy)
	     elif tipo_de_movimiento == 1: self.mover_horizontal(self.screen,vx)
	     elif tipo_de_movimiento == 2: self.mover_diagonal(self.screen,vx,vy)
	     elif tipo_de_movimiento == 3: self.mover_zig_zag(self.screen,vx,vy,tiempo,tiempo_de_duracion)
	     elif tipo_de_movimiento == 4: self.mover_circular(self.screen,vx,vy,tiempo,tiempo_de_duracion,orientacion,paso)
	     #dispara 
	     vx,vy=-5,-5
	     tipo_disparo=2
	     separacion=1
	     self.disparar(vx,vy,tipo_disparo,separacion,tiempo,10,"negy",5)
             #dispara cada sierto tiempo
	     if self.es_multiplo(tiempo,tiempo_de_duracion):
                self.disparar_bala()
