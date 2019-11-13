#!/usr/bin/python3
import socket, time, sys
from datetime import datetime

try:
    
    # Calculate Box
    hostnameLength = 43-len(str(hostName))
    hostIPLength = 37-len(str(hostIP))
    hostIPLength2 = 28-len(str(hostIP))

    # Print
    print ("*" * 60)
    print ("* PortScanner.py", " " * 42 + "*")
    print ("* Host Name is: " + hostName + " " * hostnameLength + "*")
    print ("* Host IP Address is: " + hostIP + " " * hostIPLength + "*")
    print ("* Please wait, scanning host: ", hostIP + " " * hostIPLength2 + "*")
    print ("*" * 60)
        
    # Start time
    t0 = datetime.now()

    # Scan all ports between 1 and 1024
    for port in range(1,3):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostIP, port))
        if result == 0:
            print ("Port {}:".format(port) + " " * (15-len(str(port))) + "open")

        #Show closed
        else:
            print ("Port {}:".format(port) + " " * (15-len(str(port))) + "closed")
        sock.close()
            
    # End time
    t1 = datetime.now()

    # Calculate runtime
    total =  t1 - t0

    # Generate Report
    print ("\n\nScanning Completed in: ", total, "\n")

except KeyboardInterrupt:
    print ("\nCtrl+C pressed. Closing port scanner.")
    sys.exit()
    
except socket.gaierror as sg:
    print ("\n" + str(sg))
    print ("\nInvalid hostname. Closing Main.")
    sys.exit()

except socket.error as se:
    print ("\n" + str(se))
    print ("\nError. Couldn't connect to server. Closing Main.")
    sys.exit()
