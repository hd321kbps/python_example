#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Файлоподобный объект
class Numbers(object):
	def __init__(self, path, mode):
		self.__Src = open(path, mode, encoding = "utf-8")
		self.__Mode = mode
		self.__Buffer = ""

	def read(self, count = None):
		if self.__Mode != "rt":
			raise IOError()
		return self.__Src.read(count)

	def write(self, data):
		if self.__Mode != "wt":
			raise IOError()
		self.__Buffer += data
		while "\n" in self.__Buffer:
			num, self.__Buffer = self.__Buffer.split("\n", 1)
			num = int(num.strip())
			print(num, file = self.__Src)

	def close(self):
		Buff = self.__Buffer.strip()
		if Buff:
			print(int(Buff), file = self.__Src)
		self.__Buffer = ""
		self.__Src.close()

	def __del__(self):
		self.close()

	def __enter__(self):
		return self

	def __exit__(self, ext_type, ext_value, traceback):
		self.close()
		return False

	def __iter__(self):
		Buff = ""
		while True:
			A = self.read(16)
			if not A: break
			Buff += A
			while "\n" in Buff:
				num, Buff = Buff.split("\n", 1)
				yield int(num.strip())
		if Buff.strip():
			yield int(Buff.strip())

# with Numbers("num.dat", "wt") as SRC:
# 	print(25, file = SRC)
# 	print(48, file = SRC)
# 	print(111, file = SRC)
# 	print("   12", file = SRC)

with Numbers("num.dat", "rt") as SRC:
	for item in SRC:
		print(item+1)