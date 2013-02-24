# -*- coding:utf-8 -*-

"""
# user album 用户相册

http://www.douban.com/photos/album/57673087/
http://www.douban.com/photos/album/57673087/?start=0
http://www.douban.com/photos/album/57673087/?start=18

> http://img3.douban.com/view/photo/thumb/public/p1240753935.jpg

# a photo of user album

http://www.douban.com/photos/photo/1240759488/
http://www.douban.com/photos/photo/1240759488/#image

> http://img3.douban.com/view/photo/photo/public/p1240759488.jpg

=====

# online activity album 线上活动相册

http://www.douban.com/online/11458796/album/84984393/
http://www.douban.com/online/11458796/album/84984393/?start=0
http://www.douban.com/online/11458796/album/84984393/?start=30

> http://img3.douban.com/view/photo/thumb/public/p1873720367.jpg

# a photo of online activity album

http://www.douban.com/online/11458796/photo/1873720367/

> http://img3.douban.com/view/photo/photo/public/p1873720367.jpg

=====

# douban site album 豆瓣小站相册

http://site.douban.com/106875/widget/public_album/191218/
http://site.douban.com/106875/widget/public_album/191218/?start=0
http://site.douban.com/106875/widget/public_album/191218/?start=30

http://site.douban.com/doubangongyi/widget/photos/11398597/

> http://img3.douban.com/view/photo/thumb/public/p1868859228.jpg

=====

# a photo of douban site album

http://site.douban.com/106875/widget/public_album/191218/photo/1695086563/
http://site.douban.com/106875/widget/public_album/191218/photo/1695086563/#next_photo

http://site.douban.com/doubangongyi/widget/photos/11398597/photo/1798103424/

> http://img3.douban.com/view/photo/photo/public/p1868858355.jpg
"""

from urlparse import urlparse, urlunparse, urljoin

from parse import parse_url

__all__ = ['DbpUrl', 'dl_photo_url']

class DbpUrl(object):
	"""Douban photos' url."""

	# url category
	category = {
		1: 'user album',
		2: 'online activity album',
		3: 'douban site album',
		4: 'a photo of user album',
		5: 'a photo of online activity album',
		6: 'a photo of douban site album',
	}

	def __init__(self, url):
		self.category = parse_url(url)
		if self.is_valid():
			(scheme, netloc, path, params, query, fragment) = urlparse(url)
			self.scheme = scheme
			self.netloc = netloc
			self.baseurl = urlunparse((scheme, netloc, path, '', '', ''))
			self.start = None
			if self.category <= 3:
				self.start = 0
				if query:
					self.start = int(query[query.rindex('=')+1:])
		else:
			self.baseurl = None
			self.start = None

	def __str__(self):
		if self.is_valid():
			return 'baseurl=%s, category=%s, start=%s' % \
				(self.baseurl, self.category, self.start)
		else:
			return 'unexpected url'

	__repr__ = __str__

	def is_valid(self):
		return self.category != None

	def get_url(self):
		if self.start: # or self.start != None
			return '%s?start=%d' % (self.baseurl, self.start)
		return self.baseurl

	def get_new_url(self, path):
		return urlunparse((self.scheme, self.netloc, path, '', '', ''))

def dl_photo_url(photo, preview=False):
	photo_preview = 'http://img3.douban.com/view/photo/thumb/public/'
	photo_view = 'http://img3.douban.com/view/photo/photo/public/'
	def inner_func(preview):
		if preview:
			return photo_preview + photo
		else:
			return photo_view + photo
	return inner_func(preview)

if __name__ == '__main__':
	dashes = '-' * 20
	for line in __doc__.splitlines():
		line = line.strip()
		if not line or line[0] in ('#', '>', '='):
			continue
		print(line)
		print(DbpUrl(line))
		print(dashes)
	print(DbpUrl('http://www.douban.com/people/HeLeNNeLeH/notes'))