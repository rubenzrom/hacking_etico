#! /usr/bin/python

import nmap

nma = nmap.PortScanner()

def callback_result(host, scan_result):
    print '------------------'
    print host, scan_result
  
nma.scan(hosts='192.168.1.0/24', arguments='-sP', callback=callback_result)



