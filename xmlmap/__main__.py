#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname, normpath
import xml.sax
import matplotlib.pyplot as plt
from MapXmlHandler import MapXmlHandler

datapath = dirname(abspath(__file__))
datapath = normpath(join(datapath, ".", "data"))
datafilepath = join(datapath, "map.osm")

mapdata = MapXmlHandler()
xml.sax.parse(datafilepath, mapdata)

for way in mapdata.ways.values():
  w = way["points"]
  plt.plot(w[:, 0], w[:, 1], color = "blue")
# Кординаты из OpenStreetMap
plt.axis(39.01126, 39.01968, 45.06714, 45.06382)
plt.show()