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
import pygeoip												#http://code.google.com/p/pygeoip/
from time import *
from colored import *
gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat')     	#default database install directory
print '%s Loading IP Geolocator Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tIP Geolocator [\033[1;31mweb/iplocate\033[1;m] | * This module tracks down target\n\t public IP address in a less precise way. This will allow you\n\t to view the region, city, and country of a target.\n\n\tUsage: use [module]\n\t[IPADDR] - specify address.\n"
try:
	def printRecord(tgt):
		rec = gi.record_by_name(tgt)
		city = rec['city']
		region = rec['region_name']
		country = rec['country_name']
		long = rec['longitude']
		lat = rec['latitude']
		print '\n[+] Geolocating target address \''+tgt+'\''
		print '\n[+] Target: ' + tgt + ' Geo-located. '
		print '[+] '+str(city)+', '+str(region)+', '+str(country)
		print '[+] Latitude: '+str(lat)+ ', Longitude: '+ str(long)
	tgt = str(raw_input(fore.RED+'[CMD-LINE]:[IPADDR]: '+style.RESET))	#target host acquired
	printRecord(tgt)
except Exception, error:
	print "\n[-] Error Found: "+str(error)
	print "[-] Unable to fetch data for \'"+tgt+"\'"
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
