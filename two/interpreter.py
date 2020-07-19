#!/usr/bin/python3
# -*- coding: utf-8 -*-

import stack
import abc
import enum

class InterpreterAbstract(abc.ABC):
	'''Интерпретатор кода'''

	def __init__(self, code):
		'''Принимает код'''
		self.code = code

	def execute(self):
		'''Запускает механизм исполнения кода
		Возвращает результат исполнения кода'''
		return self._parse()

	@abc.abstractmethod
	def _parse(self):
		'''Осуществляет парсинг кода.
		Вызывает _evaluate для исполнения выражений
		Возвращает результат исполнения кода в excecute'''
		pass

	@abc.abstractmethod
	def _evaluate(self, code):
		'''Осуществляет вычисление выражения
		Возвращает результат выражения в _parse'''
		pass

class Token(enum.Enum):
	PLUS = "+"
	MINUS = "-"
	ASTERISK = "*"
	SLASH = "/"
	CARET = "^"
	EXP_OPEN = "("
	EXP_CLOSE = ")"

	def __eq__(self, other):
		if type(other) is str:
			return self.value[0] == other

class Interpreter(InterpreterAbstract):
	def __init__(self, file = None, string = None):
		if string is not None:
			self.__code = string
		else:
			if file is None:
				raise ValueError("Укажите код в виде строки или файла")
			with open(file) as f:
				self.__code = f.read()
		self.__ops = stack.Stack()
		self.__vals = stack.Stack()

	def execute(self):
		return self._parse()

	def _parse(self):
		lines = self.__code.strip().split("\n")
		res = list()

		for line in lines:
			if not self._validate(line):
				raise Exception("Баг в коде со скобками!")

		for line in lines:
			line = "".join(line.split())
			res.append(self._evaluate(line))
		return res

	def _validate(self, code):
		valid = stack.Stack()
		for char in code:
			if char == Token.EXP_OPEN:
				valid.push(char)
			elif char == Token.EXP_CLOSE:
				valid.pop()
		if valid.is_empty():
			return True
		else:
			return False

	def _evaluate(self, code):
		operators = ["+", "-", "*", "/", "^"]
		code = "(" + code + ")"
		prev_char = ""
		for char in code:
			if char.isdigit():
				prev_char += char
				continue
			elif prev_char != "":
				self.__vals.push(prev_char)
				prev_char = ""
			if char == Token.EXP_OPEN:
				continue
			elif char in operators:
				self.__ops.push(char)
			elif char == Token.EXP_CLOSE:
				op = self.__ops.pop()
				val = int(self.__vals.pop())
				if op == Token.PLUS:
					val = int(self.__vals.pop()) + val
				elif op == Token.MINUS:
					val = int(self.__vals.pop()) - val
				elif op == Token.ASTERISK:
					val = int(self.__vals.pop()) * val
				elif op == Token.SLASH:
					val = int(self.__vals.pop()) // val
				elif op == Token.CARET:
					val = int(self.__vals.pop()) ^ val
				self.__vals.push(val)
				continue
			else:
				self.__vals.push(char)
		return self.__vals.pop()

interpreter = Interpreter(string = "(1+((2+3)*(4*5)))")
print(interpreter.execute())

interpreter = Interpreter(string = "(2+((2*3)/(4^5)))")
print(interpreter.execute())

interpreter = Interpreter(string = "(2+2 )+ (2  +(3+3))")
print(interpreter.execute())

# Ошибка скобок
# interpreter = Interpreter(string = "(2+2)+(2+(3+3))")
# print(interpreter.execute())

interpreter = Interpreter(file = "inter.txt")
print(interpreter.execute())

# Ошибка нет параметров
# interpreter = Interpreter()
# print(interpreter.execute())