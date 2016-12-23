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

import mechanize
import cookielib
from os import *
import os
from colored import *
from time import *
def cookiehijack():	
	print '%s Loading Cookie Hijacker Module%s' % (fg(3), attr(0))
	sleep(4)
	print "\n\tCookie Hijacker [\033[1;31mnet/cookiehijack\033[1;m] | * print the cookies\n\t stored during the session. The attacker and the target \n\t should be on the same network. Only works on HTTP protocol.\n\t Use \'sslstrip\' first.\n\n\tUsage: use [module]\n\t[URL] - specify target url.\n"
	try:
		def printCookies(url):
				browser = mechanize.Browser()
				cookie_jar = cookielib.LWPCookieJar()
				browser.set_cookiejar(cookie_jar)
				page = browser.open(url)
				for cookie in cookie_jar:
					print cookie
				
		url = str(raw_input("%s[CMD-LINE]:[URL]: %s"%(fg(1), attr(0))))
		print (fore.LIGHT_BLUE+"URL:[ "+style.RESET+url+fore.LIGHT_BLUE+']'+style.RESET)
		sleep(2)
		print '\n[+] Locating \'cookies\' from '+'\''+url+'\''
		sleep(3)
		printCookies(url)

	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)+"\n"
if __name__=='__main__':
    cookiehijack()
