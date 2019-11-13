#!/usr/bin/python3
import subprocess, ipaddress
from datetime import datetime

# Prompt the user to input a network address
netAddr = input("Enter a network address to scan (ex.192.168.1): ")
CIDR = netAddr + '.64/31'

# Print
netAddrLength = 25-len(str(netAddr))
print ("*" * 60)
print ("* PingSweeper.py", " " * 42 + "*") 
print ("* Please wait, scanning address: ", netAddr + " " * netAddrLength + "*")
print ("*" * 60)
print ("\n")

# Start time
t0 = datetime.now()

# Create network
ipNet = ipaddress.ip_network(CIDR)

# Read all hosts on network
allHosts = list(ipNet.hosts())

# Collect live hosts on network
liveHosts = list()

# Configure subprocess
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# Run the ping command with subprocess
for i in range(len(allHosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(allHosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    if "Destination host unreachable" in output.decode('utf-8'):
        print(str(allHosts[i]), "is Offline")
    elif "Request timed out" in output.decode('utf-8'):
        print(str(allHosts[i]), "is Offline")
    else:
        print(str(allHosts[i]), "is Online")
        liveHosts.append((str(allHosts[i])))

# End time
t1 = datetime.now()

# Calculate runtime
total =  t1 - t0

# Generate Report
print ("\n\nScanning Completed in: ", total)
        
i = 0
while (i != 1):
    if (len(liveHosts) != 0):
        userInput = input("\nSelect online host: ")
        live_set = set(liveHosts)
        if (userInput in live_set):
            print ("\nValid Host Selected")
            print ("Target: ", userInput, "\n")
            i = 1
        else:
            print ("\nInvalid or Offline Host Selected")
            print ("Please try again or enter Ctrl+C to exit.")
        
    else:
        print ("\n\nNo online hosts found. Retunring to Main.\n")
        userInput = None
        i = 1
    
    