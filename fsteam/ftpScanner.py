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

import optparse
from socket import *
from threading import *
from time import *
from colored import *
def ftpscanner():	
	print '%s Loading FTP Scanner Module%s' % (fg(3), attr(0))
	sleep(4)
	print "\n\tFTP Port Scanner [\033[1;31mnet/ftpscanner\033[1;m] | * scan for open FTP ports\n\t and print. This will allow you to view open ports and start\n\t an attack.\n\n\tUsage: use [module]\n\t[RHOST] - specify remote host.\n\t[RPORT] - specify remote port.\n" 	

	try:
		screenLock = Semaphore(value=1)
		def connScan(tgtHost, tgtPort):
			try:
				connSkt = socket(AF_INET, SOCK_STREAM) #This function creates an
													   #instance of a new socket given the family.
				connSkt.connect((tgtHost, tgtPort))
				connSkt.send('[+] Can we talk in private?\r\n')
				results = connSkt.recv(100)
				screenLock.acquire()
				print '[+] %d/tcp open'% tgtPort
				print '\n[+] ' + str(results)
			except:
				screenLock.acquire()
				print '[-] %d/tcp closed'% tgtPort
			finally:
				#screenLock,release()
				connSkt.close()	

		def portScan(tgtHost, tgtPorts):
			try:
				tgtIP = gethostbyname(tgtHost) #This function takes a hostname such
											   #as www.syngress.com and returns an IPv4 address 
											   #format such as 69.163.177.2.
			except:
				print "%s[-] Cannot resolve '%s': Unknown host%s" % (fg(1), attr(0)) %tgtHost
				return
			try:
				tgtName = gethostbyaddr(tgtIP) #This function takes an IPv4 address
											   #and returns a triple containing the hostname 
				print '\n[+] Scan Results for: ' + tgtName[0]
			except:
				print '\n[+] Scan Results for: ' + tgtIP
			setdefaulttimeout(1)
			for tgtPort in tgtPorts:
				t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
				t.start()

		def main():
			tgtHost=str(raw_input("%s[CMD-LINE]:[RHOST]: %s" % (fg(1), attr(0))))  #its should be the real ip
			print (fore.LIGHT_BLUE+" RHOST:["+style.RESET + tgtHost +fore.LIGHT_BLUE+"]"+style.RESET )
			sleep(3)
			tgtPort=str(raw_input("%s[CMD-LINE]:[RPORT]: %s" % (fg(1), attr(0))))  #port can be separated by ',' [eg. 80, 	8080, 808]
			print (fore.LIGHT_BLUE+" RPORT:["+style.RESET + tgtPort +fore.LIGHT_BLUE+"]"+style.RESET )
			sleep(3)
			print '\n[+] Scanning \''+tgtHost+'\' for open ports'
			sleep(2)
		
			tgtPorts = str(tgtPort).split(', ')
			if (tgtHost == None) | (tgtPorts[0] == None):
				print parser.usage
				exit(0)
			portScan(tgtHost, tgtPorts)
		if __name__ == "__main__":
			main()


	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)
if __name__ == "__main__":
	ftpscanner()
