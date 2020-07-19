#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Импотртировать только некоторые функции
# __all__ = ("func1", "z", "method1")
__all__ = ("func1", "z")

def func1(self, m):
	print("func1", 2*m)

def method1(self):
	print("Фигня")

z = property(lambda self: self.Var)

z.setter
def z(self, value):
	self.Var = value