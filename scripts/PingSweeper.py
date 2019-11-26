#!/usr/bin/python3
import os, subprocess, ipaddress, netifaces, netaddr, threading, time, json, sys
from datetime import datetime
from queue import Queue 
 

def print_menu():
    
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("ls")
    
    print ("\n" + 15 * "-" , "Penetration Testing Software" , 15 * "-")
    print (22 * "-" , "PingSweeper.py" , 22 * "-")
    print ("1. Local Network")
    print ("2. Remote Network")
    print ("3. Back to Main")
    print ("4. Exit or enter 'Ctrl+C'")
    print (60 * "-")

def check_format(netAddr):        
                
        x = netAddr.split('.')
        
        if (len(x) != 4):
            print("\n")
            print ("Address must contain 3 decimals. Restarting PingSweeper.")
            print("Format ex: 0.0.0.")
            print("\n")
            
            time.sleep(5)
            check = False
            
        else:
            N1, N2, N3, N4 = netAddr.split('.')
        
            if ((N1.isdigit() or N2.isdigit() or N3.isdigit()) == False):
                print("\n")
                print ("Illegal character in address. Restarting PingSweeper")
                print("Format ex: 192.168.1.")
                print("\n")
                time.sleep(5)
                check = False
                    
            elif (N4 != ''):
                print("\n")
                print ("Host address not empty. Restarting PingSweeper")
                print("Format ex: 192.168.1.")
                print("\n")
                time.sleep(5)
                check = False
                        
            elif ((int(N1) and int(N2) and int(N3)) >= 255):
                print("\n")
                print ("Exceeded max address. Restarting PingSweeper")
                print("Max address: 255.255.255.255")
                print("Format ex: 192.168.1.")
                print("\n")
                time.sleep(5)
                check = False           
            
            else:
                check = True
            
        return check

def cidr_range(netAddr):       
        
    loop = True
    
    while loop:
    
        print (22 * "-" , "PingSweeper.py" , 22 * "-")
        print ("1. Full Scan")
        print ("2. Scan Range")
        print ("3. Back")
        print (60 * "-")
    
        choice2 = input("Enter your choice [1-3]: ")
              
        if choice2 == "1":
            CIDR = '0/24'
            offset = 0
            loop = False 
        
        elif choice2 == "2":                  
            print("\nType 'b' or 'back' to go back")
            print ("\nRange: 1-255")           
            
            shostAddr = input("Starting host address (ex: 1): ")
            
            if shostAddr != 'b' and shostAddr != 'back':               
                ehostAddr = input("Ending host address (ex: 255): ")                  
                
                if hostAddr != 'b' and ehostAddr != 'back':
                    if ((len(shostAddr) and len(ehostAddr)) <= 3) and ((shostAddr.isdigit() and ehostAddr.isdigit()) == True) and (int(shostAddr) >= 0) and (int(ehostAddr) <= 255) and (int(shostAddr) < int(ehostAddr)):            
                        offset = int(shostAddr)-1 
                        shostAddr = str(offset)                        
                        startIP = netAddr + shostAddr            
                        endIP = netAddr + ehostAddr
                        CIDR = netaddr.iprange_to_cidrs(startIP, endIP)
                        loop = False 
                
                    else:
                        print("\n")
                        print ("Illegal Format. Please try again")
                        print("\n")
                                 
        elif choice2 == "3":
            CIDR = -1
            loop = False                 
        
    return CIDR, offset
      
def ping(allHosts, ip, info, output):                           
                
        collection = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(allHosts[ip])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
        
        
        try:
            
            if "Reply" in collection.decode('utf-8'):
                output[ip] = 'Online'
            
            elif "Destination host unreachable" in collection.decode('utf-8'):
                output[ip] = 'Offline'       
            
            elif "Request timed out" in collection.decode('utf-8'):
                output[ip] = 'Offline'                    
        
        except:    
                output[ip] = 'Offline'

               

