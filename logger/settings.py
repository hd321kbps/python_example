#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

# Создаем фильтр
class NewFunctionFilter(logging.Filter):
	def filter(self, record):
		# print(dir(record))
		return record.funcName == "new_function"

# Создаем свой обработчик
class MegaHandler(logging.Handler):
	def __init__(self, filename):
		logging.Handler.__init__(self)
		self.filename = filename

	def emit(self, record):
		message = self.format(record)
		with open(self.filename, "w") as file:
			file.write(message + "\n")

logger_config = {
	"version": 1,
	# Отключает все другие логгеры
	"disable_existing_loggers": False,
	"formatters": {
		"std_format": {
			"format": "{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}",
			"style": "{"
		}
	},
	"handlers": {
		"stream": {
			"class": "logging.StreamHandler",
			"level": "DEBUG",
			"formatter": "std_format",
			# "filters": ["new_filter"]
		},
		"file": {
			"()": MegaHandler,
			"level": "DEBUG",
			"filename": "debug.log",
			"formatter": "std_format"
		}
	},
	"loggers": {
		"app_logger": {
			"level": "DEBUG",
			"handlers": ["stream", "file"],
			# Выключить всплывание
			# "propagate": False
		}
	},
	"filter": {
		"new_filter": {
			# Создаем экземпляр класса
			"()": NewFunctionFilter
		}
	},
	# Корневой логгер
	# "root": {},
	# Указывает что этот конфиг не основной (не единственный)
	# "incremental": True
}