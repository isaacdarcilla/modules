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

from scapy.all import *
from colored import *
from time import *
print '%s Loading Probe Sniffer Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tProbe Sniffer [\033[1;31mnet/probesniffer\033[1;m] | * listens for 802.11 probe\n\t requests and prints. This module allows us to see the names\n\t of the networks on the preferred network lists of our clients.\n\n\tUsage: use [module]\n\t[IFACE] - network interface in monitor mode.\n"

try:
	interface = str(raw_input("%s[CMD-LINE]:[IFACE]: %s" % (fg(1), attr(0))))
	print (fore.LIGHT_BLUE+" IFACE:["+style.RESET + interface +fore.LIGHT_BLUE+"]"+style.RESET )
	probeReqs = []
	print '\n[+] Scanning for connections using \''+interface+'\''
	sleep(3)
	def sniffProbe(p):
		if p.haslayer(Dot11ProbeReq):
			netName = p.getlayer(Dot11ProbeReq).info
			if netName not in probeReqs:
				probeReqs.append(netName)
				print '[+] Detected New Probe Request: ' + netName
	sniff(iface=interface, prn=sniffProbe)
	
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
    	#log(error)
    	print "[-] Error Found: "+ str(error)
    	print "[-] Error Found: "+interface+" not in monitor mode\n"
