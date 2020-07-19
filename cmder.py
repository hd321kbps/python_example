#!/usr/bin/python3
# -*- coding: utf-8 -*-

import optparse

# Добавляем параметры к команде
parser = optparse.OptionParser()
parser.add_option( "-m", "--message", dest="message", default="OK", help="Message to print on screen")
parser.add_option( "-c", "--count", dest="count", type="int", help="Count of people")

( options, args ) = parser.parse_args()

# TODO: Не работает 3 строки
# subcommand = args[0]
# del args[0]

# print( subcommand )
print( options )
print( args )