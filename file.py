#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Считывание файла
FD = open( "D:/Project/vuejs/index2.html", "rt" )

# Считать 1 строчку
M = FD.readline()
print( M )

for Line in FD:
	# Убераем последний символ в стоке
	L = Line[:-1] if Line[-1] == "\n" else Line
	print( L )

# Запись в файл
TRG = open( "D:/Project/python/test.txt", "wt")
TRG.write("Вася Пупкин")
TRG.close()
