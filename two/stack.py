#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Stack:
	def __init__(self):
		self.__data = list()

	def push(self, item):
		self.__data.append(item)

	def pop(self):
		if len(self.__data) > 0:
			return self.__data.pop()
		return None

	def peek(self):
		if len(self.__data) > 0:
			return self.__data[len(self.__data)-1]
		return None

	def is_empty(self):
		return len(self.__data) == 0

	def size(self):
		return len(self.__data)

	def show(self):
		print("\n".join(str(val) for val in self.__data))