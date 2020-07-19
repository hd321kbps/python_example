#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def sqeq ( A, B, C ):
	# Проверка на тип
	if isinstance( A, int ):
		A = float ( A )
	elif not isinstance( A, float ):
		raise TypeError()
	try:
		D = B * B - 4 * A * C

		if D <= 0:
			return ( "Нет Корней" )
		else:
			x1 = ( -B + math.sqrt( D ) ) / ( 2 * A )
			x2 = ( -B - math.sqrt( D ) ) / ( 2 * A )
		return [x1, x2]
	except ZeroDivisionError:
		x = -C / B
		return [x, None]

A1 = float( input( "A: " ) )
B1 = float( input( "B: " ) )
C1 = float( input( "C: " ) )

# Для отладки
try:
	X = sqeq ( A1, B1, C1 )
	print ( X )
except Exception as Exc:
	print ( type( Exc ) )
	# Перевыбрасывание исключения
	raise
# Выполниться в любом случае
finally:
	print( "END" )