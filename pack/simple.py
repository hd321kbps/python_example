#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pack.issimple as issimple

def simple_func( N ):
	K = 2
	while K < N:
		# вызов из модуля
		if issimple.issimple_func( K ):
			yield K
		K += 1

# Отладочный режим ( запуск питона не в оптимизированном режиме -O)
if __debug__:
	print( "Модуль", __name__, "подключен" )