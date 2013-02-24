# -*- coding:utf-8 -*-

"""
Encapsulate html to offer the functions.
"""

from parse import parse_photo_preview, parse_photo_view
from parse import parse_photo_next, parse_photo_nums, parse_title

__all__ = ['Html']

class Html(object):
	"""Handle html."""

	# album photoes' number which one page previews
	album_photo_num = {
		1: 18,
		2: 30,
		3: 30
	}

	def __init__(self, html, dbpurl):
		self.html = html
		self.dbpurl = dbpurl
		self.photonum = 1

	def get_title(self):
		return parse_title(self.html)

	def get_photoes(self):
		category = self.dbpurl.category
		html = self.html
		photoes = []
		# url for previewing the album 
		if category <= 3:
			res = parse_photo_preview(html)
			photoes.extend(res)
			self.photonum = len(res)
		# url for viewing a photo
		else:
			photoes.append(parse_photo_view(html))
		return photoes

	def next_url(self):
		category = self.dbpurl.category
		html = self.html
		next = None
		# url for previewing the album 
		if category <= 3:
			num = self.album_photo_num[category]
			if self.photonum == num:
				next = '%s?start=%d' % (dbpurl.baseurl, dbpurl.start + num)
		# url for viewing a photo
		else:
			now, total = parse_photo_nums(html)
			if now < total:
				next = parse_photo_next(html)
				if next[0] == '/':
					next = self.dbpurl.get_new_url(next)
		return next