#!/usr/bin/python3
# -*- coding: utf-8 -*-

import queue
import math
from random import randrange

class RadixSort:
	def __init__(self, n):
		self.bins = list()
		self.nums = n

		for i in range(10):
			self.bins.append(queue.Queue())

	def distribute(self, digit):
		for i in range(10):
			if digit == 1:
				self.bins[self.nums[i]%10].enqueue(self.nums[i])
			else:
				self.bins[math.floor(self.nums[i]//10)].enqueue(self.nums[i])

	def collect(self):
		i = 0
		for digit in range(10):
			while not self.bins[digit].is_empty():
				self.nums[i] = self.bins[digit].dequeue()
				i += 1

	def show(self):
		return "".join(str(self.nums))

nums = []

for i in range(10):
	nums.append(randrange(100))

re = RadixSort(nums)
print("Before: ", re.show())

re.distribute(1)
re.collect()
print("Middle: ", re.show())

re.distribute(10)
re.collect()
print("After: ", re.show())