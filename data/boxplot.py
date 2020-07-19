#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Создание японских свечей
A = np.random.rand(200) * 4 + 4
B = np.random.randn(300) * 2 + 7
C = np.concatenate((A, B), 0)
plt.boxplot([A, B, C])
plt.show()

# Создание матрицы
M = np.array([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 25, 11, 12],
  [13, 14, 15, 20]
], dtype = np.float32)
M = np.mat(M)

# Плохой способ
# V = np.mat(np.array([-1, 2, 12, 6]), dtype = np.float32)
V = np.array([-1, 2, 12, 6], dtype = np.float32)
M1 = np.linalg.inv(M)
# X = np.matmul(V, M1)
# np.dot(M, X)
X = np.linalg.solve(M, V)

A1 = M + np.identity(4)
s = np.random.rand(4)
s1 = np.matmul(A1, s) + V

d = np.linalg.det(M)
A2 = M / (2 * d) + np.identity(4)
B1 = V / (2 * d)
s3 = np.matmul(A2, s1) + B1

# Создание гистограммы в виде столбчатой диаграмы
data = np.random.randn(1000) * 10
h1 = np.histogram(data)
plt.bar(range(0, 10), h1[0])
plt.show()
# Более верный вариант
plt.hist(data, 50, zorder = 2)
plt.grid(True, zorder = 1)
plt.show()