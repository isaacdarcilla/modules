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
from time import *
from colored import *
from scapy.all import *

print '%s Loading Domain Detector Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tDomain Detector [\033[1;31mweb/domain\033[1;m] | * enumerate packet captured\n\t file and analyze a domain or a machine infected with Conficker.\n\n\tUsage: use [module]\n\t[PCAP] - packet capture file.\n"
try:
	def dnsQRTest(pkt):
		if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
			rcode = pkt.getlayer(DNS).rcode
			qname = pkt.getlayer(DNSQR).qname
			if rcode == 3:
				print '[-] Name request lookup failed: ' + qname
			return True
		else:
			return False
	def main():
		unAnsReqs = 0
		pkts = rdpcap(str(raw_input(fore.RED+'[CMD-LINE]:[PCAP]: '+style.RESET ))) #domain cap file here

		
		for pkt in pkts:
			if dnsQRTest(pkt):
				unAnsReqs = unAnsReqs + 1
		print " "
		print '[+] '+str(unAnsReqs)+' Total Unanswered Name Requests'
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
	print "\n[-] Error Found: "+ str(error)+"\n"
