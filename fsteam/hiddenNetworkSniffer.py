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
import sys
from scapy.all import *
from colored import *
from time import *
def sniffhidden():
	print '%s Loading Network Decloaker Module%s' % (fg(3), attr(0))
	sleep(4)
	print "\n\tWireless Network Decloaker [\033[1;31mwifi/decloaker\033[1;m] | * de-cloaks hidden\n\t 802.11 networks. This module can parse out the network name\n\t and print it to the screen. Network cards is in monitor mode.\n\n\tUsage: use [module]\n\t[IFACE] - network interface in monitor mode.\n" 
	try:
		interface = str(raw_input("%s[CMD-LINE]:[IFACE]: %s" % (fg(1), attr(0))))
		print (fore.LIGHT_BLUE+" IFACE:["+style.RESET + interface +fore.LIGHT_BLUE+"]"+style.RESET )
		sleep(3)
		hiddenNets = []
		unhiddenNets = []
		print "\n[+] Searching for a hidden network \'"+interface+"\'" 
		sleep(3)
		def sniffDot11(p):
			if p.haslayer(Dot11ProbeResp):
				addr2 = p.getlayer(Dot11).addr2
				if (addr2 in hiddenNets) & (addr2 not in unhiddenNets):
					netName = p.getlayer(Dot11ProbeResp).info
					print '[+] Decloaked Hidden SSID: ' +\
						netName + ' for MAC: ' + addr2
					unhiddenNets.append(addr2)
			if p.haslayer(Dot11Beacon):
				if p.getlayer(Dot11Beacon).info == '':
					addr2 = p.getlayer(Dot11).addr2
					if addr2 not in hiddenNets:
						print '[-] Detected Hidden SSID: ' +\
							'with MAC:' + addr2
					hiddenNets.append(addr2)
		sniff(iface=interface, prn=sniffDot11)

	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating.\n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)
			print "[-] Error Found: "+interface+" not in monitor mode\n"
if __name__=='__main__':
    sniffhidden()
