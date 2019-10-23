#!/usr/bin/python3
import socket, time, sys
from datetime import datetime

try:
    
    # Start time
    t0 = datetime.now()

    # Scan all ports between 1 and 1024
    for port in range(1,23):
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
