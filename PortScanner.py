#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import time

# Clear the screen
subprocess.call('clear', shell=True)

try:
    # Take input
    def print_menu():       
        print 27 * "-" , "MENU" , 27 * "-"
        print "1. Local Host"
        print "2. Remote Host"
        print "3. Exit (Ctrl+C)"
        print 60 * "-"
    loop = True

    while loop:         
        print_menu()    
        choice = input("Enter your choice [1-3]: ")
         
        if choice==1:     
            print "Local Host"
            hostName= socket.gethostname()
            hostIP  = socket.gethostbyname(hostName)
            loop = False
        elif choice==2:
            print "Remote Host"
            hostName = raw_input("Enter a remote host to scan: ")
            hostIP  = socket.gethostbyname(hostName)
            loop = False
        elif choice==3:
            print "Exit"
            print "Closing port scanner."
            sys.exit()

    # Calculate Box
    hostnameLength = 43-len(str(hostName))
    hostIPLength = 37-len(str(hostIP))
    hostIPLength2 = 28-len(str(hostIP))

    # Print
    print "*" * 60
    print("* Host Name is: " + hostName) + " " * hostnameLength + "*"
    print("* Host IP Address is: " + hostIP) + " " * hostIPLength + "*"
    print "* Scan will automatically stop after 60 seconds." + " " * 11 + "*"
    print "* Please wait, scanning host: ", hostIP + " " * hostIPLength2 + "*"
    print "*" * 60
    
    # Start time
    t0 = datetime.now()

    # Scan all ports between 1 and 1024
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostIP, port))
        if result == 0:
            print "Port {}:".format(port) + " " * (15-len(str(port))) + "open"
        # Show closed
        #else:
            #print "Port {}:".format(port) + " " * (15-len(str(port))) + "closed"
        sock.close()
            
    # End time
    t2 = datetime.now()

    # Calculate runtime
    total =  t2 - t0

    # Generate Report
    print 'Scanning Completed in: ', total

except KeyboardInterrupt:
    print "\nCtrl+C pressed. Closing port scanner."
    sys.exit()

except socket.gaierror:
    print "\nInvalid hostname. Closing port scanner."
    sys.exit()

except socket.error:
    print "\nError. Couldn't connect to server. Closing port scanner."
    sys.exit()

except NameError:
     print "\nName Error. Closing port Scanner."
     sys.exit()


