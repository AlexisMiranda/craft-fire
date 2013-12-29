# coding: latin-1
from circulo import Circulo
from rectangulo import Rectangulo
from movimiento import Movimiento
from disparo import Disparo
from nave_enemiga import NaveEnemiga
from nave_jugador import NaveJugador
import pygame,sys
from etapa import Etapa
from bala import Bala
if __name__ == '__main__':
   pygame.init()
   size  = width, height = 620, 640
   speed = [2, 2]
   black = 0, 0, 0
   screen = pygame.display.set_mode(size)
   #imagen=pygame.transform.scale(pygame.image.load("a.png"),[100,130])
   imagen2=pygame.transform.scale(pygame.image.load("b.png"),[220,220])
   imagen3=pygame.transform.scale(pygame.image.load("b.png"),[110,110])
   tiempo=0
   xx=0
   yy=0
   figura_enemigo1=Rectangulo("enemigo1.png",20,20,100,10)
   bala_enemigo1=[Disparo([Rectangulo("b.png",5,5,100,100) for i in range(4)],4) for i in range(40)]
   enemigo1=NaveEnemiga(screen,figura_enemigo1,bala_enemigo1,None,100)
   figura_jugador=Rectangulo("jugador.png",30,30,100,10)
   bala_jugador=Disparo([Rectangulo("b.png",5,5) for i in range(1)],1) 
   jugador=NaveJugador(screen,figura_jugador,Rectangulo("b.png",5,5),None,500)
   salir=False
   frs=pygame.time.Clock()
   etapa1=Etapa(screen)
   etapa1.etapa1()
   bala_1=Bala(Rectangulo("b.png",5,5),True)
   while not salir:
     screen.fill([250,250,250])
     #etapa1.update(tiempo,[jugador])
     #bala_1.disparo_horizontal(screen,100,100,1,4)
     bala_1.disparo_vertical_circular(screen,100,100,1,1,4,tiempo,20)
     for even in pygame.event.get():
          if even.type == pygame.QUIT: sys.exit()
          if even.type == pygame.KEYDOWN :
             if even.key == pygame.K_UP    : jugador.evenKeydownUp()
             if even.key == pygame.K_DOWN  : jugador.evenKeydownDown()
             if even.key == pygame.K_LEFT  : jugador.evenKeydownLeft()
             if even.key == pygame.K_RIGHT : jugador.evenKeydownRight()
             if even.key == pygame.K_ESCAPE: sys.exit()
             if even.key == pygame.K_a     : jugador.disparar_bala()
          if even.type == pygame.KEYUP   :
             if even.key == pygame.K_LEFT  : jugador.evenKeyupLeft()
             if even.key == pygame.K_RIGHT : jugador.evenKeyupRight()
             if even.key == pygame.K_UP    : jugador.evenKeyupUp()
             if even.key == pygame.K_DOWN  : jugador.evenKeyupDown()

     #bala.disparo_escudo(screen,300,100,-1,-1,5) 
     #bala.disparo_vertical_circular(screen,300,100,-30,-30,5,tiempo) 
     #bala.disparo_diagonal(screen,300,400,1,1) 
     #enemigo1.update([jugador],4,4,tiempo,10,4)
     #jugador.update([enemigo1],tiempo)
     frs.tick(40)
     pygame.display.update()
     tiempo+=1
   pygame.quit()
