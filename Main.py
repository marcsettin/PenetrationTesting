#!/usr/bin/python3
import socket, sys, subprocess

# Clear the screen
#subprocess.call('clear', shell=True)

try:
    # Take input
    def print_menu():       
        print ("\n" + 14 * "-" , "Penetration Testing Software" , 15 * "-")
        print (27 * "-" , "MENU" , 27 * "-")
        print ("1. Local Host")
        print ("2. Remote Host")
        print ("3. Ping Sweep")
        print ("4. Exit (Ctrl+C)")
        print (60 * "-")
    loop = True
    
    while loop:         
        print_menu()    
        choice = input("Enter your choice [1-3]: ")
         
        if choice == "1":     
            print ("Local Host")
            hostName= socket.gethostname()
            hostIP  = socket.gethostbyname(hostName)
            loop = False
        elif choice == "2":
            print ("Remote Host")
            hostName = input("Enter a remote host to scan: ")
            hostIP  = socket.gethostbyname(hostName)
            loop = False
        elif choice == "3":
            exec(open("./PingSweeper.py").read(), globals(), globals())        
            if (userInput != None):
                hostName = userInput
                hostIP  = socket.gethostbyname(hostName)
                loop = False
        elif choice == "4":
            print ("Exit")
            print ("Closing Main.")
            sys.exit()
   
    exec(open("./PortScanner.py").read())
    exec(open("./PasswordCracker.py").read())
        
    
except KeyboardInterrupt:
    print ("\nCtrl+C pressed. Closing Main.")
    sys.exit()

except socket.gaierror as sg:
    print ("\n" + str(sg))
    print ("\nInvalid hostname. Closing Main.")
    sys.exit()

except socket.error as se:
    print ("\n" + str(se))
    print ("\nError. Couldn't connect to server. Closing Main.")
    sys.exit()

except NameError as ne:
     print ("\n" + str(ne))
     print ("\nName Error. Closing Main.")
     sys.exit()
     
except ValueError as ve:
     print ("\n" + str(ve))
     print ("\nValue Error. Closing Menu.")
     sys.exit()
	
	
