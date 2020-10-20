# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

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


def main():
	scale = 2
	# width, height = scale * 300, scale * 300
	width, height = 1280,720
	pygame.init()
	# pygame.display.set_caption('C.G. I')
	display_openGL(width, height, scale)

	x, y = 0, 0
	pintar('main',pj.warrior_main1(),0,0)	

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT :
				print("K_LEFT")
				despintar('main',pj.warrior_main1(),x,y)
				x += 0
				y += -5				
				pintar('main',pj.warrior_main1(),x,y)
			elif event.key == pygame.K_RIGHT:
				print("K_RIGHT")
				despintar('main',pj.warrior_main1(),x,y)
				x += 0
				y += 5
				# x, y = MoveDefender(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
				pintar('main',pj.warrior_main1(),x,y)
			elif event.key == pygame.K_UP :
				print("K_UP")
				despintar('main',pj.warrior_main1(),x,y)
				x += 5
				y += 0
				pintar('main',pj.warrior_main1(),x,y)
				# x, y = MoveDefender(x, y , sx, sy,59/255, 131/255, 189/255, scale)
				# set_pixel(50, 50, 255/255, 255/255, 255/255, 3)
			elif event.key == pygame.K_DOWN :
				print("K_DOWN")
				despintar('main',pj.warrior_main1(),x,y)
				x += -5
				y += 0
				pintar('main',pj.warrior_main1(),x,y)
				# x, y = MoveDefender(x, y, sx, sy, 59/255, 131/255, 189/255, scale)
		glFlush()
if __name__ == '__main__':
	main()











