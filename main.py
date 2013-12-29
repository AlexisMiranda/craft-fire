# coding: latin-1
from circulo import Circulo
from rectangulo import Rectangulo
from movimiento import Movimiento
from bala import Bala
from nave_enemiga import NaveEnemiga
from nave_jugador import NaveJugador
import pygame,sys
from etapa import Etapa
if __name__ == '__main__':
   pygame.init()
   size  = width, height = 620, 640
   speed = [2, 2]
   black = 0, 0, 0
   screen = pygame.display.set_mode(size)
   #imagen=pygame.transform.scale(pygame.image.load("a.png"),[100,130])
   imagen2=pygame.transform.scale(pygame.image.load("b.png"),[220,220])
   imagen3=pygame.transform.scale(pygame.image.load("b.png"),[110,110])
   #rectangulo= Rectangulo(imagen,200,200)
   circulo  = Circulo("b.png",300,100,100) 
   circulo2 = Circulo("b.png",100,100,50)
   movimiento=Movimiento(circulo)
   bala=Bala([Rectangulo("b.png",100,300,50,50) for i in range(2)],2,True)
   tiempo=0
   xx=0
   yy=0
   figura_enemigo1=Rectangulo("enemigo1.png",100,10,20,20)
   bala_enemigo1=[Bala([Rectangulo("b.png",100,100,5,5) for i in range(4)],4) for i in range(40)]
   enemigo1=NaveEnemiga(screen,figura_enemigo1,bala_enemigo1,None,100)
   figura_jugador=Rectangulo("jugador.png",100,300,30,30)
   bala_jugador=Bala([Rectangulo("b.png",100,100,5,5) for i in range(1)],1) 
   jugador=NaveJugador(screen,figura_jugador,Rectangulo("b.png",100,100,5,5),None,500)
   salir=False
   frs=pygame.time.Clock()
   etapa1=Etapa(screen)
   etapa1.etapa1()
   while not salir:
     screen.fill([250,250,250])
     etapa1.update(tiempo,[jugador])
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

     #pygame.draw.rect(screen,[23,23,250],[23,23,100,100])
     #pygame.draw.circle(screen,[23,23,250],[123,223],10)
     #rectangulo.update(screen)
     #rectangulo.rectangulo=rectangulo.rectangulo.move(1,0)
     #(x,y)=pygame.mouse.get_pos()
     #movimiento.mover_vertical(screen,-1)
     #movimiento.mover_zig_zag(screen,1,1,tiempo)
     #movimiento.mover_circular(screen,8,8,tiempo,5)
     #movimiento.figura.move(1,2)
     #movimiento.figura.update(screen)
     """circulo2.update(screen)
     circulo2.x=x
     circulo2.y=y
     """

     """for even in pygame.event.get():
          if even.type == pygame.QUIT: salir=True
     """
     #bala.disparo_escudo(screen,300,100,-1,-1,5) 
     #bala.disparo_vertical_circular(screen,300,100,-30,-30,5,tiempo) 
     #bala.disparo_diagonal(screen,300,400,1,1) 
     #enemigo1.update([jugador],4,4,tiempo,10,4)
     #jugador.update([enemigo1],tiempo)
     frs.tick(40)
     pygame.display.update()
     tiempo+=1
   pygame.quit()
