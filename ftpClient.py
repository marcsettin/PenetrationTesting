#!/usr/bin/python3
import ftplib, linecache, sys, time

def login(target,user,passw):
    try:
        ftp=ftplib.FTP(target)
        ftp.login(user,passw)
        print('\n')
        print('CURRENT DIRECTORY:')
        data = []
        ftp.dir(data.append)
        for line in data:
            print("-", line)
    except Exception as e:
        print(e)
        
def process(ftp):
    loop = True
    while loop:
        print ('\n')
        print ("FTP CLIENT -- ENTER 'help' FOR COMMANDS")
        command = input('Enter a command: ')
        if command=='ls':
            print ('\n')
            print (ftp.sendcmd('PWD'))
            print ('CURRENT DIRECTORY: '+ftp.pwd())
            data = []
            ftp.dir(data.append)
            for line in data:
                print ("-", line)           
        elif command=='q':
            loop = False
            

host=target
username=user
passw=password
login(host,user,passw)
process(ftp)
