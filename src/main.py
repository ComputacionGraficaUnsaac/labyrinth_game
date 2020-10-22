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

def moveWarrior(x,y,f):
	if(f % 4 == 0):
		M = pj.warrior_main1()
		P = pj.warrior_main4()
	if(f % 4 == 1):
		M = pj.warrior_main2()
		P = pj.warrior_main1()
	if(f % 4 == 2):
		M = pj.warrior_main3()
		P = pj.warrior_main2()
	if(f % 4 == 3):
		M = pj.warrior_main4()
		P = pj.warrior_main3()

	despintar('main',P,x,y)
	x += 0
	y += -5			
	pintar('piso1',pj.piso1(),x,y)	
	pintar('main',M,x,y)
	f += 1

def main():
	scale = 2
	# width, height = scale * 300, scale * 300
	width, height = 1280,720
	pygame.init()
	# pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)

	x, y = 0, 0
	for i in range(-350,350,25):
		for j in range(-400,400,26):
			pintar('piso1',pj.piso1(),i,j)

	pintar('main',pj.warrior_main2(),0,0)	
	pintar('princesa',pj.princesa(),150,150)
	f = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT :
				print("K_LEFT")
				despintar('main',pj.warrior_main2(),x,y)
				x += 0
				y += -2		
				moveWarrior(x,y,f)
				time.sleep(0.2)
				f += 1
				# pintar('piso1',pj.piso1(),x,y)	
				# pintar('main',pj.warrior_main2(),x,y)
			elif event.key == pygame.K_RIGHT:
				print("K_RIGHT")
				despintar('main',pj.warrior_main2(),x,y)
				x += 0
				y += 2
				moveWarrior(x,y,f)
				time.sleep(0.2)
				f += 1
				# pintar('piso1',pj.piso1(),x,y)
				# pintar('main',pj.warrior_main2(),x,y)
			elif event.key == pygame.K_UP :
				print("K_UP")
				despintar('main',pj.warrior_main2(),x,y)
				x += 5
				y += 0
				moveWarrior(x,y,f)
				f += 1
				# pintar('piso1',pj.piso1(),x,y)
				# pintar('main',pj.warrior_main2(),x,y)
			elif event.key == pygame.K_DOWN :
				print("K_DOWN")
				despintar('main',pj.warrior_main2(),x,y)
				x += -5
				y += 0
				moveWarrior(x,y,f)
				f += 1
				# pintar('piso1',pj.piso1(),x,y)
				# pintar('main',pj.warrior_main2(),x,y)

		glFlush()
if __name__ == '__main__':
	main()











