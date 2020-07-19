#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from decimal import Decimal

class Position(object):
	
	def __init__(self, title, quantity, **kwargs):
		self.__Title = title
		self.__Quantity = quantity
		with suppress(KeyError):
			self.__Unit = kwargs["unit"]
		with suppress(KeyError):
			self.__Price = Decimal(kwargs["price"])
		try:
			self.__Total = Decimal(kwargs["total"])
		except KeyError:
			try:
				self.__Total = self.quantity * self.price
			except AttributeError as Exc:
				raise ValueError("Price or total have to be specified") from Exc

	title = property(lambda self: self.__Title)
	quantity = property(lambda self: self.__Quantity)
	unit = property(lambda self: self.__Unit)
	price = property(lambda self: self.__Price)
	total = property(lambda self: self.__Total)

	def __str__(self):
		L = [self.title]
		with suppress(AttributeError):
			L.append(self.unit)
		L.append("C:{0}".format(self.quantity))
		with suppress(AttributeError):
			L.append("P:{0}".format(self.price))
		L.append("S:{0}".format(self.total))
		return " ".join(L)