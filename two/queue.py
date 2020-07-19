#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Queue:
	def __init__(self):
		self.__data = list()

	def enqueue(self, item):
		self.__data.append(item)

	def dequeue(self):
		if len(self.__data) > 0:
			return self.__data.pop(0)
		return None

	def rear(self):
		if len(self.__data) > 0:
			return self.__data[len(self.__data)-1]
		return None

	def front(self):
		if len(self.__data) > 0:
			return self.__data[0]
		return None

	def is_empty(self):
		return len(self.__data) == 0

	def size(self):
		return len(self.__data)

	def clear(self):
		self.__data = list()

	def show(self):
		print(", ".join(str(val) for val in self.__data))
