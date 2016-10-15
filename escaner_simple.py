#! /usr/bin/python

import nmap
nm = nmap.PortScanner()
resultados = nm.scan('192.168.1.1')
print(nm.csv())
