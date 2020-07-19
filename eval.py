#!/usr/bin/python3
# -*- coding: utf-8 -*-

A = input ("A: ")
B = input ("B: ")
O = input (": ")

func = eval( "lambda x, y: x " + O + " y" )
print( func( A, B ) )

# Многострочный текст
print('''
	Много
	Текста
''')

# Каринг
def func1 ( x, y ):
	# Форматирование строки
	# %d - decimal, %s - string %f - float

	# С кортежем
	print( "x=%d y=%d" % ( x, y ) )

	# Со словарем
	# \ склейка строки без пробела в конце
	print( "x=%(x) d y=%(y) d x=%(x) d" \
		% { "x": x, "y": y } )


	print( "x=", x, " y=", y )

func2 = lambda x : lambda y : func1( x, y )

def func3( x ):
	def f( y ) :
		return func1( x,y )
	return f

func2( 2 ) ( 3 )
func3( 2 ) ( 3 )