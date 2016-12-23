# coding: utf-8
# Copyright (c) 2015-2016 Free Security Team
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#

import os
import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
from colored import *
from time import *

print '%s Loading Metadata Parser Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tExif Metadata [\033[1;31mforensic/exifmetadata\033[1;m] | * this script will able\n\t to connect to a URL address, parse and download all the images\n\t files, and test each file for Exif metadata. Then it will\n\t download the file and test it for GPS metadata.\n\n\tUsage: use [module]\n\t[LINK] - url link of the target.\n'

def findImages(url):
	print '[+] Finding images on ' + url
	urlContent = urllib2.urlopen(url).read()
	soup = BeautifulSoup(urlContent)
	imgTags = soup.findAll('img')
	return imgTags
def downloadImage(imgTag):
	try:
		print '[+] Dowloading image...'
		imgSrc = imgTag['src']
		imgContent = urllib2.urlopen(imgSrc).read()
		imgFileName = basename(urlsplit(imgSrc)[2])
		imgFile = open(imgFileName, 'wb')
		imgFile.write(imgContent)
		imgFile.close()
		return imgFileName
	except:
		return ''
def testForExif(imgFileName):
	try:
		exifData = {}
		imgFile = Image.open(imgFileName)
		info = imgFile._getexif()
		if info:
			for (tag, value) in info.items():
				decoded = TAGS.get(tag, tag)
				exifData[decoded] = value
			exifGPS = exifData['GPSInfo']
			if exifGPS:
				print '[*] ' + imgFileName + \
					' contains GPS MetaData'
	except:
		pass
try:
	def main():
		url = str(raw_input(fore.RED+'[CMD-LINE]:[LINK]: '+style.RESET ))	
		print (fore.LIGHT_BLUE+" LINK:["+style.RESET + url +fore.LIGHT_BLUE+"]\n"+style.RESET )
		imgTags = findImages(url)
		for imgTag in imgTags:
			imgFileName = downloadImage(imgTag)
			testForExif(imgFileName)
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
