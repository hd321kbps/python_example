#!/usr/bin/python3
# -*- coding: utf-8 -*-

from contextlib import suppress
from datetime import datetime
import logging

import helpers
from .Position import *

class Invoice(object):

	def __init__(self):
		self.__Created = datetime.now()
		self.__Positions = []

	created = property(lambda self: self.__Created)

	@property
	def number(self):
		return self.__Number

	@number.setter
	@helpers.info_value
	@helpers.value_not_none
	def number(self, value):
		self.__Number = value

	@number.deleter
	def number(self):
		logging.info("Number {0} deleted".format(self.number))
		del self.__Number

	address = property(lambda self: self.__Address)

	@address.setter
	@helpers.warn_value
	@helpers.value_not_none
	def address(self, value):
		self.__Address = value

	pesponser = property(lambda self: self.__Pesponser)

	@pesponser.setter
	@helpers.trace_value(logging.ERROR - 1)
	@helpers.value_not_none
	def pesponser(self, value):
		self.__Pesponser = value

	subscribed = property(lambda self: False)

	@property
	def itogo(self):
		if self.subscribed:
			return self.__Itogo
		else:
			return sum(p.total for p in self.__Positions)

	def append(self, *args, **kwargs):
		if isinstance(args[0], Position):
			P = args[0]
		else:
			P = Position(*args, **kwargs)
		self.__Positions.append(P)

	__StrData = [
		("Number", "number"),
		("Created date", "created"),
		("Address", "address"),
		("Responible person", "pesponser"),
		("Is subscribed", "subscribed"),
		("Result", "itogo"),
	]

	def __len__(self):
		return len(self.__Positions)

	def __str__(self):
		L = []
		for text, propname in self.__StrData:
			with suppress(AttributeError):
				T = "{0}: {1}".format(text, getattr(self, propname))
				L.append(T)
		L.extend(map(str, self.__Positions))
		return "\n".join(L)

	def __getitem__(self, key):
		if not isinstance(key, int):
			raise ValueError("Slices or keys not supported")
		return self.__Positions[key]

	def __setitem__(self, key, value):
		if not isinstance(key, int):
			raise ValueError("Slices or keys not supported")
		self.__Positions[key] = value

	def __delitem__(self, key):
		if not isinstance(key, int):
			raise ValueError("Slices or keys not supported")
		del self.__Positions[key]

	def __iter__(self):
		yield from self.__Positions