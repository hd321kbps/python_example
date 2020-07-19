#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging.config
from settings import logger_config

# Подключаем свои настройки
logging.config.dictConfig(logger_config)

# Создаем логгер
logger = logging.getLogger("app_logger")
# logger.setLevel("DEBUG")

# std_format = logging.Formatter(fmt = "{asctime} - {levelname} - {name} - {message}", style = "{")

# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# stream_handler.setFormatter(std_format)

# file_handler = logging.FileHandler("my_log.log", mode = "a")
# logger.addHandler(file_handler)
# file_handler.setFormatter(std_format)

words = ["apple", "ice cream", "new house"]

def new_function():
	name = "igor"
	# extra создание атрибута в фильтре
	logger.debug("Enter", extra = {"attr_name": name})

def main():
	logger.debug("Enter")

def main2():
	for item in words:
		try:
			print(item.split(" "))
		except:
			# Показывать traceback 2 способа
			logger.exception(f"Exception, item = {item}")
			# logger.debug("Exception, item = {item}", exc_info = True)

if __name__ == "__main__":
	main()
	# main2()
	new_function()