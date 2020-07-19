#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Числоподобный объект
class quaternion (object):
	def __init__(self, x, y, z, a = 0.0):
		self.__Data = (x, y, z, a)

	def __str__(self):
		return "{0}i + {1}j + {2}k + {3}".format(*self.__Data)

	def __add__(self, other):
		x1, y1, z1, a1 = self.__Data
		if isinstance(other, (float, int)):
			return quaternion(x1, y1, z1, a1 + other)
		else:
			x2, y2, z2, a2 = other.__Data
			return quaternion(x1 + x2, y1 + y2, z1 + z2, a1 + a2)

	def __sub__(self, other):
		x1, y1, z1, a1 = self.__Data
		if isinstance(other, (float, int)):
			return quaternion(x1, y1, z1, a1 - other)
		else:
			x2, y2, z2, a2 = other.__Data
			return quaternion(x1 - x2, y1 - y2, z1 - z2, a1 - a2)

	def __rsub__(self, other):
		x1, y1, z1, a1 = self.__Data
		return quaternion(-x1, -y1, -z1, -a1 + other)

	def __neg__(self):
		x1, y1, z1, a1 = self.__Data
		return quaternion(-x1, -y1, -z1, -a1)

	def __mul__(self, other):
		x1, y1, z1, a1 = self.__Data
		if isinstance(other, (float, int)):
			return quaternion(x1 * other, y1 * other, z1 * other, a1 * other)
		else:
			x2, y2, z2, a2 = other.__Data
			return quaternion(
				x = a1 * x2 + x1 * a2 + z1 * y2 - y1 * z2,
				y = a1 * y2 + y1 * a2 + x1 * z2 - z1 * x2,
				z = a1 * z2 + z1 * a2 + y1 * x2 - x1 * y2,
				a = a1 * a2 - x1 * x2 - y1 * y2 - z1 * z2
			)

	__rmul__ = __mul__
	__radd__ = __add__

p = quaternion(1.0, 2.0, 3.0, 4.0)
q = quaternion(10.0, 20.0, 30.0, 40.0)

print("p = ", p)
print("q = ", q)

print("p + q =", p + q) # p.__add__(q)
print("p + 1 =", p + 1) # p.__add__(1)
print("1 + q =", 1 + q) # q.__radd__(1)

print("p - q =", p - q) # p.__sub__(q)
print("p - 1 =", p - 1) # p.__sub__(1)
print("1 - q =", 1 - q) # q.__rsub__(1)

print("-p =", -p) # p.__neg__()

print("p * q =", p * q) # p.__mul__(q)
print("p * 1 =", p * 1) # p.__mul__(1)
print("1 * q =", 1 * q) # q.__rmul__(1)