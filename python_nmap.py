#!/usr/bin/python
#ip address need to be changed accordingly
import sys
import os
import nmap # import nmap.py module
try:
    nm = nmap.PortScanner() # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)
nm.scan('10.0.2.7', '22-443') # scan host 10.0.2.7, ports from 22 to 443
nm.command_line() # get command line used for the scan : nmap -oX - -p 22-443 10.0.2.7
nm.scaninfo() # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts() # get all hosts that were scanned
nm['10.0.2.7'].hostname() # get one hostname for host 10.0.2.7, usualy the user record
nm['10.0.2.7'].hostnames() # get list of hostnames for host 10.0.2.7 as a list of dict [{'name':'hostname1', 'type':'PTR'>
nm['10.0.2.7'].state() # get state of host 10.0.2.7 (up|down|unknown|skipped)
nm['10.0.2.7'].all_protocols() # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
if ('tcp' in nm['10.0.2.7']):
    list(nm['10.0.2.7']['tcp'].keys()) # get all ports for tcp protocol
nm['10.0.2.7'].all_tcp() # get all ports for tcp protocol (sorted version)
nm['10.0.2.7'].all_udp() # get all ports for udp protocol (sorted version)
nm['10.0.2.7'].all_ip() # get all ports for ip protocol (sorted version)
nm['10.0.2.7'].all_sctp() # get all ports for sctp protocol (sorted version)
if nm['10.0.2.7'].has_tcp(22): # is there any information for port 22/tcp on host 10.0.2.7
    nm['10.0.2.7']['tcp'][22] # get infos about port 22 in tcp on host 10.0.2.7
    nm['10.0.2.7'].tcp(22) # get infos about port 22 in tcp on host 10.0.2.7
    nm['10.0.2.7']['tcp'][22]['state'] # get state of port 22/tcp on host 10.0.2.7 (open
print('----------------------------------------------------')
# print result as CSV
print(nm.csv())
