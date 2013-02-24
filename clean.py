#!c:\python27\python.exe

import os
from os import path
from shutil import rmtree

del_exts = ['.pyc', '.pyo', '.spec']

def del_file(p):
	if path.isfile(p):
		ext = path.splitext(p)[1]
		if ext in del_exts:
			os.remove(p)
			print('deleted : %s' % p)
	else:
		for item in os.listdir(p):
			del_file(path.join(p, item))

def del_dir(p):
	if path.isdir(p):
		rmtree(p)
		print('deleted : %s <DIR>' % p)

def del_dirs(iterable):
	for p in iterable:
		del_dir(p)

def clean():
	del_dirs(p for p in ['build', 'dist'])
	from time import sleep
	sleep(0.1)
	del_file(os.curdir)

if __name__ == '__main__':
	clean()