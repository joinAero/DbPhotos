DbPhotos
========

To crawl the photos of [豆瓣](http://www.douban.com/) site.

Deploy
-----

[pyr_lnk]: https://pypi.python.org/pypi/pyreadline
[pyi_lnk]: https://pypi.python.org/pypi/pyreadline
[py2_lnk]: https://pypi.python.org/pypi/pyreadline

* setup [pyreadline][pyr_lnk].

	* make be able to paste on a console window

* setup [pyinstaller][pyi_lnk] to make exe.

	* [py2exe][py2_lnk] has problem when using [pyreadline][pyr_lnk].

	* execute the following:

		```
		$ cd [project_path]
		$ python -O C:\pyinstaller-2.0\pyinstaller.py -c -F -i dbp.ico dbphotos.py
		```
* execute `clean.py` to clean.

Change log
----------

2013-02-25 --r1--

* First alpha release	