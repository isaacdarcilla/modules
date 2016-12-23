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
gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat')

print '%s Loading Packet Mapper Module%s' % (fg(3), attr(0))
sleep(4)
print '\n\tPacket Mapper [\033[1;31mfile/packetmapper\033[1;m] | * this module redirects an\n\t output to a text file with a kml extension. Then opening this\n\t file with Google Earth, we see a visual depiction of our packet\n\t destinations.\n\n\tUsage: use [module]\n\t[PCAP] - packet capture directory.\n'

def retKML(ip):
	rec = gi.record_by_name(ip)
	try:
		longitude = rec['longitude']
		latitude = rec['latitude']
		kml = (
			'<Placemark>\n'
			'<name>%s</name>\n'
			'<Point>\n'
			'<coordinates>%6f,%6f</coordinates>\n'
			'</Point>\n'
			'</Placemark>\n'
			)%(ip,longitude, latitude)
		return kml
	except:
		return ''
def plotIPs(pcap):
	kmlPts = ''
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			srcKML = retKML(src)
			dst = socket.inet_ntoa(ip.dst)
			dstKML = retKML(dst)
			kmlPts = kmlPts + srcKML + dstKML
		except:
			pass
	return kmlPts
try:	
	def main():
		pcapFile = str(raw_input(fore.RED+'[CMD-LINE]:[PCAP]: '+style.RESET ))
		print (fore.LIGHT_BLUE+" PCAP:["+style.RESET + pcapFile +fore.LIGHT_BLUE+"]"+style.RESET )
		print '\n[+] Initializing packet mapper'

		f = open(pcapFile)
		pcap = dpkt.pcap.Reader(f)
		kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\
			\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
		kmlfooter = '</Document>\n</kml>\n'
		kmldoc=kmlheader+plotIPs(pcap)+kmlfooter
		print kmldoc
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
