# -*- coding:utf-8 -*-

import os
import re
import sys
import urllib

from core.fetch import fetch_html, fetch_img
from core.html import Html
from core.url import DbpUrl, dl_photo_url
from utils.cn_path import make_dirs_cn, u2c
from utils.size import approximate

counter = 0

def u2c_print(s):
	print(u2c(s))

def dl_photos(photo_list):
	for photo, dl_url in photo_list:
		filename, httpmsg = fetch_img(dl_url, photo)
		length = httpmsg.getheader('Content-Length')
		u2c_print('下载完成 %d %s %s' % (counter, filename, approximate(length)))

def get_photo_list(photoes, preview=False):
	global counter
	for photo in photoes:
		counter += 1
		yield (photo, dl_photo_url(photo, preview))

def parse_html(dbpurl):
	global counter

	# fetch html
	src = fetch_html(dbpurl.get_url())
	html = Html(src, dbpurl)

	out_dir = html.get_title()

	# enter album
	cn_dirpath = make_dirs_cn(out_dir)
	os.chdir(cn_dirpath)

	# create album
	print(u2c('\n创建相册 ') + cn_dirpath)
	counter = 0

	# download
	photoes = html.get_photoes()
	dl_photos(get_photo_list(photoes))

	# continue download
	next = html.next_url()

	def parse_next(next):
		dbpurl = DbpUrl(next)
		# fetch html
		src = fetch_html(dbpurl.get_url())
		html = Html(src, dbpurl)
		# download photoes
		photoes = html.get_photoes()
		dl_photos(get_photo_list(photoes))
		next = html.next_url()
		if next:
			parse_next(next)

	if next:
		parse_next(next)

	# leave album
	os.chdir('..')
	u2c_print('下载总数 %d张' % counter)

def dbp_loop():
	try:
		while True:
			url = raw_input(u2c('\n输入豆瓣相册地址: '))
			dbpurl = DbpUrl(url)
			if dbpurl.is_valid():
				parse_html(dbpurl)
			else:
				u2c_print('输入地址不合法TT')
	except (KeyboardInterrupt, SystemExit):
		# user wants to quit
		res = raw_input(u2c('\n确认退出程序？(Y/N)'))
		if res not in 'yY':
			dbp_loop()
	except Exception:
		u2c_print('\n出错误了TT！')
		dbp_loop()

def main():
	import readline
	readline.parse_and_bind("control-v: paste")

	u2c_print("""豆瓣相册下载小脚本
1）支持相册：用户相册、线上活动相册、豆瓣小站相册。
2）支持地址：预览相册地址、查看图片地址。
3）图片下载仅从当前地址开始至结束，下载全部需从第一页开始。""")

	# main loop
	dbp_loop()

def test():
	albums = [
		'http://www.douban.com/photos/album/85642820/', # 7
		'http://www.douban.com/online/10859460/album/51259013/', # 11
		'http://site.douban.com/story/widget/photos/5857547/', # 4
		'http://www.douban.com/photos/photo/1600191811/', # 3
		'http://www.douban.com/online/11458796/photo/1852757882/', # 5
		'http://site.douban.com/doubangongyi/widget/photos/11398597/photo/1775979493/' # 2
	]
	for url in albums:
		dbpurl = DbpUrl(url)
		if dbpurl.is_valid():
			parse_html(dbpurl)
		else:
			print('unaccepted url')

if __name__ == '__main__':
	main()