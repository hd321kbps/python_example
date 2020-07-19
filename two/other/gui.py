#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)

		# Кнопка
		PB = QtWidgets.QPushButton(self)

		# Текст
		PB.setText("Exit")
		self.setCentralWidget(PB)

		# Закрыть по клику по кнопке
		PB.clicked.connect(self.close)

App = QtWidgets.QApplication([])
MW = MainWindow()
MW.show()

Result = App.exec_()

sys.exit(Result)