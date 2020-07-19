#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Создаем функтор (обьект которые ведет себя как фунция)
class Functor(object):
	def __init__(self, num):
		self.__Num = num

	def __call__(self, param):
		return self.__Num * param

F = Functor(3)

print(F(4))
print(F("Вася\n"))