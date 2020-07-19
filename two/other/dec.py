#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Мультиметоды - это несколько методов из которых вызываеться только один или другой

class multimethod(object):
	def __init__(self):
		self.__List = []

	def variant(self, check = lambda *args: True):
		def append(func):
			self.__List.append((check, func))
			return self
		return append

	def __call__(self, *args):
		for (check, f) in self.__List:
			if check(*args):
				return f(self.__Caller, *args)
		else:
			raise AttributeError()

	def __get__(self, instance, type):
		self.__Caller = instance
		return self

class Model(object):

	func = multimethod()

	@func.variant(lambda a, b: a > b)
	def func(self, a, b):
		return "Вариант 1"

	@func.variant(lambda a, b: True)
	def func(self, a, b):
		return "Вариант 2"
	# Или
	# func = func.variant(???)(func)

if __name__ == "__main__":
		M = Model()

		print(M.func(2, 3))
		print(M.func(3, 2))
	# @property
	# def prop(self):
	# 	return 2
	# # Или
	# def prop(self):
	# 	return 2
	# prop = property (prop)
