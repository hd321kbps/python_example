#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
# Используем слабые ссылки в словарях
import weakref

from profiling import timing

from collections import UserDict
from .read_nodes import read_nodes
from .read_links import read_links

# Создаем исключение
class CorruptedData(Exception) : pass

# Включаем декоратор
@timing
def read_all(path, nodes = "nodes.csv", links = "links.csv"):

	nodes_path = os.path.join(path, nodes)
	links_path = os.path.join(path, links)

	# w - запись, a - дополнение, r - чтение; t - текстовый b - бинарный
	# encoding только для python3
	# src = open(nodes_path, "rt", encoding="utf-8")

	# try:
	# 	for line in src:
	# Удаляем пустые строки
			# if line[-1] == "\n":
			# 	line = line[:-1]
			# print(line)
	# finally:
	# 	src.close()

	Graph = {}
	Names = {}

	for number, name in read_nodes(nodes_path):
		Node = UserDict({
			"number": number,
			"name": name,
			"neighbours": dict(),
			"prohibited": set(),
			# "neighbours": {},
			# "prohibited": (),
			# "prohibited": list(),
		})
		Graph[number] = Node
		if name in Names:
			raise CorruptedData("{0} уже существует".format(name))
		Names[name] = Node

	for point, point2, penalty in read_links(links_path):
		Node1 = Graph[point]
		Node2 = Graph[point2]
		Node1["neighbours"][point2] = (penalty, weakref.ref(Node2))
		Node2["neighbours"][point] = (penalty, weakref.ref(Node1))

	# print(Graph)
	return Graph, Names