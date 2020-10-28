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

# def atacar_iz(x,y,xa,ya,f):
# 	despintar()
# 	M = pj.warrior_main6()
# 	time.sleep(0.5)
# 	pintar('main',M,x,y)
# 	time.sleep(1)
# 	despintar('main',M,x,y)
# 	M = pj.warrior_main1()
# 	pintar('main',M,x,y+2)
# 	# M = pj.warrior_main5()
# 	# pintar('main',M,x,y)
# 	# despintar('main',M,x,y)
# 	# M = pj.warrior_main1()
# 	# pintar('main',M,x,y)

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
	# pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)-2)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)-2)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)-2)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)-1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)-1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)-1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26))*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26))*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26))*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)+1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)+1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)+1)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25))*25,int(int(ya/26)+2)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)+1)*25,int(int(ya/26)+2)*26)
	# pintar('piso1',pj.piso1(),int(int(xa/25)-1)*25,int(int(ya/26)+2)*26)
	
	# pintar('piso1',pj.piso1(),x,y)
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

def main():
	scale = 2
	# width, height = scale * 300, scale * 300
	width, height = 1280,720
	pygame.init()
	# pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)

	x, y = 0, 125
	for i in range(0,201,25):
		for j in range(0,339,26):
			pintar('piso1',pj.piso1(),i,j)
			pintar('piso1',pj.piso1(),-i,-j)
			pintar('piso1',pj.piso1(),i,-j)
			pintar('piso1',pj.piso1(),-i,j)

	j = 0
	for i in range(0,350,26):
		pintar('Pared1',pj.Pared1(),j,i)
		pintar('Pared1',pj.Pared1(),-j,i)

	pintar('main',pj.warrior_main5(),0,125)	 
	pintar('princesa',pj.princesa(),150,150)
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
				x += 0
				y += -2
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
				x += 0
				y += 2
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
				x += 5
				y += 0				
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
				x += -5
				y += 0				
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
				x += 0
				y += -2			
				atacar_iz(x,y,xa,ya,f)
				time.sleep(0.1)
				f += 1
		glFlush()
if __name__ == '__main__':
	main()











