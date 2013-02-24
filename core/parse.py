# -*- coding:utf-8 -*-

"""
Parse url, html, etc.
"""

import re

__all__ = ['parse_url', 'parse_photo_preview', 'parse_photo_view', 
'parse_photo_next', 'parse_photo_nums', 'parse_title']

# url pattern
_url_patts = {
	1: r'http://www\.douban\.com/photos/album/\d+/($|\?start=\d+)',
	2: r'http://www\.douban\.com/online/\d+/album/\d+/($|\?start=\d+)',
	3: r'http://site\.douban\.com/\w+/widget/(public_album|photos)/\d+/($|\?start=\d+)',
	4: r'http://www\.douban\.com/photos/photo/\d+/($|#\w+)',
	5: r'http://www\.douban\.com/online/\d+/photo/\d+/($|#\w+)',
	6: r'http://site\.douban\.com/\w+/widget/(public_album|photos)/\d+/photo/\d+/($|#\w+)',
}

# url pattern
_compile_patts = { k: re.compile(v) for k, v in _url_patts.items() }

def parse_url(url):
	"""Parse douban url's category."""
	for key, patt in _compile_patts.items():
		res = re.match(patt, url)
		if res:
			return key
	return None

def parse_photo_preview(html):
	"""Parse web page where preview many photoes.

	<img src="http://img3.douban.com/view/photo/thumb/public/p1240756895.jpg" />
	"""
	patt = re.compile(r'<img src="http://img3\.douban\.com/view/photo/thumb/public/(p\d+\.jpg)"\s?/?>')
	def inner_func(html):
		return re.findall(patt, html)
	return inner_func(html)

def parse_photo_view(html):
	"""Parse web page where view a photo. 

	<img src="http://img3.douban.com/view/photo/photo/public/p1240756463.jpg" />
	"""
	patt = re.compile(r'<img src="http://img3\.douban\.com/view/photo/photo/public/(p\d+\.jpg)"\s?/?>')
	def inner_func(html):
		res = re.search(patt, html)
		if res:
			return res.group(1)
		return None
	return inner_func(html)

def parse_photo_next(html):
	"""Parse it's next page which view a photo.

	<a href="http://www.douban.com/photos/photo/1240753935/#image" title="用方向键→可以向后翻页" id="next_photo">下一张</a>

	<a name="next_photo" title="用方向键→可以向后翻页" id="next_photo" href="/online/11458796/photo/1880140149/">下一张</a>

	<a href="http://site.douban.com/106875/widget/public_album/191218/photo/1793130680/#next_photo"  title="用方向键→可以向后翻页" id="next_photo">下一张</a>
	"""
	patt = re.compile(r'<a.+?href="(?P<next>.+?)".*?>下一张</a>')
	def inner_func(html):
		res = re.search(patt, html)
		if res:
			return res.group('next')
		return None
	return inner_func(html)

def parse_photo_nums(html):
	"""Parse current and total number of pages which view a photo.

	<span class="ll">第183张 / 共183张</span>

	<span class='ll'>第1861张/共1861张</span>

	<span class="nums">第149张 / 共149张</span>
	"""
	patt = re.compile(r'<span class=[\'"]\w+[\'"]>第(?P<now>\d+)张\s?/\s?共(?P<total>\d+)张</span>')
	def inner_func(html):
		res = re.search(patt, html)
		if res:
			return res.group('now'), res.group('total')
		return (0, 0)
	return inner_func(html)

def parse_title(html):
	patt = re.compile(r'<title>\s?(.+?)\s?</title>')
	def inner_func(html):
		res = re.search(patt, html)
		if res:
			return res.group(1).strip()
		return 'unname'
	return inner_func(html)

if __name__ == '__main__':
	from fetch import fetch_html

	for url in ['http://www.douban.com/photos/album/57673087/?start=18',
				'http://www.douban.com/online/11458796/album/84984393/?start=30',
				'http://site.douban.com/doubangongyi/widget/photos/11398597/',
				'http://www.douban.com/']:
		html_album = fetch_html(url)
		photoes = parse_photo_preview(html_album)
		title = parse_title(html_album)
		print(title)
		print(len(photoes), photoes)

	for url in ['http://www.douban.com/photos/photo/1240759488/#image',
				'http://www.douban.com/online/11458796/photo/1873720367/',
				'http://site.douban.com/doubangongyi/widget/photos/11398597/photo/1798103424/',
				'http://www.douban.com/']:
		html_photo = fetch_html(url)
		photo = parse_photo_view(html_photo)
		next = parse_photo_next(html_photo)
		now, total = parse_photo_nums(html_photo)
		title = parse_title(html_photo)
		print(title)
		print(photo, next, now, total)