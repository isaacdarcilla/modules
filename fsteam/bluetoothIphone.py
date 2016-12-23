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

#it identifies the MAC addresses of an iPhone 802.11 Wireless Radio and its Bluetooth MAC addresses
import os
from time import *
from colored import *
from scapy.all import *
from bluetooth import *

def bluetoothmac():
	print '%s Loading Mac Identifier Module%s' % (fg(3), attr(0))
	sleep(4)
	print "\n\tMac Identifier [\033[1;31mbluetooth/macbtid\033[1;m] | * it identifies the MAC\n\t addresses of an iPhone 802.11 Wireless Radio and its Bluetooth\n\t MAC addresses."
	try:
		print '\n[+] Detecting for 802.11 Wireless Radio'
		def retBtAddr(addr):
			btAddr=str(hex(int(addr.replace(':', ''), 16) + 1))[2:]
			btAddr=btAddr[0:2]+":"+btAddr[2:4]+":"+btAddr[4:6]+":"+\
			btAddr[6:8]+":"+btAddr[8:10]+":"+btAddr[10:12]
			return btAddr
		def checkBluetooth(btAddr):
			btName = lookup_name(btAddr)
			if btName:
				print '[+] Detected Bluetooth Device: ' + btName
			else:
				print '[-] Failed to Detect Bluetooth Device.'
		def wifiPrint(pkt):
			iPhone_OUI = 'd0:23:db'
			if pkt.haslayer(Dot11):
				wifiMAC = pkt.getlayer(Dot11).addr2
				if iPhone_OUI == wifiMAC[:8]:
					print '[*] Detected iPhone MAC: ' + wifiMAC
					btAddr = retBtAddr(wifiMAC)
					print '[+] Testing Bluetooth MAC: ' + btAddr
					checkBluetooth(btAddr)
		conf.iface = 'hci0'
		sniff(prn=wifiPrint)

	except KeyboardInterrupt:
		print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
		sleep(2)
	except Exception, error: #handle exceptions
			#log(error)
			print "[-] Error Found: "+ str(error)+"\n"
if __name__=='__main__':
    bluetoothmac()
