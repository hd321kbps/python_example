#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join, abspath
from liss2 import liss
from linear import *

# liss(1, 9, '.')("

# ar = sheet_to_array(join("data", "line.xlsx"))
# print(ar)

# save_pict(join("data", "line.xlsx"), "line.png")

D = sheet_to_array(join("data", "line.xlsx"))
D1, A = kill_extent(D)
a, b = ab(D1)
save_pict(D, "line1.png", a = a, b = b)
save_pict(D1, "line2.png", a = a, b = b, add_points = A)