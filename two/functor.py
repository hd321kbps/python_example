#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Deposit(object):
	def __init__(self, begin, rate):
		self.__Begin = begin
		self.__Rate = rate

	# превратить в функтор
	# def income(self, months):
	def __call__(self, months):
		return (1 + self.__Rate) ** months * self.__Begin

	def __bool__(self):
		return self.__Rate < 1

	def __iadd__(self, addon):
		self.__Begin += addon
		return self

if __name__ == "__main__":
	D = Deposit(100, 0.05)
	D1 = Deposit(100, 2)
	D += 200
	print(D(4))
	# print(D.income(4))
	print(Deposit(200, 0.03)(5))

	if D:
		print(D(10))
	if D1:
		print(D1(10))
	else:
		print("D1 is bad")