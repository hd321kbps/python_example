#!/usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum, unique, auto

@unique
class Color(Enum):
	# Константы
	RED = 1
	GREEN = 2
	BLUE = 3
	SOME = auto()

print(Color.RED)
list(Color)