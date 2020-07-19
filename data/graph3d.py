#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# t = np.linspace(-13, 13, 1001, dtype = np.float64)
# z = t / 5
# r = z ** 2 + 1
# x = r * np.cos(t)
# y = r * np.sin(t)

# fig = plt.figure()
# ax = fig.gca(projection = "3d")
# ax.plot(x, y, z)
# plt.show()

# Круговая диаграмма
A = [10, 15, 3, 0]
B = [15, 14, 3, 25]

# fig = plt.figure()
# old = fig.add_subplot(1, 2, 1)
# new = fig.add_subplot(1, 2, 2)
names = ["Вася", "Петя", "Коля", "Саша"]
# old.pie(A, labels = names)
# new.pie(B, labels = names)
# plt.show()

# Столбчатая диаграмма
idx = np.linspace(0, 10, 4, dtype = np.float32)
wid = 0.5
plt.bar(idx, A, wid, color = "b", label = "2010")
# plt.bar(idx + wid, B, wid, color = "r", label = "2015")
plt.bar(idx, B, wid, color = "r", label = "2015", bottom = A)
# plt.xticks(idx + wid / 2, names)
plt.xticks(idx, names)
plt.legend()
plt.show()