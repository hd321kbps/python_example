#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Создание менеджера контекста
@contextmanager
def figure(mode):
	glBegin(mode)
	try:
		yield
	finally:
		glEnd()

class DrawContext(object):
	def __init__(self):
		pass

	def __enter__(self):
		# Запоминает сцену
		glPushMatrix()
		return self

	def __exit__(self, exc_type, ext_value, traceback ):
		glPopMatrix()
		return False