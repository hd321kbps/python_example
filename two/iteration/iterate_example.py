#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import random
from random import shuffle

# Создаем итератор
class RSeq(object):
	def __init__(self, first, *args):
		self.__Data = [x for x in first]

	def __iter__(self):
		L = list(self.__Data)
		# random.shuffle(L)
		shuffle(L)
		return RSeqIterator(L)

class RSeqIterator(object):
	def __init__(self, seq):
		self.__Seq = seq

	def __next__(self):
		try:
			return self.__Seq.pop()
		except IndexError as Exc:
			raise StopIteration() from Exc

	# Для использования в цикле
	def __iter__(self):
		return self

R = RSeq([1, 2, 3, 4, 5, 6, 7, 8, 9])

for k in R:
	print(k)
print("-----")

Q = iter(R)

for k in Q:
	print(k)