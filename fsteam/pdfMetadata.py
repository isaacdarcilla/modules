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
# THE SOFTWARE.
#

import pyPdf
import optparse
from colored import *
from time import *
from pyPdf import PdfFileReader

print '%s Loading Pdf Metadata Parser Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tPdf Metadata Parser [\033[1;31mforensic/pdfparser\033[1;m] | * this module\n\t script extracts information such as the author. This will\n\t parse the metadata from a .pdf file extension.\n\n\tUsage: use [module]\n\t[FILE] - target file directory\n'


def printMeta(fileName):
	pdfFile = PdfFileReader(file(fileName, 'rb'))
	docInfo = pdfFile.getDocumentInfo()
	print '[+] PDF Metadata for: ' + str(fileName)
	for metaItem in docInfo:
		print '[+] ' + metaItem + ':' + docInfo[metaItem]
try:
	def main():
		fileName = str(raw_input("%s[CMD-LINE]:[FILE]: %s" % (fg(1), attr(0))))	
		print (fore.LIGHT_BLUE+" FILE:["+style.RESET + fileName +fore.LIGHT_BLUE+"]\n"+style.RESET )
		sleep(2)

		printMeta(fileName)
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
