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
from scapy.all import *
from time import *
def scapyscan():
	print '%s Loading Packet Sniffer Module%s' % (fg(3), attr(0))
	sleep(4)
	print "\n\tPacket Sniffer [\033[1;31mnet/packetsniffer\033[1;m] | * automatically print out\n\t the source IP addresses. Also print Time To Live [TTL] of incoming\n\t packets.\n\n\tUsage: use net/scapyscan"
	print '\n[+] Receiving incoming packets'
	try:
		def testTTL(pkt):
			try:
				if pkt.haslayer(IP):
					ipsrc = pkt.getlayer(IP).src
					ttl = str(pkt.ttl)
					print '[+] Pkt Received From: '+ipsrc+' with TTL: ' \
					+ ttl
			except:
				pass
		def main():
			sniff(prn=testTTL, store=0)
		if __name__ == '__main__':
			main()
	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)+"\n"
if __name__ == '__main__':
	scapyscan()
