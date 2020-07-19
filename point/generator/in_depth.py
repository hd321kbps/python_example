#!/usr/bin/python3
# -*- coding: utf-8 -*-

def in_depth(graph, first, last):
	
	# def neighbours(node):
	# 	R = set(node["neighbours"].keys())
	# 	return R
	
	Path = [first]
	while Path:
		Node = graph[Path[-1]]
		# R = neighbours(node) - node["prohibited"]
		R = set(Node["neighbours"].keys())
		R -= Node["prohibited"]
		try:
			next = R.pop()
			Node["prohibited"].add(next)
			if next == last:
				yield Path + [next]
			elif next in Path: pass
			else:
				Path.append(next)
		except KeyError:
			Node["prohibited"] = set()
			del Path[-1]