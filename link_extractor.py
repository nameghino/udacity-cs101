#!/usr/bin/python

import sys, urllib2

def extract_link(s, i=0):
	tag = '<a href="'
	start_tag = s.find(tag, i)
	if start_tag == -1:
		return {'url': None, 'range': (-1, -1)}
	closing = "</a>"
	end_tag = s.find(closing , start_tag) + len(closing)
	rng = (start_tag, end_tag)
	url = s[rng[0]:rng[1]]
	return {'url': url, 'range': rng}


def extract_all_links(page):
	last_range = (0,0)
	while (True):
		d = extract_link(page, last_range[1])
		if (d['url'] == None):
			break
		print d['url']
		last_range = d['range']

if __name__ == '__main__':
	page = sys.argv[1] 
	print 'Fetching content...'
	contents = urllib2.urlopen(page).read()
	extract_all_links(contents)