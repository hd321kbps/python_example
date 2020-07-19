#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 10000
T = np.linspace(0, 1000, N+1, dtype = np.float32)

a = 3
b = 5

X = np.cos(a*T)
Y = np.sin(b*T)

plt.plot(X, Y, "g-")
plt.savefig(f"liss_{a}_{b}.png")