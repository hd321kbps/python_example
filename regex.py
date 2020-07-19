#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import codecs
import random

def false_phone( match ):
	Op = [
		[ "916", "917", "985" ],
		[ "925", "926" ]
	]
	D = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
	R = "+"

	R = "+"+match.group(1)
	O = match.group(2)

	for OpCodes in Op:
		if O in OpCodes :
			N = random.randrange( 0, len(OpCodes))
			O = OpCodes[ N ]
	R += "("+O+")"

	for k in range( 0, 3 ):
		R += D[random.randrange( 0, len(D))]
	R += "-"

	for k in range( 0, 4 ):
		R += D[random.randrange( 0, len(D))]
	return R

	# for k in range( 0, 11 ) :
	# 	R += D[random.randrange( 0, len( D ) )]
	# return R[:1]+"("+R[1:4]+")"+R[4:7]+"-"+R[7:]

CD = codecs.lookup( "cp866" )

PT = re.compile( r"[+](7)\((\d{3})\)(\d{3}-(\d{2}-\d{2}|\d{4})|\d{7})" )

# X = input()

# TODO: Не работает строка 43
X = CD.decode( input() ) [0]
M = PT.search ( X )

if M:
	print( M.group(0) )
	# print( M.group(1) )
	# Выводить все группы кроме 0
	print( M.groups() )
	# Выбросить группу 2
	# X = X[:M.start(2)] + X[M.end(2):]
	# print( X )
	# Начало и конец группы 0 в виде кортежа
	# M.span(0)
	# Замена при выводе
	Y = PT.sub( false_phone, X )
	print( Y )
else:
	print( "Строка не соотвествует паттерну" )

PZ = re.compile( r"\s*[,;]\s*" )
A = PZ.split( "Vasja, Petya   ; Kolya" )
print( A )