#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

path = f"D:\Project"

folders = [
	["input",
		[["src", []],
			["doc", []],
		],
	],
	["output", []],
	["scenes", []],
	["assets",
		[["txeture", []],
			["models",
				[["characters", []],
					["location", []],
				],
			],
		],
		["text"],
	],
]

def createFolder(path):
	if not os.path.exists(path):
		os.mkdir(path)

def build(root, data):
	if data:
		for d in data:
			name = d[0]
			path = os.path.join(root, name)
			createFolder(path)
			build(path, d[1])

projectname = input("Enter project name: ")
if projectname:
	fullPath = os.path.join(path, projectname)
	createFolder(fullPath)
	build(fullPath, folders)