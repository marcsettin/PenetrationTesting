#!/usr/bin/python3
import sys, os, socket, time, linecache
sys.path.insert(0, 'scripts/')
import PingSweeper, PortScanner, PasswordCracker, ftpClient

if os.name == 'nt':
    os.system("cls")
else:
    os.system("ls")

try:
        
    def print_menu():
        
        print ("\n" + 15 * "-" , "Penetration Testing Software" , 15 * "-")
        print (27 * "-" , "MENU" , 27 * "-")
        print ("1. Local Host")
        print ("2. Remote Host")
        print ("3. Ping Sweep")
        print ("4. Exit (Ctrl+C)")
        print (60 * "-")
        
    def check_format(remote):        
            
        x = remote.split('.')

        if (len(x) != 4):
            print("\n")
            print ("Address must contain 3 decimals. Restarting Main.")
            print("Format ex: 0.0.0.0")
            print("\n")
            
            time.sleep(5)
            check = False
            
        else:
            
            N1, N2, N3, N4 = remote.split('.')

            if ((N1.isdigit() or N2.isdigit() or N3.isdigit() or N4.isdigit()) == False):
                print("\n")
                print ("Illegal character in address. Restarting Main")
                print("Format ex: 192.168.1.1")
                print("\n")
                time.sleep(5)
                check = False                    
                        
            elif ((int(N1) or int(N2) or int(N3) or int(N4)) >= 255):
                print("\n")
                print ("Exceeded max address. Restarting Main")
                print("Max address: 255.255.255.255")
                print("Format ex: 192.168.1.")
                print("\n")
                time.sleep(5)
                check = False           
            
            else:
                check = True
            
        return check       
    
    def tests(hostIP):
        print ("\nVulnerability found attempting Password Cracker.\n")
        time.sleep(5)
        user, password = PasswordCracker.run(hostIP)
        print ("\nPassword cracked opening ftpClient.\n")
        time.sleep(5)
        ftpClient.run(hostIP, user, password)
    
    def main():
               
        loop = True
        
        with open('report.txt', 'w') as f:
            f.write("Penetration Testing Software")
            f.write("\n-Starting Scripts-\n")
        
        while loop:         
            
            print_menu()    
            choice = input("Enter your choice [1-4]: ")
             
            if choice == "1":     
                print ("\n")
                print ("-Local Host")
                print ("\n")
                
                hostName = socket.gethostname()
                hostIP  = socket.gethostbyname(hostName)                
                back = PortScanner.run(hostIP, hostName, 1)                
                if back != True:
                        loop = False
            
            elif choice == "2":
                print ("\n")
                print ("-Remote Host")
                print ("\n")
                
                remote = input("Enter a remote host to scan: ")
                
                if check_format(remote) == True:
                    hostIP  = socket.gethostbyname(remote)
                    back = PortScanner.run(hostIP, hostName, 1)               
                    if back != True:
                        loop = False
            
            elif choice == "3":                
                target = PingSweeper.run()    
                
                if target != None:
                    
                    hostName = target
                    hostIP  = socket.gethostbyname(target)                    
                    back = PortScanner.run(hostIP, hostName, 0)   
                    if back != True:
                        loop = False
            
            elif choice == "4":
                print ("\n")
                print ("-Exit")
                print ("\n")
                print ("Closing Main.")
                
                sys.exit()       
        
        tests(hostIP)
        print("Report Generated to report.txt")
        os.system("type report.txt")
    
    # this means that if this script is executed, then 
    # main() will be executed
    if __name__ == '__main__':
        main()
    
    
except KeyboardInterrupt:
    print("\n")
    print ("Ctrl+C entered. Closing Program.")
    print("\n")
    
    sys.exit()

except socket.gaierror as sg:
    print("\n")
    print (str(sg))
    print ("\nInvalid hostname.")
    print ("\n")
    
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))


except socket.error as se:
    print("\n")
    print (str(se))
    print ("\nError. Couldn't connect to server.")
    print ("\n")
    
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

except NameError as ne:
    print("\n")
    print (str(ne))
    print ("\nName Error.")
    print ("\n")
    
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

     
except ValueError as ve:
    
    print("\n")
    print (str(ve))
    print ("\nValue Error.")
    print("\n")
    
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

            
except Exception as e:
    print("\n")
    print(str(e))
    print ("\n")

    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))    

