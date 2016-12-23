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


import os
from time import *
from colored import *
import mechanize, cookielib, random
class anonBrowser(mechanize.Browser):
	print fore.BLUE+"\n[+] Activating anonimity. Please wait."+style.RESET
	sleep (3)
	def __init__(self, proxies = [], user_agents = []):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		self.proxies = proxies
		self.user_agents = user_agents + ['Mozilla/4.0 ',\
		'FireFox/6.01','ExactSearch', 'Android7.0/24']
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()
	def clear_cookies(self):
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
	def change_user_agent(self):
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', \
			(self.user_agents[index]))]
	def change_proxy(self):
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies({'http': self.proxies[index]})
	def anonymize(self, sleep = False):
		self.clear_cookies()
		self.change_user_agent()
		self.change_proxy()
		if sleep:
			time.sleep(60)
	print fore.BLUE+"[+] Anonimity Module activated. Enjoy.\n"+style.RESET
	sleep (2)
