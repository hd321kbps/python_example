#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import join, abspath
from itertools import product
import numpy as np
import matplotlib.pyplot as plt

# Все фигуры Лиссажу
def liss(begin, end, path = "."):
  # begin = 1
  # end = 9
  T = np.linspace(0, 100, 1001, dtype = np.float32)

  # product - вложенные циклы
  for a, b in product(range(begin, end+1), range(begin, end+1)):
    X = np.cos(a*T)
    Y = np.sin(b*T)

    plt.plod(X, Y, "b-")
    plt.axis("equal")
    plt.axis([-1.1, 1.1, -1.1, 1.1])

    filepath = join(path, f"liss_{a}_{b}.png")
    filepath = abs(filepath)
    plt.savefig(filepath)
    plt.clf()
    print(a, b)