#!/usr/bin/python3
# -*- coding: utf-8 -*-

from OpenGL.GL import *

_MAX_LIGHTS = 8

# Точечный источник света
class Light(object):

	__FreeNumbers = [eval("GL_LIGHT{0}".format(x)) for x in range(0, _MAX_LIGHTS)]

	# number - номер лампочки от 0 до 8 включительно
	def __init__(self, number = None):
		if number is not None:
			self.__Number = Light.__FreeNumbers[number]
			if self.__Number is None:
				raise ValueError("Number already taken")
			Light.__FreeNumbers[number] = None
		else:
			for k in range(0, _MAX_LIGHTS):
				if Light.__FreeNumbers[k] is None:
					continue
				self.__Number = Light.__FreeNumbers[k]
				Light.__FreeNumbers[k] = None
				break
			else:
				raise ValueError("No free numbers")

	def __del__(self):
		for k in range(0, _MAX_LIGHTS):
			if Light.__FreeNumbers[k] is None:
				Light.__FreeNumbers[k] = self.__Number

	@property
	def enabled(self):
		return glIsEnabled(self.__Number)

	@enabled.setter
	def enabled(self, value):
		if value:
			glEnable(self.__Number)
		else:
			glDisable(self.__Number)

	ambient = property(lambda self: self.__Ambient)

	@ambient.setter
	def ambient(self, value):
		glLightfv(self.__Number, GL_AMBIENT, value)
		self.__Ambient = value