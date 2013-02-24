# -*- coding:utf-8 -*-

"""
Fetch web contents.
"""

import urllib
import urllib2

__all__ = ['fetch_html', 'fetch_img']

def fetch_html(url, timeout=10):
	"""Fetch a web page source."""
	return urllib2.urlopen(url, timeout=timeout).read()

def fetch_img(url, filename):
	"""Fecth a image and return `(filename, httplib.HTTPMessage)`."""
	return urllib.urlretrieve(url, filename)

if __name__ == '__main__':
	html = fetch_html('http://www.douban.com/')
	print(html)

	print('*****' * 10)
	filename, httpmsg = fetch_img('http://img3.douban.com/view/photo/photo/public/p1240753935.jpg', 'p1240753935.jpg')
	print(httpmsg)

	print('*****' * 10)
	print(httpmsg.getheader('Content-Length'))