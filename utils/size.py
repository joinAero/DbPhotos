# -*- coding:utf-8 -*-

__all__ = ['approximate']

_suffixes = {
	1024: ['B', 'KB', 'MB', 'GB', 'TB']
}

def approximate(size, multiple=1024):
	'''Return a size with appropriate unit to display.'''
	if isinstance(size, str):
		size = int(size)
	suffixes = _suffixes[multiple]
	last_suffix = suffixes[-1]
	rem = 0
	for suffix in suffixes:
		if size < multiple:
			m_suffix = suffix
			break
		if suffix == last_suffix:
			m_suffix = last_suffix
			break
		size, rem = divmod(size, multiple)
	return ' '.join(['%d.%02d' % (size, 100 * rem / multiple), m_suffix])

if __name__ == '__main__':
	for i in range(5):
		size = 1024 ** (i + 1) + (1024 ** i) * 50
		print '%d B = %s' % (size, approximate(size))