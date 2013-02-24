# -*- coding:utf-8 -*-

"""
Helper functions for handling chinese path.
"""

import os
from os import path

__all__ = ['u2c', 'make_dirs', 'make_dirs_cn', 'join_cn']

def _encode(s, oldcode, newcode):
	return s.decode(oldcode, 'ignore').encode(newcode, 'ignore')

# def c2u(s):
# 	return _encode(s, 'gbk', 'utf8')

def u2c(s):
	return _encode(s, 'utf8', 'gbk') # gbk or cp936

def make_dirs(dirpath):
	"""Make a directory."""
	if path.isdir(dirpath):
		return dirpath
	os.makedirs(dirpath)
	return dirpath

def make_dirs_cn(dirpath_utf8):
	"""Make a chinese directory. Return a new path which's encoding is gbk."""
	return make_dirs(u2c(dirpath_utf8))

def join_cn(path_cn, *path_utf8):
	"""Join a chinese directory(gbk) and one or more path components(utf8)."""
	return path.join(path_cn, *tuple([u2c(p) for p in path_utf8]))

if __name__ == '__main__':
	"""Easy test."""
	dirpaths = [
		'dir',
		'dir/目录',
		# 'c:/测试/test'
	]
	for dirpath in dirpaths:
		path_cn = make_dirs_cn(dirpath)
		make_dirs(join_cn(path_cn, '测试', 'test'))