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

import os
import gzip
import zipfile, optparse
from threading import Thread
from colored import *
from time import *
print '%s Loading Zip Cracker Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tZip-file Password Cracker [\033[1;31mfile/filecracker\033[1;m] | * this module\n\t cracks password encrypted zip files. Two argument must be\n\t given. The default file extension is \033[1;31m.zip | *.zip\033[1;m files.\n\n\tUsage: use [module]\n\t[ZIPFL] - specify zip file directory.\n\t[PASSL] - specify password list directory.\n"
try:
	def extractFile(zFile, passwords):
		try:
			zFile.extractall(pwd=passwords)
			print '[+] Found password ' + passwords
		except:
			pass	
	def main():
		pass
		parser=optparse.OptionParser("Specify [ZIPFL] directory\nSpecify [PASSL] directory")	
		zname=str(raw_input("%s[CMD-LINE]:[ZIPFL]: %s" % (fg(1), attr(0))))			#user input for zip file
		print (fore.LIGHT_BLUE+" ZIPFL:["+style.RESET + zname +fore.LIGHT_BLUE+"]"+style.RESET )
		sleep(3)
		dname=str(raw_input("%s[CMD-LINE]:[PASSL]: %s" % (fg(1), attr(0))))			#user input for pass list
		print (fore.LIGHT_BLUE+" PASSL:["+style.RESET + dname +fore.LIGHT_BLUE+"]"+style.RESET )
		sleep(3)
		print '\n[+] Cracking credentials for \''+zname+'\''
		(options, args)=parser.parse_args()
		if (zname == None) | (dname == None):
			print parser.usage
			exit(0)
		else:
			zname = zname
			dname = dname
		zFile = zipfile.ZipFile(zname)
		passFile = open(dname)
		for line in passFile.readlines():
			passwords = line.strip('\n')
			t = Thread(target=extractFile, args=(zFile, passwords))
			t.start()
	if __name__ == '__main__':
		main()	 
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
    	#log(error)
    	print "[-] Error Found: "+ str(error)
    	print "[-] Error Found: Check directory\n "
