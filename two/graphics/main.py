#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import graph
from MyApp import MyApp

# import sys
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *

# Запуск документации  python -m pydoc -p 8080

# Инициализация
# App = graph.Application()
App = MyApp()
App.win_size = (320, 240)
App.win_pos = (10, 20)

# glutInit(sys.argv)
# Режимы
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)
# Размер окна
# glutInitWindowSize(800, 600)
# Позиция
# glutInitWindowPosition(0, 0)
# Создание окна
# glutCreateWindow("This is an experimental OpenGL window")
# Видимая область при изминения окна (необязательно)
# glViewport(0, 0, 800, 600)
# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
# glMatrixMode(GL_MODELVIEW)
# glLoadIdentity()

# def draw():
# 	pass

# glutDisplayFunc(draw)

# Запуск
App.run()
# glutMainLoop()