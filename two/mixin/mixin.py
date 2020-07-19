#!/usr/bin/python3
# -*- coding: utf-8 -*-

def mix1(self):
	print("mix1", self.x)

y = property(lambda self: "y")

def mymix(cls):
	setattr(cls, "mix1", mix1)
	setattr(cls, "y", y)
	return cls