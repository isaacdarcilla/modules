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
#

import dpkt
import socket
import pygeoip
import optparse
import os
from colored import *
from time import *

print '%s Loading Packet Tracker Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tPacket Tracker [\033[1;31mnet/packettracker\033[1;m] | * this powerful packet\n\t analysis toolkit will allow us to see the physical destinations\n\t of our target\'s packets.\n\n\tUsage: use [module]\n\t[PCAP] - packet capture directory.\n'

gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat')
def retGeoStr(ip):
	try:
		rec = gi.record_by_name(ip)
		city = rec['city']
		country = rec['country_code3']
		if city != '':
			geoLoc = city + ', ' + country
		else:
			geoLoc = country
		return geoLoc
	except Exception, e:
		return 'Unregistered'
def printPcap(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] '+fore.RED+"Source: "+style.RESET + src + fore.GREEN+' Destination: '+style.RESET + dst
			print '[+] '+fore.RED+"Source: "+style.RESET + retGeoStr(src) + fore.GREEN+' Destination: '+style.RESET \
				+ retGeoStr(dst)
		except:
			pass
try:	
	def main():
		pcapFile = str(raw_input(fore.RED+'[CMD-LINE]:[PCAP]: '+style.RESET ))
		print (fore.LIGHT_BLUE+" PCAP:["+style.RESET + pcapFile +fore.LIGHT_BLUE+"]"+style.RESET )

		print '\n[+] Initializing packet tracker'

		f = open(pcapFile)
		pcap = dpkt.pcap.Reader(f)
		printPcap(pcap)
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
