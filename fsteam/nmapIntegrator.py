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
import nmap
import optparse
from colored import *
from time import *
print '%s Loading Integrated Scanner Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tIntegrated Port Scanner [\033[1;31mnet/portscanner\033[1;m] | * scan for all\n\t available TCP port. An alternative for FTP port scanner.\n\n\tUsage: use [module]\n\t[RHOST] - specify remote host.\n\t[RPORT] - specify remote port.\n"
def nmapinteg():
	try:
		def nmapScan(tgtHost, tgtPort):
			nmScan = nmap.PortScanner()
			nmScan.scan(tgtHost, tgtPort)
			state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
			print "[+] " + tgtHost + " tcp/"+tgtPort +" "+state
		def maincmd():
			parser=optparse.OptionParser("Specify [RHOST] host\nSpecify [RPORT] port")
			tgtHost=str(raw_input("%s[CMD-LINE]:[RHOST]: %s" %(fg(1), attr(0))))			#user input 
			sleep(2)
			print (fore.LIGHT_BLUE+" RHOST:["+style.RESET + tgtHost +fore.LIGHT_BLUE+"]"+style.RESET )
			tgtPort=str(raw_input("%s[CMD-LINE]:[RPORT]: %s" %(fg(1), attr(0))))			#user input
			sleep(2)
			print (fore.LIGHT_BLUE+" RPORT:["+style.RESET + tgtPort +fore.LIGHT_BLUE+"]"+style.RESET) 
			sleep(1)
			print '\n'+'%s[+] Scanning \'%s' % (fg(15), attr(0)) +tgtHost+'\' on port \''+tgtPort+'\'\n'
	
			(options, args) = parser.parse_args()
			tgtHost = tgtHost
			tgtPorts = str(tgtPort).split(', ')
			if (tgtHost == None) | (tgtPorts[0] == None):
				print parser.usage
				exit(0)
			for tgtPort in tgtPorts:
				nmapScan(tgtHost, tgtPort)
			
			fileName = file('Main/logs/iplogs.txt', 'w')
			fileName.truncate()
			fileName.write(str(tgtHost) + " : tcp/" + str(tgtPort) +' scan - Internet Protocol Address Found')

			fileName2 = file('Main/logs/_iplogs.txt', 'w')
			fileName2.truncate()
			fileName2.write(str(tgtHost) + " : tcp/" + str(tgtPort) +' scan - Internet Protocol Address Found')
			os.system('sudo mv Main/logs/_iplogs.txt Main/core/logs')

		if __name__ == '__main__':
			maincmd()
	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating.\n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)+"\n"
if __name__ == '__main__':
	nmapinteg()
