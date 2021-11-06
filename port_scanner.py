#!/usr/bin/env python3

import argparse
import socket
import pyfiglet
import sys
from datetime import datetime

display = pyfiglet.figlet_format("Port  Scanner")
print(display)

parser = argparse.ArgumentParser(description='port scanner')
parser.add_argument('-t',  '--target', type=str, help='target ip address to scan')
#parser.add_argument('-o', '--output', help=" Output the results in a file", \
#			action='store_true') 
args = parser.parse_args()


print("-" * 50)
print("Scanning Target: ", args.target )
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

for port in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    connection = s.connect_ex((args.target, port))
    if connection == 0:
        print("Port ", port , "is open" ) 
    if args.output:
        if connection ==0:
            f=open("scan_results.txt", 'a')
            f.write("port {} open ".format(port)+'\n')

    s.close()

