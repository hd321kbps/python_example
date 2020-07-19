#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs

# rb двоичный rt текстовый
with codecs.open( "test.txt", "rb", encoding="windows-1251" ) as SRC:
	for Line in SRC :
		print( Line )