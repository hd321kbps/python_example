#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

__all__ = ("read_nodes",)

def read_nodes(filepath, encoding = "utf-8"):
	with open(filepath, "rt", encoding = encoding) as src:
		# Создаем обьект данных
		rdr = csv.reader(src)
		for number, name in rdr:
			yield int(number), name