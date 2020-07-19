#!/usr/bin/python3
# -*- coding: utf-8 -*-

import doc

N = doc.Invoice()

N.append("Рога", 25, unit = "шт", price = 100.02)
N.append(doc.Position("Копыта", 100, total = 1000.45))
N.append(doc.Position("Баранки", 100, total = 1000.45))

print("----- __str__ -----")
print(N)

print("----- __len__ -----")
print("Всего позиций: {0}".format(len(N)))

print("----- __getitem__ -----")
print(N[1])

print("----- __setitem__ -----")
N[2] = doc.Position("Бублики", 21, price = 100, total = 1000)
print(N)

print("----- __delitem__ -----")
del N[1]
print(N)

print("----- __iter__ -----")
for p in N:
	print(p)