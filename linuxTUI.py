import os,getpass
import subprocess
import pyttsx3
def linux():
        
    os.system("color 01")
    print('''
        .----------------.  .----------------.  .-----------------. .----------------.  .----------------.
       | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
       | |   _____      | || |     _____    | || | ____  _____  | || | _____  _____ | || |  ____  ____  | |
       | |  |_   _|     | || |    |_   _|   | || ||_   \|_   _| | || ||_   _||_   _|| || | |_  _||_  _| | |
       | |    | |       | || |      | |     | || |  |   \ | |   | || |  | |    | |  | || |   \ \  / /   | |
       | |    | |   _   | || |      | |     | || |  | |\ \| |   | || |  | '    ' |  | || |    > `' <    | |
       | |   _| |__/ |  | || |     _| |_    | || | _| |_\   |_  | || |   \ `--' /   | || |  _/ /'`\ \_  | |
       | |  |________|  | || |    |_____|   | || ||_____|\____| | || |    `.__.'    | || | |____||____| | |
       | |              | || |              | || |              | || |              | || |              | |
       | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

        ''')

    print("\t\t\t Hi welcome to my TUI for some small tasks")
    #os.system("color 07")

    print("\t\t\t-----------------------------------------")
    passwd = getpass.getpass("Enter ur password: ")
    apass = "abhay"
    if passwd != apass:
        print("authorization incorrect")
        pyttsx3.speak("authorization incorrect")
        exit()

    pyttsx3.speak("In which machine you want to use local/remote: ")    
    print("which machine you want to use local/remote: ",end="")
    location = input()
    print(location)
    if location == "remote":
        remoteIp = input("Enter ur Ip: ")
        user_name=input("Enter the username:")
    while True:
        os.system("color 04")
        print("\t\t .--,\t    .--,\n\t\t( (  \.---./  ) )\n\t\t '.__/o   o\__.'\n\t\t    {=  ^  =}\n\t\t     >  -  <\n      ___________.\"\"`-------`\"\".____________\n     /                                      \ \n     \ o   Press 1: to see memory usage   o / \n     /     Press 2: Check the Software      \ \n     \     Press 3: to conf Webserver       /   \n     /     Press 4: to create user          \ \n     \     Press 5: to install a package    / \n     /     Press 6: to check about server?  \ \n     \     Press 7:to check running process / \n     /     Press 8: to see the packets      \ \n     \     Press 9: to exit \t\t    / \n     /______________________________________\ \n\t\t   ___)( )(___ \n \t\t  (((__) (__)))")
        os.system("color 02")
        pyttsx3.speak("Enter your choice")
        print("Enter your choice: " , end="")
        ch=input()
        print(ch)
        os.system("color 07")

        if location == "local":
            if int(ch) == 1:
                os.system("free -m")
            elif int(ch) == 2:
                pyttsx3.speak("Enter the software name")
                n=input("*Enter the software name:")
                os.system("rpm -q {}".format(n))
            elif int(ch) == 3:
                os.system("yum install httpd".format(user_name,remoteIP))
                print("Enter the webpage name:",end='..')
                webpage_name=input()
                print("Enter the code or data u want to put in webpage:")
                os.system("cat > /var/www/html/{1}.html".format(remoteIP,webpage_name,user_name))
                os.system("systemctl start httpd".format(user_name,remoteIP))
            elif int(ch) == 4:
                pyttsx3.speak("Please provide name of the user:")
                print("Please provide name of the user: ",end="")
                create_user = input()
                os.system("sudo useradd {0}".format(create_user))   ##this is called place holder  or interpolation
            elif int(ch) == 5:
                print("Enter the name of package : ", end="")
                pack_name = input()
                os.system("yum install {0}".format(pack_name))
            elif int(ch) == 6:
                os.system("systemctl status httpd")
            elif int(ch) == 7:
                os.system("ps -aux")
            elif int(ch) == 8:
                os.system("tcpdump -i enp0s3 -n")
            elif int(ch) == 9:
                exit()

                
            else:
                print("option not found")
            os.system(input("Press Enter to continue........"))
            os.system("cls")
        elif location == "remote":
            if int(ch) == 1:
                os.system("ssh {1}@{0} free -m".format(remoteIp,user_name))
            elif int(ch) == 2:
                pyttsx3.speak("Enter the software name")
                n=input("*Enter the software name:")
                os.system("ssh {1}@{0} rpm -q {2}".format(remoteIp,user_name,n))
            elif int(ch) == 3:
                os.system("ssh {}@{} yum install httpd".format(user_name,remoteIp))
                os.system("ssh {}@{} systemctl start httpd".format(user_name,remoteIp))
            elif int(ch) == 4:
                pyttsx3.speak("can you give me name for user:")
                print("can you give me name for user: ",end="")
                create_user = input()
                os.system("ssh {2}@{0} sudo useradd {1}".format(remoteIp,create_user,user_name))   ##this is called place holder  or interpolation
            elif int(ch) == 5:
                pyttsx3.speak("Enter the name of package")
                pack_name = input("Enter the name of package :")
                os.system("ssh {2}@{0} sudo dnf install {1} -y".format(remoteIp,pack_name,user_name))
            elif int(ch) == 6:
                os.system("ssh {1}@{0} systemctl status httpd".format(remoteIp,user_name))
            elif int(ch) == 7:
                os.system("ssh {}@{} ps -aux".format(user_name,remoteIp))
            elif int(ch) == 8:
                os.system("ssh {}@{} tcpdump -i enp0s3 -n".format(user_name,remoteIp))
            elif int(ch) == 9:
                exit()
            else:
                print("option not found")
            pyttsx3.speak("Press any key to continue")
            cl=input()
            os.system("cls")
                
        else:
            print("sorry wrong input")
            
