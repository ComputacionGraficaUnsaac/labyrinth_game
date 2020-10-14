# pip install PyOpenGL
# pip install pygame

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
import random as rdn

### Algorithm ###

def set_point(x, y, r, g, b, size):
	glColor3f(r, g, b)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()
	
	pygame.display.flip()
	print("{}\t{}".format(x, y))
	pygame.time.wait(1)

def DDA(x0, y0, x1, y1, r, g, b, size):
	dx = x1 - x0
	dy = y1 - y0

	x = x0
	y = y0

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	xi = dx / steps
	yi = dy / steps

	set_point(round(x), round(y), r, g, b, size)
	for k in range(steps):
		x += xi
		y += yi
		set_point(round(x), round(y), r, g, b, size)

def Bressennham(x0, y0, x1, y1, r, g, b, size):
	# |m| < 1
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)

	""" if x1 - x0 == 0:
		m = 0
	else: 
		m = (y1 - y0) / (x1 - x0) """

	r = 2 * dy
	s = 2 * dy - 2 * dx

	p = 2 * dy - dx

	if x0 > x1:
		x = x1
		y = y1
		x1 = x0
	else:
		x = x0
		y = y0

	set_point(x, y, 1, 0, 0, size)
	k = 0
	# print(m, dx, dy)
	while k < dx:
		x += 1
		if p < 0:
			p = p + r
		else:
			y += 1
			p = p + s
		""" if m < 1:#dx == 0:
			set_point(x, y, r, g, b, size)
		else:
			set_point(x, y, r, g, b, size) """
		set_point(x, y, r, g, b, size)
		k += 1

def Circle2v(xc, yc, radio, r, g, b, size):
	# set_point(xc + radio, yc, 0, 0, 1, size)
	# set_point(xc - radio, yc, 0, 1, 0, size)

	for x in range(-radio, radio + 1):
		y = math.ceil(math.sqrt(radio * radio - x * x))

		set_point(xc + x, yc + y, r, g, b, size)
		set_point(xc - x, yc - y, r, g, b, size)

def Circle4v(xc, yc, radio, r, g, b, size):
	# set_point(xc, yc + radio, 0, 1, 0, size)
	# set_point(xc, yc - radio, 0, 0, 1, size)

	for x in range(radio + 1):
		y = math.ceil(math.sqrt(radio * radio - x * x))
		set_point(xc + x, yc + y, r, g, b, size)
		set_point(xc - x, yc + y, r, g, b, size)
		set_point(xc - x, yc - y, r, g, b, size)
		set_point(xc + x, yc - y, r, g, b, size)

def Circle8v(xc, yc, radio, r, g, b, size):
	# set_point(xc, yc + radio, 0, 1, 0, size)
	# set_point(xc, yc - radio, 0, 0, 1, size)
	# set_point(xc + radio, yc, 0, 1, 0, size)
	# set_point(xc - radio, yc, 0, 0, 1, size)

	for x in range(math.floor(radio / math.sqrt(2)) + 1):
		y = math.ceil(math.sqrt(radio * radio - x * x))
		set_point(xc + x, yc + y, r, g, b, size)
		set_point(xc - x, yc + y, r, g, b, size)
		set_point(xc - x, yc - y, r, g, b, size)
		set_point(xc + x, yc - y, r, g, b, size)

		set_point(xc + y, yc + x, r, g, b, size)
		set_point(xc - y, yc + x, r, g, b, size)
		set_point(xc - y, yc - x, r, g, b, size)
		set_point(xc + y, yc - x, r, g, b, size)

def CirclePM(xc, yc, radio, r, g, b, size):
	# k starting in 0
	x = 0
	y = radio

	p = 1 - radio # (5 / 4) - radio

	""" set_point(xc + x, yc + y, r, g, b, size)
	set_point(xc - x, yc + y, r, g, b, size)
	set_point(xc - x, yc - y, r, g, b, size)
	set_point(xc + x, yc - y, r, g, b, size)

	set_point(xc + y, yc + x, r, g, b, size)
	set_point(xc - y, yc + x, r, g, b, size)
	set_point(xc - y, yc - x, r, g, b, size)
	set_point(xc + y, yc - x, r, g, b, size) """

	while x < y:
		# x += 1
		if p < 0:
			p += 2 * x + 1
		else:
			y -= 1
			p += 2 * (x - y) + 1

		set_point(xc + x, yc + y, r, g, b, size)
		set_point(xc - x, yc + y, r, g, b, size)
		set_point(xc - x, yc - y, r, g, b, size)
		set_point(xc + x, yc - y, r, g, b, size)

		set_point(xc + y, yc + x, r, g, b, size)
		set_point(xc - y, yc + x, r, g, b, size)
		set_point(xc - y, yc - x, r, g, b, size)
		set_point(xc + y, yc - x, r, g, b, size)
		x += 1

def Circle(xc, yc, radio, r, g, b, size):
	angle = 0
	while angle < 45:
		x = radio * math.cos(math.radians(angle))
		y = radio * math.sin(math.radians(angle))

		set_point(xc + x, yc + y, r, g, b, size)
		set_point(xc - x, yc + y, r, g, b, size)
		set_point(xc - x, yc - y, r, g, b, size)
		set_point(xc + x, yc - y, r, g, b, size)

		set_point(xc + y, yc + x, r, g, b, size)
		set_point(xc - y, yc + x, r, g, b, size)
		set_point(xc - y, yc - x, r, g, b, size)
		set_point(xc + y, yc - x, r, g, b, size)

		angle += 1 / radio

### Draw
def display_openGL(width, height, scale):
	pygame.display.set_mode((width, height), pygame.OPENGL)

	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glScalef(scale, scale, scale)

	gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)

def main():
	scale = 5
	width, height = scale * 150, scale * 150

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)

	set_point(0, 0, 1, 1, 1, scale)

	# DDA(0, 0, 10, 0, 0/255, 255/255, 0/255, scale)
	# DDA(0, 0, 0, 10, 0/255, 255/255, 0/255, scale)
	# Bressennham(0, 0, 6, 7, 0, 1, 0, scale)
	# Circle2v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circle4v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circle8v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	Circle(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# CirclePM(0, 0, 60, 255/255, 0/255, 0/255, scale)

	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()