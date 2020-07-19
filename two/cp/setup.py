#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

# Собрать модуль через команду python setup.py build
# error: Unable to find vcvarsall.bat (Visual Studio)
# module1 - имя dll
module1 = Extension("spec", sources = ["spec.c"])

setup(name = "Spec", version = "0.1", description = "This is a test", ext_modules = [module1])