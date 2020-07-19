#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Создаем мультиметод
class overload(object):
	def __init__(self, default = None):
		self.__Default = default
		self.__Functions = []

	def register(self, var_type):
		def register_func(function):
			self.__Functions.append((var_type, function))
			return self
		return register_func

	def __get__(self, instance, owner):
		self.__Instance = instance
		return self

	def __call__(self, x, *args, **kwargs):
		for var_type, function in self.__Functions:
			if isinstance(x, var_type):
				return function(self.__Instance, x, *args, **kwargs)
		else:
			return self.__Default(self.__Instance, x, *args, **kwargs)

class Example(object):
	def __init__(self):
		pass

	@overload
	def func(self, x):
		print("Method for any type", type(x))

	@func.register(int)
	def func(self, x):
		print("Method for int")

	@func.register(str)
	def func(self, x, y):
		print("Method for str")

E = Example()
E.func(25)
E.func("Вася", 1)
E.func(46.34)