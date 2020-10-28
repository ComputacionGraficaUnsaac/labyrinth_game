# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8
import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

import pjs as pj

from modules import *
### Algorithm ###
def ParedHorizontal(x,y,m):
	for j in range(y,m,26):
		pintar('pared1',pj.pared1(),x,j)
  
def ParedVertical(x,y,m):
	for j in range(y,m,26):
		pintar('pared1',pj.pared1(),j,x)


def fondo(xa,ya):
	pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)-2)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)-2)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)-2)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)-1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)-1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)-1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26))*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26))*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26))*26)
	pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)+1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)+1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)+1)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)+2)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)+2)*26)
	pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)+2)*26)

def atacar_iz(x,y,f):
	despintar('main',pj.warrior_main1(),x,y)
	fondo(x,y)
	M = pj.warrior_main_a()
	# time.sleep(0.5)
	pintar('main',M,x,y)

def atacar_de(x,y,f):
	despintar('main',pj.warrior_main1(),x,y)
	fondo(x,y)
	M = pj.r_warrior_main_a()
	# time.sleep(0.5)
	pintar('main',M,x,y)


def moveWarrior_der(x,y,xa,ya,f):
	if(f % 6 == 0):		
		M = pj.r_warrior_main1()
		P = pj.r_warrior_main6()
	if(f % 6 == 1):
		M = pj.r_warrior_main2()
		P = pj.r_warrior_main1()
	if(f % 6 == 2):
		M = pj.r_warrior_main3()
		P = pj.r_warrior_main2()
	if(f % 6 == 3):
		M = pj.r_warrior_main4()
		P = pj.r_warrior_main3()
	if(f % 6 == 4):
		M = pj.r_warrior_main5()
		P = pj.r_warrior_main4()
	if(f % 6 == 5):
		M = pj.r_warrior_main6()
		P = pj.r_warrior_main5()

	despintar('main',P,xa,ya)
	fondo(xa,ya)

	pintar('main',M,x,y)

def moveWarrior_iz(x,y,xa,ya,f):	

	if(f % 6 == 0):
		M = pj.warrior_main1()
		P = pj.warrior_main6()
	if(f % 6 == 1):
		M = pj.warrior_main2()
		P = pj.warrior_main1()
	if(f % 6 == 2):
		M = pj.warrior_main3()
		P = pj.warrior_main2()
	if(f % 6 == 3):
		M = pj.warrior_main4()
		P = pj.warrior_main3()
	if(f % 6 == 4):
		M = pj.warrior_main5()
		P = pj.warrior_main4()
	if(f % 6 == 5):
		M = pj.warrior_main6()
		P = pj.warrior_main5()

	# x += 0
	# y += -5			
	# pintar('piso1',pj.piso1(),x,y)	
	despintar('main',P,xa,ya)
	fondo(xa,ya)
	
	# pintar('piso1',pj.piso1(),x,y)
	pintar('main',M,x,y)
	f += 1

def pintar_laberinto():
	#Pintar paredes
	ParedHorizontal(183,-240,345)
	ParedHorizontal(-152,-278,280)
	ParedVertical(-298,-210,230)
	ParedVertical(322,-100,230)
	# ParedHorizontal(-10,0,10)
	#Piedras
	# ParedHorizontal(-10,-100,-90)
	# ParedHorizontal(-10,-200,-190)
	# ParedHorizontal(100,-200,-190)
	# ParedHorizontal(100,-100,-90)
	# ParedHorizontal(100,0,10)

def main():
	scale = 2
	# width, height = scale * 300, scale * 300
	width, height = 1280,720
	pygame.init()
	# pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)

	x, y = 0, 125
	xm, ym = 0, 0
	for i in range(0,201,25):
		for j in range(0,339,26):
			pintar('piso1',pj.piso1(),i,j)
			pintar('piso1',pj.piso1(),-i,-j)
			# aux = ReflexionY([x,y,1])
			# j1 = aux[0][1]
			# i = aux[0][0]
			pintar('piso1',pj.piso1(),i,-j)
			pintar('piso1',pj.piso1(),-i,j)

	pintar('main',pj.warrior_main5(),0,125)	 
	pintar_laberinto()
	pintar('princesa',pj.princesa(),175,-270)
	pintar('muerte',pj.muerte(),xm,ym)
	pintar('soldado1',pj.soldado1(),155,-245)
	f = 0
	iz = True
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT :
				print("K_LEFT")
				xa = x
				ya = y
				aux = Traslate([[x, y, 1]], 0, -2)
				x = aux[0][0]
				y = aux[0][1]
				# x += 0
				# y += -2
				iz = True
				if (iz):
					moveWarrior_iz(x,y,xa,ya,f)
				else:
					moveWarrior_der(x,y,xa,ya,f)

				time.sleep(0.1)
				f += 1

			elif event.key == pygame.K_RIGHT:
				print("K_RIGHT")
				despintar('main',pj.warrior_main2(),x,y)
				xa = x
				ya = y
				aux = Traslate([[x, y, 1]], 0, 2)
				x = aux[0][0]
				y = aux[0][1]
				# x += 0
				# y += 2
				iz = False
				if (iz):
					moveWarrior_iz(x,y,xa,ya,f)
				else:
					moveWarrior_der(x,y,xa,ya,f)
				time.sleep(0.1)
				f += 1

			elif event.key == pygame.K_UP :
				print("K_UP")				
				xa = x
				ya = y
				aux = Traslate([[x, y, 1]], 2, 0)
				x = aux[0][0]
				y = aux[0][1]
				# x += 5
				# y += 0				
				if (iz):
					moveWarrior_iz(x,y,xa,ya,f)
				else:
					moveWarrior_der(x,y,xa,ya,f)
				time.sleep(0.1)
				f += 1

			elif event.key == pygame.K_DOWN :
				print("K_DOWN")
				xa = x
				ya = y
				aux = Traslate([[x, y, 1]], -2, 0)
				x = aux[0][0]
				y = aux[0][1]
				# x += -5
				# y += 0				
				if (iz):
					moveWarrior_iz(x,y,xa,ya,f)
				else:
					moveWarrior_der(x,y,xa,ya,f)
				time.sleep(0.1)
				f += 1
				# pintar('piso1',pj.piso1(),x,y)
				# pintar('main',pj.warrior_main2(),x,y)
				
			if event.key == pygame.K_a:
				print("K_a")
				xa = x
				ya = y	
				aux = Traslate([[x, y, 1]], 0, -2)
				x = aux[0][0]
				y = aux[0][1]
				# x += 0
				# y += -2			
				if (iz):
					atacar_iz(xa,ya,f)
				else:
					atacar_de(xa,ya,f)
				time.sleep(0.1)
				f += 1

			if event.key == pygame.K_j:
				print("K_j")						
				xm += 0
				ym += -5
				fondo(xm,ym)
				pintar('muerte',pj.muerte(),xm,ym)
				time.sleep(0.1)		

			if event.key == pygame.K_l:
				print("K_l")						
				xm += 0
				ym += 5
				fondo(xm,ym)
				pintar('muerte',pj.muerte(),xm,ym)
				time.sleep(0.1)		

			if event.key == pygame.K_k:
				print("K_k")						
				xm += -5
				ym += 0
				fondo(xm,ym)
				pintar('muerte',pj.muerte(),xm,ym)
				time.sleep(0.1)

			if event.key == pygame.K_i:
				print("K_i")						
				xm += 5
				ym += 0
				fondo(xm,ym)
				pintar('muerte',pj.muerte(),xm,ym)
				time.sleep(0.1)


		glFlush()
if __name__ == '__main__':
	main()











