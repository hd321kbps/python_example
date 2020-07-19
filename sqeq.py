#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Синтаксис 3 версии во 2
# from __future__ import print_function, unicode_literals, division
import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

D = B**2 - 4.0*A*C

if D <= 0:
	print ("Нет Корней")
elif A == 0 or B == 0 or C == 0:
	print ("Делить на ноль нельзя")
else:
	x1 = ( -B + math.sqrt(D) ) / ( 2.0 * A )
	x2 = ( -B - math.sqrt(D) ) / ( 2.0 * A )

	print ("x1 = ", x1)
	print ("x2 = ", x2)