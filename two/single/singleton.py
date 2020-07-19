#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Создаем объект синглтон
class Singleton(object):

	__Instance = None

	def __new__(cls, n):
		if cls.__Instance is not None:
			return cls.__Instance
		X = super(cls, cls).__new__(cls)
		cls.__Instance = X
		# X.__must_be_initialized = True
		X.must_be_initialized = True
		return X

	def __init__(self, n):
		if not hasattr(self, "must_be_initialized"):  return
		# try:
		# 	self.__must_be_initialized
		# except AttributeError:
		# 	return
		try:
			self.__N = n
		finally:
			# del self.__must_be_initialized
			del self.must_be_initialized

	n = property(lambda self: self.__N)

S1 = Singleton(1)
print(S1.n)
S2 = Singleton(2)
print(S1.n, S2.n)
print("S1 = {0}". format(id(S1)))
print("S2 = {0}". format(id(S2)))
print(S1 is S2)