#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Слабые ссылки
import weakref
# Замыкание
from functools import partial

def _remove_child(L, wr):
	# L.remove(wr)
	for k in range(0, len(L)):
		if L[k] is wr:
			del L[k]
			break

# Контейнер и компоненты
class Container(object):
	def __init__(self):
		self.__Children = []

	def add(self, component):
		rc = partial(_remove_child, self.__Children)
		self.__Children.append(weakref.ref(component, rc))
		component._adjust_container(self)

	@property
	def children(self):
		for child in self.__Children:
			yield child()

	def __del__(self):
		print("deleted", self)

class Component(object):
	def __init__(self, container = None):
		self.__Container = container
		if container is not None:
			container.add(self)

	def _adjust_container(self, container):
		if self.__Container is not container:
			self.__Container = container

	def __del__(self):
		print("deleted", self)

box = Container()
# apple = Component(box)
x = Component(box)
y = Component(box)
z = Component(box)

del box
del x
del y
del z

print ("-----")