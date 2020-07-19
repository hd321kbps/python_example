#!/usr/bin/python3
# -*- coding: utf-8 -*-

class InvalidMixin(Exception): pass

def mixin(module):
	def mix(cls):
		for name in module.__all__:
			if hasattr(cls, name):
				raise InvalidMixin("Dublicate attribute '{0}' in class '{1}'".format(name, cls.__name__))
			setattr(cls, name, getattr(module, name))
		return cls
	return mix