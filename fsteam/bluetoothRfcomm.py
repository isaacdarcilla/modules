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

#This vulnerability targeted the Bluetooth RFCOMM transport protocol

from colored import *
from bluetooth import *
from time import *

print '%s Loading Bluetooth RFCOMM Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tBluetooth RFCOMM Scanner [\033[1;31mbluetooth/btrfcomm\033[1;m] | * scan for an open\n\t RFCOMM port protocol and prints in screen.\n\n\tUsage: use [module]\n\t[BTADDR] - specify bluetooth address.\n\t[MVALUE] - specify maximum value.\n"
try:	
	tgtBt = raw_input("%s[CMD-LINE]:[BTADDR]: %s" %(fg(1), attr(0)))
	
	print (fore.LIGHT_BLUE+" BTADDR:["+style.RESET + tgtBt +fore.LIGHT_BLUE+"]"+style.RESET )

	maxVal = int(raw_input("%s[CMD-LINE]:[MVALUE]: %s" %(fg(1), attr(0))))
	print (fore.LIGHT_BLUE+" BTADDR:["+style.RESET + str(maxVal) +fore.LIGHT_BLUE+"]"+style.RESET )
	print "\n[+] Scanning Bluetooth Address \'"+tgtBt+"\'"+"\n"
	def rfcommCon(addr, port):
		sock = BluetoothSocket(RFCOMM)
		try:
			sock.connect((addr, port))
			print '[+] RFCOMM Port ' + str(port) + ' open'
			sock.close()
		except Exception, e:
			print '[-] RFCOMM Port ' + str(port) + ' closed'
	for port in range(1, maxVal):
		rfcommCon(tgtBt, port)

except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating.\n"+style.RESET)
except Exception, error: #handle exceptions
			#log(error)
		print "[-] Error Found: "+ str(error)+"\n"

