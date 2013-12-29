# coding: latin-1
import sys, pygame

class Movimiento():

      def __init__(self,figura):
          self.figura              = figura
          self.contador_de_movimiento=0
	  self.lim_inf_x       = 0
	  self.lim_inf_y       = -5
	  self.lim_sup_x       = 600
	  self.lim_sup_y       = 600

 
      def mover_vertical(self,screen,vy):
          """Si vy es positivo la moverá hacia abajo,
	     si vy es negativo la moverá hacia arriba.
          """
	  self.figura.move(0,vy)
	  self.figura.update(screen)

      def mover_horizontal(self,screen,vx):
          """Si vx es positivo la moverá a la derecha,
	     si vx es negativo la moverá a la izquierda.
          """
	  self.figura.move(vx,0)
	  self.figura.update(screen)

      def mover_diagonal(self,screen,vx,vy):
          """Si vx es positivo la moverá a la derecha,
	     si vx es negativo la moverá a la izquierda.
          """
	  self.figura.move(vx,vy)
	  self.figura.update(screen)
      def mover_zig_zag(self,screen,vx,vy,tiempo,tiempo_de_duracion):
	  self.mover_funcion(screen,tiempo,tiempo_de_duracion,[vy,vy],[vx,-vx])

      def mover_circular(self,screen,vx,vy,tiempo,tiempo_de_duracion,orientacion='posy',paso=5):
          """Fija 8 puntos de manera circular.La figura avanzará 
	     segun su orientacion, una cantidad de pixeles dada
             por el valor del paso.
          """
	  (posx,posy)=(vx,vy) 
          (negx,negy)=(-vx,-vy)
          if   orientacion == "posy": posy =  vy + paso
          elif orientacion == "posx": posx =  vx + paso
          elif orientacion == "negy": negy = -vy - paso
          elif orientacion == "negx": negx = -vx - paso
          x=[ vx   , posx , -vx , -2*vx , negx , -vx   , vx  , 2*vx ]
          y=[ posy , 2*vy , vy  , vy    , negy , -2*vy , -vy , -vy  ]
	  self.mover_funcion(screen,tiempo,tiempo_de_duracion,y,x)

      def mover_funcion(self,screen,tiempo,tiempo_de_duracion,list_y,list_x):
	  """Dado puntos x, y los valores de f(x)
	     expresados en y, mueve la figura
	     por cada uno de estos puntos.
          """
	  if len(list_x) == len(list_y):
              xx=list_x[self.contador_de_movimiento]
	      yy=list_y[self.contador_de_movimiento]
	      self.figura.move(xx,yy)
	      self.figura.update(screen)	  
	      if self.es_multiplo(tiempo,tiempo_de_duracion):
	         entre = False
	         if self.contador_de_movimiento == (len(list_x)-1): 
	            entre  = True
	            self.contador_de_movimiento = 0 
	         if not entre:
		    self.contador_de_movimiento += 1

      def es_multiplo(self,a,b):
	  """Si a es multiplo de b
             (20,10) True
	     (23,10) False
	  """
	  if (a%b) == 0: return True
	  return False

      def esta_en_area_de_juego(self):
	  if self.figura.rectangulo.y >= self.lim_inf_y and self.figura.rectangulo.y <= self.lim_sup_y:
	     return True
	  """if self.figura.rectangulo.x <= self.lim_inf_x and self.figura.rectangulo.x >= self.lim_sup_x:
	     return True
	  """
	  return False
