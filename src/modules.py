from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn
import numpy as np

def set_pixel(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	# glFlush()

def color_pixel(width, height, x, y, size):
	rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size , GL_RGB, GL_UNSIGNED_BYTE, None)
	return list(rgb)

def clearCanvas():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(1, 1, 1, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glScalef(scale, scale, 0)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)

def pintar(str,matrix,x,y):	
	size = 2
	if(str == 'main'):
		r,g,b = 0, 0, 0
		color1 = ()
		war_orange = (255/255,154/255,77/255)
		# orange2
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 1:
					set_pixel((y - j)*size, (x - i)*size, r, g, b, size)
				#Color cuernos
				if matrix[i][j] == 2:
					set_pixel((y - j)*size, (x - i)*size,war_orange[0], war_orange[1], war_orange[2], size)
				#Color del arma
				if matrix[i][j] == 3:
					set_pixel((y - j)*size, (x - i)*size,0/255, 190/255, 244, size)
				# # Color Armadura
				if matrix[i][j] == 4:
					set_pixel((y - j)*size, (x - i)*size,24/255, 117/255 , 117/255, size)
				# # color pecho			
				if matrix[i][j] == 5:
					set_pixel((y - j)*size, (x - i)*size,255/255, 157/255 , 0/255, size)
	
	if(str == 'princesa'):
		r ,g ,b = 0, 0, 0
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 1:
					set_pixel((y - j)*size, (x - i)*size, r, g, b, size)
				#Color cuernos
				if matrix[i][j] == 2:
					set_pixel((y - j)*size, (x - i)*size,255/255, 192/255, 5/255, size)
				#Color del arma
				if matrix[i][j] == 3:
					set_pixel((y - j)*size, (x - i)*size,244, 244, 244, size)
				# # Color Armadura
				if matrix[i][j] == 4:
					set_pixel((y - j)*size, (x - i)*size,10/255, 10/255 , 10/255, size)
				# # color peto			
				if matrix[i][j] == 5:
					set_pixel((y - j)*size, (x - i)*size,255/255, 255/255 , 0/255, size)
	

def despintar(str,matrix,x,y):
	size = 2
	if(str == 'main'):
		r,g,b = 1, 1, 1
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				set_pixel((y - j)*size, (x - i)*size, r, g, b, size)

# esto generar un conflicto
#Prueba de fallo
# esto lo escribo yo (widmaro) y generara algun conflicto