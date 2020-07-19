#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Создаем мульти-функтор
class multifunctor(object):
	def __init__(self, default):
		self.__Default = default
		self.__Functions = []

	def less_than(self, number):
		def reg_func(function):
			self.__Functions.append((number, function))
			return self
		return reg_func

	def __get__(self, instance, owner):
		self.__Instance = instance
		return self

	def __call__(self, x, *args, **kwargs):
		for number, function in self.__Functions:
			if x < number:
				return function(self.__Instance, x, *args, **kwargs)
		else:
			return self.__Default(self.__Instance, x, *args, **kwargs)

class MyFunctor(object):
	def __init__(self, param):
		self.__Param = param

	@multifunctor
	def __call__(self, x):
		return 0.0

	@__call__.less_than(0.0)
	def __call__(self, x):
		return -1.0

	@__call__.less_than(2.0)
	def __call__(self, x):
		return 1.0

	@__call__.less_than(5.0)
	def __call__(self, x):
		return self.__Param * x

F = MyFunctor(2.0)
print(F(-7.0))
print(F(1.5))
print(F(3.0))
print(F(7.0))
