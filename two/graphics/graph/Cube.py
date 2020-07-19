#!/usr/bin/python3
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from .draw_context import figure, DrawContext

class Cube(object):

	# Размер угла и угол поворота
	def __init__(self, a, angle = 0.0):
		self.__A = a
		self.__Angle = angle

	a = property (lambda self: self.__A)
	angle = property (lambda self: self.__Angle)

	@angle.setter
	def angle(self, value):
		self.__Angle = value

	def draw(self):
		q = self.a / 2
		glColor4f(1.0, 1.0, 0.0, 1.0)
		with DrawContext() as DC:
			glRotatef(self.angle, 1.0, 1.0, 1.0)
			with figure(GL_TRIANGLES):
				for w in (q, -q):
					glVertex3f(-q, -q, w)
					glVertex3f(-q, q, w)
					glVertex3f(q, q, w)
					glVertex3f(-q, -q, w)
					glVertex3f(q, -q, w)
					glVertex3f(q, q, w)
				for w in (q, -q):
					glVertex3f(-q, w, -q)
					glVertex3f(-q, w, q)
					glVertex3f(q, w, q)
					glVertex3f(-q, w, -q)
					glVertex3f(q, w, -q)
					glVertex3f(q, w, q)