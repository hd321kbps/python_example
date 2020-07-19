#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import requests

# Создаем логгеру уровень логгирования
logging.basicConfig(level = "DEBUG", filename = "mylog.log")
# Содание логгера
logger = logging.getLogger()
# Выключаем лишний логгер
logging.getLogger("urllib3").setLevel("CRITICAL")

# Просмотр всех логгеров
for key in logging.Logger.manager.loggerDict:
	print(key)

def main(name):
	logger.warning(f"Enter in the main() function: name = {name}")
	r = requests.get("https://www.google.ru")

if __name__ == "__main__":
	main("igor")