import os
import subprocess
import pyttsx3 as ts
#import FileStorage as fs
import webbrowser
def install_hadoop():
	sh = open("new_script.sh",'w')
	sh.write(f'''#!/bin/bash
	
	sudo yum install -y http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm
	sudo yum install wget
	sudo wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm
	sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force
			''')
	sh.close()
def file_creation():
	
	name = input("Enter directory name to be used as namenode{ e.g:- /dir }: ")
	fi = open("core-site.xml",'w')
	fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>hdfs://0.0.0.0:9001</value></property></configuration>')
	fi.close()
	fd = open("hdfs-site.xml", "w")
	fd.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.data.dir</name><value>{name}</value></property></configuration>')
	fd.close()
	sh = open("en.sh",'w')
	sh.write(f'''#!/bin/bash
			sudo mkdir {name}
			sudo mv core-site.xml /etc/hadoop/
			sudo mv hdfs-site.xml /etc/hadoop/
			sudo hadoop namenode - format
			sudo hadoop-daemon.sh start namenode
			sudo hadoop dfsadmin -report
			jps
			''')
	sh.close()
def namenode_creation():
	ip1 = input("Enter the IP of your master node : ")
	name = input("Enter directory to share as datanode { e.g:- /dir } : ")
	fi = open("core-site.xml",'w')
	fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>{ip1}:9001</value></property></configuration>')
	fi.close()
	fd = open("hdfs-site.xml", "w")
	fd.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.data.dir</name><value>{name}</value></property></configuration>')
	fd.close()
	sh = open("en.sh",'w')
	sh.write(f'''#!/bin/bash
			sudo mkdir {name}
			sudo mv core-site.xml /etc/hadoop/
			sudo mv hdfs-site.xml /etc/hadoop/
			sudo hadoop datanode - format
			sudo hadoop-daemon.sh start datanode
			jps
			''')
	sh.close()
def client_creation():
	ip = input("Enter the IP of your master : ")
	fi = open("core-site.xml",'w')
	fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>{ip}:9001</value></property></configuration>')
	fi.close()
def icon():
	os.system("tput setaf 4")
	print('''
 __                             
'. \                                    
 '- \                                    @@       @@     @@@@@     @@@@@@@           @@@@@           @@@@@       @@@@@@@@
  / /_         .---.                     @@       @@    @@   @@    @@   @@@        @@     @@       @@     @@    @@      @@
 / | \\,.\/--.//    )                     @@       @@   @@     @@   @@    @@@      @@       @@     @@       @@   @@      @@
 |  \//        )/  /                     @@       @@  @@    @ @@@  @@     @@@    @@         @@   @@         @@  @@      @@
  \  ' ^ ^    /    )____.----..  6       @@@@@@@@@@@  @@   @ @ @@  @@      @@@   @@         @@   @@         @@  @@     @@
   '.____.    .___/            \._)      @@       @@  @@  @ @  @@  @@      @@@   @@         @@   @@         @@  @@   @@
      .\/.                      )        @@       @@  @@ @ @   @@  @@      @@@   @@         @@   @@         @@  @@@@@
       '\                       /        @@       @@  @@@ @    @@  @@     @@@     @@       @@     @@       @@   @@
       _/ \/    ).        )    (         @@       @@  @@ @     @@  @@    @@@       @@     @@       @@     @@    @@
      /#  .!    |        /\    /         @@       @@  @@@      @@  @@@@@@@           @@@@@           @@@@@      @@
      \  C// #  /'-----''/ #  / 
   .   'C/ |    |    |   |    |     ,
   \), .. .'OOO-'. ..'OOO'OOO-'. ..\(,





''')
	os.system("tput setaf 2")
