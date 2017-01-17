#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os
import sys
import readchar			# https://pypi.python.org/pypi/readchar






def readpwd_debug():
	while True:
		c = readchar.readchar()
		ordC = ord(c[0])
		if ordC == 3:
			break
		print("CHAR: " + c + " (" + str(ordC) + ")")



def readpwd(startText = None):
	if startText != None:
		sys.stdout.write(startText)
		sys.stdout.flush()

	ret = ""
	while True:
		c = readchar.readchar()
		ordC = ord(c[0])
		if ordC == 3:
			sys.stdout.write('\n')
			sys.stdout.flush()
			return None
		if ordC == 13:
			sys.stdout.write('\n')
			sys.stdout.flush()
			return ret
		if ordC == 127:
			if len(ret) > 0:
				ret = ret[:-1]
				sys.stdout.write('\b \b')
				sys.stdout.flush()
			continue
		ret += c[0]
		sys.stdout.write('*')
		sys.stdout.flush()











