#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging

# Декоратор
def timing(function):
	def timed_function(*args, **kwars):
		T0 = datetime.now()
		Result = function(*args, **kwars)
		T0 = datetime.now() - T0
		# logging.debug("{0}: {1}".format(function.__name__, T0.microsecond))
		# logging.debug("{function.__name__}: {T0.microsecond}\
		# 	".format(function=function, T0=T0))
		logging.debug("{function.__name__}: {T0.microseconds}".format(**locals()))
		return Result
	return timed_function