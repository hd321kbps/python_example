#!/usr/bin/python3
# -*- coding: utf-8 -*-

def issimple_func( X ):
	for K in range( 2, int(X / 2) ):
		if X % K == 0:
			return False
		return True

# Отладочный режим ( запуск питона не в оптимизированном режиме -O)
if __debug__:
	print( "Модуль", __name__, "подключен" )