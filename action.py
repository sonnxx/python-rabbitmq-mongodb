#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys
import inspect
import Worker as words

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

if __name__ == '__main__':
	argNames = ['command', 'task']
	args = dict(zip(argNames, sys.argv))

	tasks = ['sendqueue', 'progressqueue']

	if 'task' not in args:
		print('===> Not found task in tasks')
		for vtask in tasks:
			print('- ' + vtask)
		exit()
	
	task = args['task']
	if task in tasks:

		# words.Worker().sendqueue()

		method_to_call = getattr(words.Worker(), task)
		method_to_call()
	else:
		print('===> Not found task in tasks')
		for vtask in tasks:
			print('- ' + vtask)
		exit()