while(True):
	os.system('clear')
	icon()
	os.system("tput setaf 2")
	print("Press 1 : Hadoop as a Master \nPress 2 : Hadoop as a Slave \nPress 3 : HAdoop as a Client \nPress 4 for opening a webpage of Hadoop Master \n")
	print("Press 5 for Exit")
	ts.speak("Welcome to Hadoop Cluster .")
	ts.speak("Enter your choice below")
	ch = int(input())
	if(ch == 1):
		os.system('clear')
		icon()
		print("Press 1 : Create a namenode.\nPress 2 : see the report \nPress 3 : get the status of safemode\n\nPress 4 : go back.")
		op=int(input())
		if(op==1):
			os.system('clear')
			icon()
			print("Press 1 : Use local system.  \nPress 2 : Use remote system\n\nPress 3 : go back.")
			in1 = int(input())
			if(in1 ==1):
				print("using my system as Master or Data node")
				install_hadoop()
				os.system("source ./new_script.sh")
				file_creation()
			elif(in1 ==2):
				ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
				path = input("Enter your path to ec2 key file : ")
				checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
				if(checker == "n"):
					install_hadoop()
					os.system(f"scp -i {path} new_script.sh  {ec2_user}:~/")
					os.system(f"ssh -i {path} {ec2_user} source ./new_script.sh")
					print("Hadoop is installed")
				else:
					print("Thank you for installing")
				file_creation()
				os.system(f"scp -i {path} core-site.xml {ec2_user}:~/")
				os.system(f"scp -i {path} hdfs-site.xml {ec2_user}:~/")
				os.system(f"scp -i {path} en.sh {ec2_user}:~/")
				os.system(f"ssh -i {path} {ec2_user} sudo yum install -y net-tools")
				os.system(f"ssh -i {path} {ec2_user} source ./en.sh")
			elif (in1==3):
				continue
			else:
				print("Option not exist")
		elif(op==2):
			os.system("hadoop dfsadmin -report")
		elif(op==3):
			os.system("hadoop dfsadmin -safemode get")
		elif (op==4):
			continue
		else:
			print("Invalid option.")
	elif(ch == 2):
		os.system('clear')
		icon()
		print("Press 1 : Create a Datanode.\nPress 2 : get status of datanode.\n\nPress 3 : go back.")
		op=int(input())
		if(op==1):
			os.system('clear')
			icon()
			print("Press 1 : Use local system as DataNode \nPress 2 : Use remote system\n\nPress 3 : go back.")
			in1 = int(input())
			if(in1==1):
				namenode_creation()
				os.system("source ./em.sh")
			elif(in1==2):
				ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
				path = input("Enter your path to ec2 key file : ")
				checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
				if(checker == "n"):
					install_hadoop()
					os.system(f"scp -i {path} new_script.sh  {ec2_user}:~/")
					os.system(f"ssh -i {path} {ec2_user} source ./new_script.sh")
				else:
					print("Thank you for installing")
				namenode_creation()
				os.system(f"scp -i {path} core-site.xml {ec2_user}:~/")
				os.system(f"scp -i {path} hdfs-site.xml {ec2_user}:~/")
				os.system(f"scp -i {path} em.sh {ec2_user}:~/")
				os.system(f"ssh -i {path} {ec2_user} ./em.sh")
			elif (in1==3):
				continue
			else:
				print("Invalid option.")
		elif(op==2):
			os.system("jps")
		elif(op==3):
			continue
		else:
			print("Invalid option.")
	elif(ch==3):
		os.system('clear')
		icon()
		print("Press 1 : Connect to master.\nPress2 : Upload file to master.\nPress 3 : List files.\nPress 4 : Read a file\nPress 5 : Remove a file\n\nPress 6 : go back.")
		op=int(input())
		if(op==1):
			print("Press 1 to use your local system as a client\n")
			print("Press 2 to use EC2 instance\n\nPress 3 : go back.")
			in1 = int(input())
			if(in1==1):
				client_creation()
				os.system(f"sudo mv core-site.xml /etc/hadoop/")
			elif(in1 == 2):
				ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
				path = input("Enter your path to ec2 key file : ")
				checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
				if(checker == "n"):
					install_hadoop()
					os.system(f"scp -i {path} new_script.sh  {ec2_user}:~/")
					os.system(f"ssh -i {path} {ec2_user} source ./new_script.sh")
				else:
					print("Thank you for installing")
				client_creation()
				os.system(f"scp -i {path} core-site.xml {ec2_user}:~/")
				os.system(f"ssh -i {path} {ec2_user} sudo mv core-site.xml /etc/hadoop/")
			elif(in1==3):
				continue
			else:
				print("Invalid option.")
		if(op==2):
			path=input("Input file name with path { e.g:- /dir/file.txt } : ")
			os.system("sudo hadoop fs -put {path} /")
		if(op==3):
			os.system("sudo hadoop fs -ls /")
		if(op==4):
			path=input("Input file name with path to read { e.g:- /dir/file.txt } : ")
			os.system("sudo hadoop fs -cat {path}")
		if(op==5):
			path=input("Input file name with path to remove { e.g:- /dir/file.txt } : ")
			os.system("sudo hadoop fs -rm {path} ")
		elif (op==6):
			continue
		else:
			print("Invalid option.")
	elif(ch==4):
		os.system('clear')
		icon()
		ip = input("Enter your Master IP : ")
		webbrowser.open(f"{ip}:50010")
	elif (ch==5):
		break
	else:
		print("Invalid input")
	os.system("tput setaf 3")
	a=input("Press any key to continue...")


