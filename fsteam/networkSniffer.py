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
print '%s Loading Traffic Sniffer Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tNetwork Sniffer [\033[1;31mnet/networksniffer\033[1;m] | * this module scan for\n\t traffic that includes the 802.11 Probe Requests looking for\n\t networks, 802.11 Beacon Frames indicating traffic, and a DNS\n\t and TCP packet.\n\n\tUsage: use [module]\n\t[IFACE] - interface in monitor mode.\n"
try:
	def pktPrint(pkt):
		if pkt.haslayer(Dot11Beacon):
			print '[+] Detected 802.11 Beacon Frame'
		elif pkt.haslayer(Dot11ProbeReq):
			print '[+] Detected 802.11 Probe Request Frame'
		elif pkt.haslayer(TCP):
			print '[+] Detected a TCP Packet'
		elif pkt.haslayer(DNS):
			print '[+] Detected a DNS Packet'
	interface =str(raw_input("%s[CMD-LINE]:[IFACE]: %s" % (fg(1), attr(0))))	
	print (fore.LIGHT_BLUE+" IFACE:["+style.RESET + interface +fore.LIGHT_BLUE+"]"+style.RESET )
	conf.iface = interface
	print '\n[+] Starting network sniffing using \''+interface+'\''
	sniff(prn=pktPrint)
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
