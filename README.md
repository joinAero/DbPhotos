DbPhotos
========

To crawl the photos of [豆瓣](http://www.douban.com/) site.

Deploy
-----

[pyr_lnk]: https://pypi.python.org/pypi/pyreadline
[pyi_lnk]: http://www.pyinstaller.org/
[py2_lnk]: http://www.py2exe.org/

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

Download
--------

[dbphotos.exe](https://add110.opendrive.com/files?67945224_v2cnM)

Change log
----------

2013-02-25 --r1--

* Amend websites' link in `README.md`
* Fixed issue that fail to next album page
* First alpha release