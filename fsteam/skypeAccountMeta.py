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

import sqlite3
import optparse
import os
from colored import *
from time import *

print '%s Loading Skype Metadata Parser Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tSkype Metadata Parser [\033[1;31mforensic/skypeparser\033[1;m] | * this module\n\t script examines the Skype profile database. This script can\n\t print the profile information, address contacts, call log\n\t and even the messages stored in the target\'s database record.\n\n\tUsage: use [module]\n\t[PATH] - path to database file.\n\t[DATA] - database file.\n'

def printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, country, \
		datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	for row in c:
		print '[*] Found Skype Account'
		print '[+] User           : '+str(row[0])
		print '[+] Skype Username : '+str(row[1])
		print '[+] Location       : '+str(row[2])+','+str(row[3])
		print '[+] Profile Date   : '+str(row[4])
def printContacts(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT displayname, skypename, city, country,\
		phone_mobile, birthday FROM Contacts;")
	for row in c:
		print '\n[*] Found Skype Contact'
		print '[+] User           : ' + str(row[0])
		print '[+] Skype Username : ' + str(row[1])
		if str(row[2]) != '' and str(row[2]) != 'None':
			print '[+] Location       : ' + str(row[2]) + ',' \
				+ str(row[3])
		if str(row[4]) != 'None':
			print '[+] Mobile Number  : ' + str(row[4])
		if str(row[5]) != 'None':
			print '[+] Birthday       : ' + str(row[5])
def printCallLog(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(begin_timestamp,'unixepoch'), \
		identity FROM calls, conversations WHERE \
		calls.conv_dbid = conversations.id;"
			)
	print '\n[*] Found Skype Calls '
	for row in c:
		print '[+] Time: '+str(row[0])+\
			' | Partner: '+ str(row[1])
def printMessages(skypeDB):
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT datetime(timestamp,'unixepoch'), \
		dialog_partner, author, body_xml FROM Messages;")
	print '\n[*] Found Skype Message'
	for row in c:
		try:
			if 'partlist' not in str(row[3]):
				if str(row[1]) != str(row[2]):
					msgDirection = 'To ' + str(row[1]) + ': '
				else:
					msgDirection = 'From ' + str(row[2]) + ': '
				print 'Time: ' + str(row[0]) + ' ' \
					+ msgDirection + str(row[3])		
		except:
			pass
try:	
	def main():
		pathName = str(raw_input(fore.RED+'[CMD-LINE]:[PATH]: '+style.RESET ))
		print (fore.LIGHT_BLUE+" PATH:["+style.RESET + pathName +fore.LIGHT_BLUE+"]"+style.RESET )
		mainDb = str(raw_input(fore.RED+'[CMD-LINE]:[DATA]: '+style.RESET ))
		print (fore.LIGHT_BLUE+" DATA:["+style.RESET + mainDb +fore.LIGHT_BLUE+"]"+style.RESET )
		print '\n[+] Extracting metadata to '+mainDb
		if os.path.isdir(pathName) == False:
			print '[-] Error Found: Path ' + pathName +' does not exist'
			exit(0)
		else:
			skypeDB = os.path.join(pathName, mainDb)
			if os.path.isfile(skypeDB):
				printProfile(skypeDB)
				printContacts(skypeDB)
				printCallLog(skypeDB)
				printMessages(skypeDB)
			else:
				print '[-] Error Found: Skype database '+skypeDB+' does not exist'
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
