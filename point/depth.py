#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import argparse
import logging
from contextlib import suppress

import generator

AP = argparse.ArgumentParser(description = "Search path in graph")
AP.add_argument("first", type = str, help = "First vertex in path")
AP.add_argument("last", type = str, help = "Last vertex in path")
AP.add_argument("--data-path", "-d", dest = "path", action = "store", type = str, default = ".", help = "Path to directory where data files are located")
AP.add_argument("--nodes", "-n", dest = "nodes", action = "store", type = str, default = "nodes.csv", help = "Name of nodes file")
AP.add_argument("--links", "-l", dest = "links", action = "store", type = str, default = "links.csv", help = "Name of links file")
AP.add_argument("--debug", dest = "loglevel", action = "store_const", const = logging.DEBUG, default = logging.WARNING, help = "log level = DEBUG")
AP.add_argument("--error", dest = "loglevel", action = "store_const", const = logging.ERROR, default = logging.WARNING, help = "log level = ERROR")

ARGS = AP.parse_args()

# В папке пользователя .depth
LogPath = os.path.expanduser(os.path.join("~", ".depth"))
# подавляем исключени (компактная запись)
with suppress(OSError):
	# создаем папку
	os.mkdir(LogPath)

logging.basicConfig(
	level = ARGS.loglevel,
	style = "{",
	format = "{levelname:8} {asctime} {name:10} {message}",
	# filename = "./log/error.log",
	# filename = os.path.join(LogPath, "general.log")
)

# Абсолютный путь
data_path = os.path.abspath(ARGS.path)

logging.debug("First: {0.first} Last: {0.last}".format(ARGS))
logging.debug("Data path: {0.path} ({1})".format(ARGS, data_path))
logging.debug("Nodes: {0.nodes} Links: {0.nodes}".format(ARGS))
logging.info("Test")
logging.warning("Test")
logging.error("Test")
logging.critical("Test")


# data_path = os.path.join("D:", "\\", "Project", "python", "point", "data")
# print(data_path)
Graph, Names = generator.read_all(data_path, ARGS.nodes, ARGS.links)

First = Names[ARGS.first]['number']
Last = Names[ARGS.last]['number']

for path in generator.in_depth(Graph, First, Last):
	print(path)