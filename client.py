import os
import subprocess
import pyttsx3 as ts
#import FileStorage as fs
import webbrowser
def install_hadoop(path):
	path_had = input("Enter the path for the folder where you saved the java and hadoop software : ")
	os.system(f"scp -r -i {path}  {path_had} {ec2_user}:~/")
	os.system(f"scp -i {path} new_script.sh  {ec2_user}:~/")
	os.system(f"ssh -i {path} {ec2_user} ./new_script.sh")
	print("Hadoop is installed")
print("Starting with Hadoop")
print("Below are the few options to get start and create a cluster")
while(True):
	ts.speak("Welcome to Hadoop Cluster Creation. Follow the below steps")
	print("Press 1 for creating a Master or Name node and get the IP \nPress 2 for creating a Slave or Data node \nPress 3 for creating a client \nPress 4 for opening a webpage of Hadoop Master \n")
	print("Press 5 for Exist")
	ts.speak("Enter your choice below")
	ch = int(input())
	if(ch == 1):
		print("Press 1 for using local system as DataNode \nPress 2 for using remote system")
		in1 = int(input())
		if(in1 ==1):
			print("using my system as Master or Data node")
			os.system("ifconfig")
		elif(in1 ==2):
			ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
			path = input("Enter your path to ec2 key file : ")
			checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
			if(checker == "n"):
				install_hadoop(path)
			else:
				print("Thank you for installing")
			name = input("Enter your folder of choice : ")
			os.system('./script.sh')
			fi = open("core-site.xml",'w')
			fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>{ip1}:9001</value></property></configuration>')
			fi.close()
			fd = open("hdfs-site.xml", "w")
			fd.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.data.dir</name><value>{name}</value></property></configuration>')
			fd.close()
			os.system("scp -i {path} core-site.xml {ec2_user}:~/")
			os.system("scp -i {path} hdfs-site.xml {ec2_user}:~/")
			os.system("scp -i {path} en.sh {ec2_user}:~/")
			os.system("ssh -i {path} {ec2_user} rpm -i net-tools&&ifconfig")
			os.system("ssh -i {path} {ec2_user} ./en.sh")
		else:
			print("Option not exist")
	elif(ch == 2):
		ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
		path = input("Enter your path to ec2 key file : ")
		checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
		if(checker == "n"):
			install_hadoop(path)
		else:
			print("Thank you for installing")
		ip1 = input("Enter the IP of your master node : ")
		name = input("Enter your folder of choice : ")
		os.system('./script.sh')
		fi = open("core-site.xml",'w')
		fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>{ip1}:9001</value></property></configuration>')
		fi.close()
		fd = open("hdfs-site.xml", "w")
		fd.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>dfs.data.dir</name><value>{name}</value></property></configuration>')
		fd.close()
		os.system("scp -i {path} core-site.xml {ec2_user}:~/")
		os.system("scp -i {path} hdfs-site.xml {ec2_user}:~/")
		os.system("scp -i {path} em.sh {ec2_user}:~/")
		os.system("ssh -i {path} {ec2_user} ./em.sh")
	elif(ch==3):
		print("Press 1 to use your local system as a client")
		print("Press 2 to use EC2 instance")
		in1 = int(input())
		if(n1 == 1):
			ec2_user = input("Enter your ec2 user name@ip, eg:ec2-user@123.23.45.1 : ")
			path = input("Enter your path to ec2 key file : ")
			checker = input("Java and Hadoop already installed in EC2 (y/n) : ")
			if(checker == "n"):
				install_hadoop()
			else:
				print("Thank you for installing")
		ip = input("Enter the IP of your master : ")
		fi = open("core-site.xml","w")
		fi.write(f'<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="configuration.xsl"?><configuration><property><name>fs.default.name</name><value>{ip}:9001</value></property></configuration>')
		fi.close()
		os.system("scp -i {path} core-site.xml {ec2_user}:~/")
		os.system("scp -i {path} emc.sh {ec2_user}:~/")
		os.system("ssh -i {path} {ec2_user} ./emc.sh")
	elif(ch==4):
		ip = input("Enter your Master IP : ")
		webbrowser.open(f"{ip}:50010")
	else:
		break


