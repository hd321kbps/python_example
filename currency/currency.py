#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from datetime import date
from decimal import Decimal

# TABLE = re.compile("<table\\s?[^<>]*>.+</table>", re.DOTALL)
TABLE = re.compile(r"<table\s?[^<>]*>.+?</table>", re.DOTALL)
# расширенные правила
ITEM = re.compile(r'''
	<td\b[^<>]*>(\d\d)\.(\d\d)\.(\d\d\d\d)</td> # дата
	<td\b[^<>]*>(\d+)</td> # количество единиц
	<td\b[^<>]*>(\d+\.\d+)</td> # курс
	<td\b[^<>]*><span\b[^<>]*>([+|-]\d\.\d\d\d\d)</span></td> # динамика
	''', re.VERBOSE)

with open("history.htm", "rt", encoding = "windows-1251") as src:
	data = src.read()

# for M in TABLE.finditer(data):
# 	if "<table>" in M.group(0): continue
# 	print(M.group(0))

# for M in ITEM.finditer(data):
# 	print(M.group(0))

# M = ITEM.search(data)
# if M:
# 	print(M.group(0))

for M in ITEM.finditer(data):
	day = int(M.group(1))
	month = int(M.group(2))
	year = int(M.group(3))
	scale = int(M.group(4))
	course = Decimal(M.group(5))
	dinamic = Decimal(M.group(6))
	Dt = date(year = year, month = month, day = day)
	print(Dt, scale, course, dinamic)