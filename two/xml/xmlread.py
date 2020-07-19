#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import xml.dom, xml.dom.minidom

Doc = xml.dom.minidom.parse("example.xml")
Doc2 = xml.dom.minidom.parseString("<params id='210'>основной текст</params>")

print(Doc)
print(Doc2)

# Выборка корневого элемента
Root = Doc.documentElement
print(Root)

Sp = re.compile(r"^\s+")

for N in Root.childNodes:
	if N.nodeType == xml.dom.Node.TEXT_NODE:
		if Sp.match(N.data):
			# Удаляем \n
			Root.removeChild(N)

for N in Root.childNodes:
	print(N)

# Добавить узел
El = Doc.createElement("four")
Root.appendChild(El)

with open("example2.xml", "wt") as TRG:
	Doc.writexml(TRG, " ", " ", "\n")

print(Root)