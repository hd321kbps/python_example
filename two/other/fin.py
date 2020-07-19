#!/usr/bin/python3
# -*- coding: utf-8 -*-

import decimal

Ctx = decimal.getcontext()
Ctx.prec = 30 # numeric(22, 2)
# Способ округления
Ctx.rounding = decimal.ROUND_HALF_UP

# Шаблон для количества отображения символов (2) после запятой
TWO = decimal.Decimal("0.01")

A = decimal.Decimal("15.267")
B = (A / 7).quantize(TWO)
C = 15.257 / 7
print(B, C)