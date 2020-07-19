#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def sqeq (A, B, C):
	D = B * B - 4 * A * C

	if D <= 0:
		return ("Нет Корней")
	elif A == 0 or B == 0 or C == 0:
		return ("Делить на ноль нельзя")
	else:
		x1 = ( -B + math.sqrt( D ) ) / ( 2 * A)
		x2 = ( -B - math.sqrt( D ) ) / ( 2 * A)
	return [x1, x2]

A1 = float(input( "A: " ))
B1 = float(input( "B: " ))
C1 = float(input( "C: " ))

X = sqeq (A1, B1, C1)
print (X)