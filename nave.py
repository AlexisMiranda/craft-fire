# coding: latin-1
import sys, pygame
from movimiento import Movimiento
from disparo import Disparo

from rectangulo import Rectangulo
class Nave(Movimiento):
      """

      """

      def __init__(self,screen,figura,figura_bala,bomba,vida):
	  Movimiento.__init__(self,figura)
	  self.screen                 = screen
	  self.vida                   = vida
          self.vida_total             = vida
	  #lista de balas
	  self.figura_bala            = figura_bala
	  self.balas                  = [] 
	  self.cnt_balas              = 0
	  self.bomba                  = bomba
	  self.muerta                 = False

      def disparar(self,vx,vy,tipo_de_disparo,separacion,tiempo,tiempo_de_duracion,orientacion="posy",paso=5,pri=False):
	  """Recibe los parametros de las balas
          """
	  for bala in self.balas:
	     if bala.dispara:
                posx=self.figura.rectangulo.x
                posy=self.figura.rectangulo.y
                if pri:
	           print self.figura.rectangulo.x,self.figura.rectangulo.y
	        if   tipo_de_disparo == 0:
                     bala.disparo_vertical(self.screen,posx,posy,vy,separacion)
	        elif tipo_de_disparo == 1:
                     bala.disparo_vertical_circular(self.screen,posx,posy,vx,vy,separacion,tiempo,
	      		                           tiempo_de_duracion,orientacion,paso)
	        elif tipo_de_disparo == 2:
                     bala.disparo_diagonal(self.screen,posx,posy,vx,vy) 
	        elif tipo_de_disparo == 3:
                     bala.disparo_escudo(self.screen,posx,posy,vx,vy,separacion)
             else: self.balas.remove(bala)

      def disparar_bala(self):

	  self.balas.insert(0,Disparo([Rectangulo("b.png",100,100,5,5) for i in range(1)],1))
          self.balas[0].dispara =  True
	  """self.cnt_balas                     += 1
	  if self.cnt_balas >= len(self.balas): self.cnt_balas = 0
	  """

      def dibujar_vida(self,posx,posy,color_cuadro=[23,23,240],color_vida=[25,125,125]):
          if self.vida_total > 0:
             #cuadro que contiene la vida total
             largo_cuadro_x=self.vida_total
             ancho_cuadro_y=10
	     pygame.draw.rect(self.screen,color_cuadro,[posx,posy,largo_cuadro_x,ancho_cuadro_y])
             #dinujo cada cuadro de vida
	     largo_un_cuadrado=largo_cuadro_x/self.vida_total
             x=posx
	     for num in range(self.vida):
	         x=x+largo_un_cuadrado
	         pygame.draw.rect(self.screen,color_vida,[x,posy,largo_un_cuadrado,ancho_cuadro_y])
             
      def collidelist(self,lista_de_naves):
          """Cada una de las figuras involucradas en la colicion debe ser del mismo tipo
          """
	  lista_de_figuras=[nave.figura for nave in lista_de_figuras]
	  return self.figura.collidelist(lista_de_figuras)
	
      def colision_con_nave(self,naves_enemigas):
	  """Recibe una lista de enemigos de esta nave
	  """	  
          #si la nave colisiona con algún enemigo o alguna bala de ese enemigo le quito una vida
          if  naves_enemigas is not None:
              if self.figura.collidelist([nave.figura.rectangulo for nave in naves_enemigas]) != -1: 
                 self.vida -= 1
		 return True
              for nave in naves_enemigas:
                  for balas_nave in nave.balas:
                      if self.figura.collidelist([bala.figura.rectangulo for bala in balas_nave.balas]) != -1:
                         self.vida -=1
			 return True
	
      def explotar(self):
          pass
      def lanzar_bomba(self):
          pass
      def morir(self):
	  self.figura.rectangulo.y=-500
	  self.muerta=True
          
          
