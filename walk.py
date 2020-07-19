#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, os.path
import codecs

# Сохранить результаты в файл python walk.py >list.txt 2>error.txt
CDC = codecs.lookup( "windows-1251" )

Cdrive = "C:\\"
for ( path, dirs, files ) in os.walk( Cdrive ):
	for File in files:
		P = os.path.join( path, File )
		RP = os.path.relpath( P, Cdrive )
		( Str, N ) = CDC.encode( RP )
		print( Str )