import sys, pygame

class Rectangulo(pygame.sprite.Sprite):

      def __init__(self,url_imagen,x,y,tamx,tamy):
          self.imagen        = pygame.transform.scale(pygame.image.load(url_imagen),[tamx,tamy])
	  self.rectangulo    = self.imagen.get_rect()
	  self.rectangulo.x  = x
	  self.rectangulo.y  = y

      def update(self,screen,color=[255,0,0]):
	  screen.blit(self.imagen,self.rectangulo)
          pygame.draw.rect(screen,color,self.rectangulo,True)

      def move(self,vx,vy):
	  self.rectangulo.x += vx
	  self.rectangulo.y += vy

      def collidelist(self,lista_de_rectangulos):
          return self.rectangulo.collidelist(lista_de_rectangulos)
