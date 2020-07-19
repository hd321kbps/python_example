#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress

# Создание дескриптора
class simple_property(object):
	def __init__(self, varname = None):
		self.__VarName = varname

	def __get__(self, instance, owner):
		if instance is None:
			return self
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

	def _adjust_varname(self, classname, attrname):
		if self.__VarName is None:
			self.__VarName = "_{0}__{1}".format(classname, attrname)
		elif self.__VarName[:2] == "__" and self.__VarName[-2:] != "__":
			self.__VarName = "_" + classname + self.__VarName

class MetaExample(type):
	def __init__(self, name, bases, attrs):
		type.__init__(self, name, bases, attrs)
		for at_name, attr in attrs.items():
			if isinstance(attr, simple_property):
				attr._adjust_varname(name, at_name)

class Example(object, metaclass = MetaExample):
	def __init__(self, one, two):
		self.__one = one
		self.__two = two

	one = simple_property()
	two = simple_property()

E = Example(1, "ggg")
print(E.one)
print(E.two)

del E.two
E.one = 25
print(E.one)
E.two = 25
print(E.two)