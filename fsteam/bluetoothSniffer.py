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
#we can locate any nearby Bluetooth devices.

import os
from time import *
from colored import *
from bluetooth import *
alreadyFound = []

print '%s Loading Bluetooth Sniffer Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tBluetooth MAC Sniffer [\033[1;31mbluetooth/btsniffer\033[1;m] | * scan for all nearby\n\t available Bluetooth devices\n\n\tUsage: use [module]\n\t"
sleep(1)
print "[+] Scanning nearby Bluetooth signals\n"
try:	
	def findDevs():		
		foundDevs = discover_devices(lookup_names=True)
		for (addr, name) in foundDevs:
			if addr not in alreadyFound:
				print '[+] Found Bluetooth Device: ' + str(name)
				print '[+] MAC address: ' + str(addr)
				alreadyFound.append(addr)
				fileName = file('Main/logs/btlogs.txt', 'w')
				fileName.truncate()
				fileName.write(str(addr) + " : " + str(name) +' - Bluetooth MAC Address Found')

				fileName2 = file('Main/logs/_btlogs.txt', 'w')
				fileName2.truncate()
				fileName2.write(str(addr) + " : " + str(name) +' - Bluetooth MAC Address Found')
				os.system('sudo mv Main/logs/_btlogs.txt Main/core/logs') 
	while True:
		findDevs()

except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating.\n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		#log(error)
		print "[-] Error Found: "+ str(error)+"\n"
