#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments. ")
    print("Syntax: python3 port_scanner.py <ip>")

#Add banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,2500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns
        print("Checing port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting pogram.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolvd.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()