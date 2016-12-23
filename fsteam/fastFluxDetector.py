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
from colored import *
from time import *
from scapy.all import *
dnsRecords = {}
print '%s Loading Fast Flux Detector Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tFast Flux Detector [\033[1;31mweb/fastflux\033[1;m] | * this module print\n\t out all the domain names and how many unique IP addresses exist\n\t for each domain name.\n\n\tUsage: use [module]\n\t[PCAP] - packet capture file.\n"
try:
	def handlePkt(pkt):
		if pkt.haslayer(DNSRR):
			rrname = pkt.getlayer(DNSRR).rrname
			rdata = pkt.getlayer(DNSRR).rdata
			if dnsRecords.has_key(rrname):
				if rdata not in dnsRecords[rrname]:
					dnsRecords[rrname].append(rdata)
			else:
				dnsRecords[rrname] = []
				dnsRecords[rrname].append(rdata)
	def main():
		pkts = rdpcap(str(raw_input(fore.RED+'[CMD-LINE]:[PCAP]: '+style.RESET )))   #domain capture file

		for pkt in pkts:
			handlePkt(pkt)
		for item in dnsRecords:
			print " "
			print '[+] '+item+' has '+str(len(dnsRecords[item])) \
			+ ' unique IPs.'
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
	print "\n[-] Error Found: "+ str(error)+"\n"
