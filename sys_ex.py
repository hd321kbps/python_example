#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

for P in sys.path:
	print( P )

for P in os.environ:
	print( P )

X = "C:\\www\\dict.js"
# Разбивает путь имени папки и имени файла
print( os.path.split( X ) )
# Склеить пути
print( os.path.join( "C:\\www", "dict.js" ) )
# Имя файла
print( os.path.basename( X ) )
# Имя папки
print( os.path.dirname( X ) )

# Есть ли этот файл
print( os.path.exists( X ) )
# Это файл
print( os.path.isfile( X ) )