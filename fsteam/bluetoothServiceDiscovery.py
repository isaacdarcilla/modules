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
#Bluetooth Service Discovery Protocol

import os
from time import *
from colored import *
from bluetooth import *

print '%s Loading Bluetooth SDP Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tBluetooth Service Discovery [\033[1;31mbluetooth/btsdp\033[1;m] | * describing\n\t and enumerating the types of Bluetooth profiles and services\n\t offered by a device\n\n\tUsage: use [module]\n\t[BTADDR] - specify bluetooth address.\n"
btaddr = raw_input("%s[CMD-LINE]:[BTADDR]: %s" %(fg(1), attr(0)))
print (fore.LIGHT_BLUE+" BTADDR:["+style.RESET + btaddr +fore.LIGHT_BLUE+"]"+style.RESET )
print "\n[+] Scanning BT Profiles and Services \'"+btaddr+"\'\n"
try:
	
	def sdpBrowse(addr):
		services = find_service(address=addr)
		for service in services:
			name = service['name']
			proto = service['protocol']
			port = str(service['port'])
			print '[+] Found ' + str(name)+' on '+\
				str(proto) + ':'+port
	sdpBrowse(btaddr)

except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating.\n"+style.RESET)
except Exception, error: #handle exceptions
			#log(error)
		print "[-] Error Found: "+ str(error)+"\n"
