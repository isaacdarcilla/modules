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

import dpkt
import optparse
import socket
import os
from colored import *
from time import *

THRESH = 1000

print '%s Loading DDOS Tracker Module%s' % (fg(3), attr(0))
sleep(4)
print "\n\tDDOS Tracker [\033[1;31mweb/ddostracker\033[1;m] | * this script detects the\n\t download and usage of loic app, overhears the HIVE commands\n\t and provide overwhelming evidence to prove user participated\n\t in an Anonymous-sponsored DDoS attack.\n\n\tUsage: use [module]\n\t[PCAP] - packet capture directory.\n"

def findDownload(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			tcp = ip.data
			http = dpkt.http.Request(tcp.data)
			if http.method == 'GET':
				uri = http.uri.lower()
			if '.zip' in uri and 'loic' in uri:
				print '[!] ' + src + ' Downloaded LOIC.'
		except:
			pass
def findHivemind(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			sport = tcp.sport
			if dport == 6667:
				if 'loic' in tcp.data.lower():
					print '[!] DDoS Hivemind issued by: '+src
					print '[+] Target CMD: ' + tcp.data
			if sport == 6667:
				if 'loic' in tcp.data.lower():
					print '[!] DDoS Hivemind issued to: '+src
					print '[+] Target CMD: ' + tcp.data
		except:
			pass
def findAttack(pcap):
	pktCount = {}
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			if dport == 80:
				stream = src + ':' + dst
				if pktCount.has_key(stream):
					pktCount[stream] = pktCount[stream] + 1
				else:
					pktCount[stream] = 1
		except:
			pass
	for stream in pktCount:
		pktsSent = pktCount[stream]
		if pktsSent > THRESH:
			src = stream.split(':')[0]
			dst = stream.split(':')[1]
			print '[+] '+src+' attacked '+dst+' with ' \
				+ str(pktsSent) + ' pkts.'
try:
	def main():
		pcapFile = str(raw_input(fore.RED+'[CMD-LINE]:[PCAP]: '+style.RESET ))	
		print (fore.LIGHT_BLUE+" PCAP:["+style.RESET + pcapFile +fore.LIGHT_BLUE+"]"+style.RESET )

		print '\n[+] Initializing loic tracker'

		f = open(pcapFile)
		pcap = dpkt.pcap.Reader(f)
		findDownload(pcap)
		findHivemind(pcap)
		findAttack(pcap)
	if __name__ == '__main__':
		main()
except KeyboardInterrupt:
	print (fore.BLUE+"\n\n[+] Interrupted by user. Terminating. \n"+style.RESET)
	sleep(2)
except Exception, error: #handle exceptions
		print "[-] Error Found: "+ str(error)
