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
import os
from colored import *
from time import *

print '%s Loading Skype Metadata Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tSkype Metadata [\033[1;31mforensic/skypedata\033[1;m] | * this script will able\n\t to automate extraction process and extra information from\n\t several different columns and tables in the database. For\n\t each result returned, it contains indexed columns for the\n\t user, skype username, location, and profile date.\n\n\tUsage: use [module]\n\t[DATA] - database file directory.\n'

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
try:	
	def main():
		skypeDB = str(raw_input(fore.RED+'[CMD-LINE]:[DATA]: '+style.RESET ))
		print (fore.LIGHT_BLUE+" DATA:["+style.RESET + skypeDB +fore.LIGHT_BLUE+"]"+style.RESET )
		print '\n[+] Extracting metadata to '+skypeDB
		printProfile(skypeDB)
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
