#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

HM = hashlib.md5()
HS = hashlib.sha1()
func = HS.update
with open( "test2.txt", "rb" ) as TRG:
	try :
		while True :
			A = TRG.read( 1024 )
			if A == b"" : break
			func( A )
			HM.update( A )
	# Подавляем исключение через pass
	except IOError : pass

print( HS.hexdigest() )
print( HM.hexdigest() )