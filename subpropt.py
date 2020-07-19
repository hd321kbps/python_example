#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import subprocess

path = os.path.expandvars( "%windir%\\system32\\notepad.exe" )
print( path )

# Запускаем подпроцесс редко используеться
# dir = subprocess.Popen( [], executable=path )

# Запускаем подпроцесс
# параметр cwd из какой папки запускать
# параметр env пути окружения
# dir = subprocess.Popen( [path] )

# Запуск програмы mod.py
# TODO: ошибки
dir = subprocess.Popen( ["C:\\Users\\HD321kbps\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", "mod.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE )

P = dir.communicate( ["This is a test"] )
print( P )

# Текущее состояние процесса none - не завершон, 0 - завершон
# print( dir.poll() )

# Дождаться когда команда выполниться
dir.wait()

print( dir.poll() )

