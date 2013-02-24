# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe

includes = ["encodings", "encodings.*"]

options = {
	"py2exe": {
		"compressed": 1, # (boolean) create a compressed zipfile
		"optimize": 2, # 2 = extra optimization (like python -OO)
		"includes": includes, # list of module names to include
		"bundle_files": 1 # 1 = bundle everything, including the Python interpreter
	}
}

setup(
	name = "DbPhotos",
	version = "0.1",
	description = "Douban Photos by Join",
	author = "Join",
	author_email = "join.aero@gmail.com",
	options = options,
	zipfile = None, # the files will be bundled within the executable instead of 'library.zip'
	console = [
		{
			"script": "dbphotos.py",
			"icon_resources": [(1, "dbp.ico")]
		}
	]
)