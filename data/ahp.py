#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# Метод Саати - метод анализа
M1 = np.indentity(4, dtype = np.float32)
# Сравниваем первый вариант (0) со вторым (1) и получаем результат (2)
M1[0, 1] = 2
M1[3, 2] = 3

def fill_zeros(M):
  R, C = M.shape
  R = range(0, R)
  C = range(0, C)
  for i, k in product(R, C):
    if M[i, k] == 0:
      M[i, k] = 1 / M[k, i]

fill_zeros(M1)
np.linalg.eig(M1)