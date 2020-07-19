#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

__all__ = ("read_links",)

def read_links(filepath, encoding = "utf-8"):
	with open(filepath, "rt", encoding = encoding) as src:
		# Создаем обьект данных
		rdr = csv.reader(src)
		for point, point2, penalty in rdr:
			yield int(point), int(point2), float(penalty)