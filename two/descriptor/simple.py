#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress

# Создание дескриптора
class simple_property(object):
	def __init__(self, varname):
		self.__VarName = varname

	def __get__(self, instance, owner):
		return getattr(instance, self.__VarName)

	def __set__(self, instance, value):
		with suppress(AttributeError):
			Old = getattr(instance, self.__VarName)
			if not isinstance(value, type(Old)):
				raise TypeError("Type mismatch")
		setattr(instance, self.__VarName, value)
		# return value

	def __delete__(self, instance):
		delattr(instance, self.__VarName)

class Example(object):
	def __init__(self, one, two):
		self.One = one
		self.Two = two

	one = simple_property("One")
	two = simple_property("Two")

E = Example(1, "ggg")
print(E.one)
print(E.two)

del E.two
E.one = 25
print(E.one)
E.two = 25
print(E.two)