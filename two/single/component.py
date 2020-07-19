#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Слабые ссылки
import weakref

# Контейнер и компоненты
class Container(object):
	def __init__(self):
		self.__Children = []

	def add(self, component):
		self.__Children.append(component)
		component._adjust_container(self)

	def __del__(self):
		print("deleted", self)

class Component(object):
	def __init__(self, container = None):
		if container is not None:
			self.__Container = weakref.ref(container)
			container.add(self)
		else:
			self.__Container = None

	def _adjust_container(self, container):
		if self.container is not container:
			self.__Container = weakref.ref(container)

	@property
	def container(self):
		if self.__Container is None:
			return None
		else:
			return self.__Container()

	def __del__(self):
		print("deleted", self)

box = Container()
# apple = Component(box)
Component(box)
Component(box)
Component(box)

a = Component()

del box
del a

print ("-----")