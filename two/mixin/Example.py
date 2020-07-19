#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from mixin import mymix

import mix2
from mix import mixin

# @mymix
@mixin(mix2)
class MyClass(object):

	def method1(self):
		print("method1")

	def method2(self):
		print("method2")

	x = property(lambda self: self.__X)

	@x.setter
	def x(self, value):
		self.__X = value

# Z = MyClass()
# Z.method1()
# Z.method2()
# print(Z.x)

# Z.mix1()
# print(Z.y)

# Z.func1(5)
# Z.z = 25
# print(Z.z)

A = MyClass()
A.x = 10
print(A.x)
# print(A.__X)

A.__X = 25
print(A.__X)
print(A.x)

print(A._MyClass__X)
A._MyClass__X = 53
print (A.x)