def get_hosts(netAddr, CIDR, i, io, offset):                                 
                   
    if io == 0:
        ipNet = ipaddress.ip_network(netAddr+CIDR)
        
    else:
        ipNet = ipaddress.ip_network(CIDR[i])
 
    # Read all hosts on network
    allHosts = list(ipNet.hosts())

    # Configure subprocess
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
        
    threads = []       
    output = {}
    liveHosts = list()
    
    # Spawning threads to ping addresses
    for i in range(len(allHosts)):
        t = threading.Thread(target=ping, args=(allHosts, i, info, output))
        threads.append(t)

    # Starting threads
    for i in range(len(allHosts)):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(len(allHosts)):
        threads[i].join()

    # Printing live hosts from small to large          
    for i in range(len(allHosts)):                
        if output[i] == 'Online':
            liveHosts.append(netAddr + str(offset+1))                
            
            if (len(str(offset+1)) == 1):
                print(netAddr + str(offset+1) + ':     ' + output[i])
            
            elif (len(str(offset+1)) == 2):
                print(netAddr + str(offset+1) + ':    ' + output[i])
            
            elif (len(str(offset+1)) == 3):
                print(netAddr + str(offset+1) + ':   ' + output[i])
            
            offset = 1 + offset
                
        else:
            offset = 1 + offset
              
    return liveHosts, offset
    
                
def check_hosts(liveHosts, netAddr):
    
    loop = True
    
    while loop:
        
        if (len(liveHosts) != 0):                
            print("\nType 'b' or 'back' to go back")
            host = input("Select online host (ex: 12): ")
            
            if  host == 'back' or host =='b':
                target = None
                loop = False
            
            else:
                target = netAddr + host
                live_set = set(liveHosts)
                
                if (target in live_set):
                    print ("\nValid Host Selected")
                    print ("Target: ", target, "\n")
                    
                    loop = False
                
                else:
                    print ("\nInvalid or Offline Host Selected")
                    print ("Please try again or enter Ctrl+C to exit.")                
        
        else:
            print ("\n\nNo online hosts found. Retunring to Main.\n")
            
            target = None
            loop = False
    
    return target

def pingsweep(netAddr, CIDR, offset):                
    
    # Print
    netAddrLength = 25-len(str(netAddr))
    print ("*" * 60)
    print ("* PingSweeper.py", " " * 42 + "*")
    print ("* Please wait, scanning network: ", netAddr + " " * netAddrLength + "*")
    print ("*" * 60)
    print ("\n")       
    
    # Start time 
    t0 = datetime.now()
    
    liveHosts = list()
    temp = list()
    curOffset = offset
        
    if type(CIDR) == list:                                      
        for i in range(len(CIDR)):                                   
            temp, offset = get_hosts(netAddr, CIDR, i, 1, offset)                       
            
            if i <= 2:
                set = i
            offset = set + offset
            
            for j in range(len(temp)):                
                liveHosts.insert(j, temp[j])               
    
    else:        
        liveHosts, length = get_hosts(netAddr, CIDR, 0, 0, 0)
                
    # End time
    t1 = datetime.now()

    # Calculate runtime
    total =  t1 - t0

    # Generate Report
    print ("\n\nScanning Completed in: ", total)
    
    with open('report.txt', 'a') as f:
        f.write("\nPingSweeper.py\n")
        f.write("-Online Users-\n")
        for item in liveHosts:
            f.write("%s\n" % item)
                    
    target = check_hosts(liveHosts, netAddr)
    
    return target

def run():                              
    
    loop = True    
    
    while loop:         
        
        print_menu()    
        choice = input("Enter your choice [1-3]: ")
         
        if choice == "1":                 
            print ("\n")
            print ("-Local Network") 
            
            
            # Get default gateway
            gateways = netifaces.gateways()
            netAddr = gateways['default'][netifaces.AF_INET][0]
            netAddr = netAddr[:-1]
            print(netAddr)
            print("\n")
            
            
            if (check_format(netAddr) == True):
            
                CIDR, offset = cidr_range(netAddr)
                
                if CIDR != -1:
                    target = pingsweep(netAddr, CIDR, offset)
                    
                    if target != None:
                        loop = False
          
        elif choice == "2":                                 
            print ("\n")
            print ("-Remote Network")
            print ("\n")
            
            # Prompt the user to input a network address   
            netAddr = input("Enter a network address to scan (ex: 192.168.1.): ")
            print ("\n")                       
            
            if (check_format(netAddr) == True):
            
                CIDR, offset = cidr_range(netAddr)
                
                if CIDR != -1:
                    target = pingsweep(netAddr, CIDR, offset)
                    
                    if target != None:
                        loop = False            
            
        elif choice == "3":            
            print ("\n")
            print ("-Back")
            print ("\n")
            print ("Closing PingSweeper.")
            
            target = None
            loop = False
        
        elif choice == "4":
            print ("\n")
            print ("-Exit")
            print ("\n")
            print("Closing Program.")
            
            sys.exit()
    
    return target  
