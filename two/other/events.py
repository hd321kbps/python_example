#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Dispatch(object):
	def __init__(self):
		self.__DispTable = {}

	def addEvent(self, event, function):
		if event in self.__DispTable:
			self.__DispTable[event]. append(function)
		else:
			self.__DispTable[event] = [function]

	def killEvent(self, event):
		if event in self.__DispTable:
			del self.__DispTable[event]

	def loop(self):
		while True:
			Event = input(": ")
			if Event in self.__DispTable:
				for func in self.__DispTable[Event]:
					func(Event)
			if Event == "quit":
				break

def echo1(event):
	print(event)

def echo2(event):
	print(event + "-2")

def echo3(event):
	print(event + ":" + event)

if __name__ == "__main__":
		D = Dispatch()
		D.addEvent("echo", echo1)
		D.addEvent("exit", echo2)
		D.addEvent("continue", echo2)
		D.addEvent("stop", echo3)
		D.addEvent("stop", echo1)

		D.loop()