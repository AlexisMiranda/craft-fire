import pygame
import math

class Circulo():

      def __init__(self,imagen,x,y,radio):
          self.transform_img = int((radio*2)+(radio*0.2))
          self.imagen        = pygame.transform.scale(pygame.image.load(imagen),[self.transform_img]*2)
          self.radio         = radio
	  self.x             = x
	  self.y             = y
	 
      def update(self,screen,color=[255,0,0]):
	  posx_img      = self.x-(self.radio+(self.radio*0.1))
	  posy_img      = self.y-(self.radio+(self.radio*0.1))
	  dimencion     = self.radio+self.radio*0.4
	  screen.blit(self.imagen,[posx_img,posy_img,dimencion,dimencion])
          pygame.draw.circle(screen,color,[self.x,self.y],self.radio,True)

      def centerx(self):
	  return self.x + self.radio

      def centery(self):
	  return self.y + self.radio

      def collidecirculo(self,circulo):
          distancia = math.sqrt( (self.x - circulo.x)**2 + (self.y - circulo.y)**2)
	  if distancia <= self.radio + circulo.radio:
             return True
	  return False

      def collidelist(self,lista_de_circulos):
	  for index in range(len(lista_de_circulos)):
	      if self.collidecirculo(lista_de_circulos[index]):
                 return index
          return -1

      def move(self,x,y):
          self.x+=x
	  self.y+=y
