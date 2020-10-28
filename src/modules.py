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

def Traslate(vertices, tx, ty):
	T = [
		[1, 0, tx], 
		[0, 1, ty], 
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

def ReflexionX(vertices):
	T = [
		[-1, 0, 0], 
		[0, 1, 0], 
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

def ReflexionY(vertices):
	T = [
		[1, 0, 0], 
		[0,-1, 0], 
		[0, 0, 1]
	]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

def pintar(str,matrix,x,y):	
	size = 2	
	if(str == 'main'):
		size = 2
		color1 = (0/255,0/255,0/255)		 # color negro borde
		color2 = (252/255, 160/255, 68/255)# color naranja cuernos
		color3 = (60/255, 188/255, 252/255) # color celeste arma
		color4 = (0/255, 136/255, 136/255)# color armadura
		color5 = (252/255, 252/255 , 252/255) # color blanco

	if(str == 'princesa'):
		size = 2
		color1 = (0/255,0/255,0/255)
		color2 = (255/255,192/255,5/255)
		color3 = (244/255,244/255,244/255)
		color4 = (10/255,10/255,10/255)
		color5 = (255/255,157/255,0/255)
	
	if(str == 'piso1'):		
		size = 2
		color1 = (55/255, 67/255, 100/255)  # color fondo
		color2 = (142/255, 158/255, 183/255)# color bloques
		color3 = (93/255, 106/255, 140/255) # color sobras de bloques
		color4 = (0/255, 136/255, 136/255)# color armadura
		color5 = (252/255, 252/255 , 252/255) # color blanco

	if(str == 'muerte'):		
		size = 2
		color1=(0/255, 0/255, 0/255)# colo Marco claro
		color2 =(193/255, 80/255, 60/255)  # color ladrillo
		color3 = (47/255, 60/255, 87/255)# Color separacion de bloques
		color4 = (91/255, 106/255, 133/255) # color Marco oscuro
		color5 = (0/255, 136/255, 136/255)# color armadura		
	
	if(str == 'pared1'):		
		size = 2
		color1=(140/255, 156/255, 179/255)# colo Marco claro
		color2 =(193/255, 203/255, 224/255)  # color ladrillo
		color3 = (47/255, 60/255, 87/255)# Color separacion de bloques
		color4 = (91/255, 106/255, 133/255) # color Marco oscuro
		color5 = (0/255, 136/255, 136/255)# color armadura	

	if(str == 'soldado1'):		
		size = 2
		color1 = (0/255,0/255,0/255)# colo Marco claro
		color2 =(193/255, 203/255, 224/255)  # color ladrillo
		color3 = (78/255, 59/255, 49/255)# Color separacion de bloques
		color4 = (255/255, 0/255, 0/255) # color de capa y
		color5 = (156/255, 156/255, 156/255)# color armadura
	
	


	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				set_pixel((y - j)*size, (x - i)*size, color1[0], color1[1], color1[2], size)
			
			if matrix[i][j] == 2:
				set_pixel((y - j)*size, (x - i)*size, color2[0], color2[1], color2[2], size)
			
			if matrix[i][j] == 3:
				set_pixel((y - j)*size, (x - i)*size, color3[0], color3[1], color3[2], size)
			
			if matrix[i][j] == 4:
				set_pixel((y - j)*size, (x - i)*size, color4[0], color4[1], color4[2], size)
			
			if matrix[i][j] == 5:
				set_pixel((y - j)*size, (x - i)*size, color5[0], color5[1], color5[2], size)
						


def despintar(str,matrix,x,y):
	size = 2
	if(str == 'main'):
		r,g,b = 1, 1, 1
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if(matrix[i][j] != 0):
					set_pixel((y - j)*size, (x - i)*size, r, g, b, size)

