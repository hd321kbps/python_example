#!/usr/bin/python3
# -*- coding: utf-8 -*-

import graph

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyApp(graph.Application):

	def __init__(self):
		# Вызывает все из родительского класса
		super().__init__()

		self.__Lamp = graph.Light()
		self.__CubeA = graph.Cube(4.0, 30.0)

	def init_context(self):
		super().init_context()
		self.__Lamp.ambient = (0.0, 0.0, 0.0, 1.0)
		# self.__Lamp.diffuse = (1.0, 1.0, 1.0, 1.0)
		self.__Lamp.enabled = True

	def timer(self, number):
		self.__CubeA.angle += 0.5
		glutTimerFunc(100//30, self.timer, 1)
		glutPostRedisplay()

	def draw_stage(self):
		# Сеанс отрисовки (треугольник)
		# with graph.figure(GL_TRIANGLES):
			# 3 точки на вершину float
			# glVertex3f(0.0, 0.0, 0.0)
			# glVertex3f(1.0, 1.0, 0.0)
			# glVertex3f(0.0, 1.0, 0.5)
			self.__CubeA.draw()