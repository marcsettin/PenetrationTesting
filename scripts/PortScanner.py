#!/usr/bin/python3
import socket, time, sys, threading, os, sys
from datetime import datetime
  
def print_menu(io):
    
    if io == 1:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("ls")
    
    print ("\n" + 15 * "-" , "Penetration Testing Software" , 15 * "-")
    print (22 * "-" , "PortScanner.py" , 22 * "-")
    print ("1. Full Scan(65356)")    
    print ("2. Common Ports")
    print ("3. Back to Main")
    print ("4. Exit or enter 'Ctrl+C'")
    print (60 * "-")

def print_scanner(hostName, hostIP):
    
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

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = 'Closed'



def scan_ports(host_ip, delay, i):

    threads = []
    output = {}
    openPorts = list()

    # Spawning threads to scan ports
    for i in range(i):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(i):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(i):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(i):
        if output[i] == 'Listening':           
            
            openPorts.append('Port ' + str(i))
            
            if (len(str(i)) == 1):
                print('Port ' + str(i) + ':       ' + output[i])
            
            elif (len(str(i)) == 2):
                print('Port ' + str(i) + ':      ' + output[i])
            
            elif (len(str(i)) == 3):
                print('Port ' + str(i) + ':     ' + output[i])
            
            elif (len(str(i)) == 4):
                print('Port ' + str(i) + ':    ' + output[i])
            
            elif (len(str(i)) == 5):
                print('Port ' + str(i) + ':   ' + output[i])
            
    with open('report.txt', 'a') as f:
        f.write("\nPortScanner.py\n")
        f.write("-Open Ports-\n")
        for item in openPorts:
            f.write("%s\n" % item)
    
    # Printing closed ports from small to large
    #for i in range(65356):
        #if output[i] == 'Closed':
            #print(str(i) + ': ' + output[i])


def run(hostIP, hostName, io):

    loop = True    
    
    while loop:         
        
        back = False
        
        print_menu(io)    
        choice = input("Enter your choice [1-3]: ")
         
        if choice == "1":                 
            print ("\n")
            print ("-Full Scan") 
            
            # Start time
            t0 = datetime.now()

            print_scanner(hostIP, hostName)
            scan_ports(hostIP, 0.1, 65356)            
                
            # End time
            t1 = datetime.now()
            
            back = False
            loop = False
            
          
        elif choice == "2":                                 
            print ("\n")
            print ("-Common Ports")
            print ("\n")
            
            # Start time
            t0 = datetime.now()            

            print_scanner(hostIP, hostName)
            scan_ports(hostIP, 0.1, 8080)
                
            # End time
            t1 = datetime.now()
            
            back = False
            loop = False
            
        elif choice == "3":            
            print ("\n")
            print ("-Back")
            print ("\n")
            print ("Closing PortScanner.")
            
            back = True
            loop = False
        
        elif choice == "4":
            print ("\n")
            print ("-Exit")
            print ("\n")
            print("Closing Program.")
            
            sys.exit()
        
        return back 
            
    # Calculate runtime
    total =  t1 - t0

    # Generate Report
    print ("\n\nScanning Completed in: ", total, "\n")  
        
