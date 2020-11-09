import os
import subprocess
#import FileStorage as fs
import webbrowser
def hadoop():
	print("Starting with Hadoop")
	print("Below are the few options to get start and create a cluster")
	while(True):
		print("Press 1 for creating a Master or Name node and get the IP \nPress 2 for creating a Slave or Data node \nPress 3 for creating a client \nPress 4 for opening a webpage of Hadoop Master \n")
		print("Press 5 for Exist")
		ch = int(input("Enter your choice"))
		if(ch == 1):
			print("using my system as Master or Data node")
			os.system("ifconfig")
		elif(ch == 2):
			ip1 = input("Enter the IP of your master node")
			name = input("Enter your folder of choice")
			os.system(f"mkdir {name}")
			fi = open("etc/hadoop/core-site.xml",'w')
			fi.write(f"<configuration><property><name>fs.default.name</name><value>{ip1}:9001</value></property></configuration>")
			fi.close()
			fd = open("etc/hadoop/hdfs-site.xml", "w")
			fd.write(f"<configuration><property><name>dfs.data.dir</name><value>{name}</value></property></configuration>")
			fd.close()
			os.system("hadoop datanode -format")
			os.system("hadoop-daemon.sh start datanode")
			os.system("jps")
		elif(ch==3):
			ip = input("Enter the IP of your master")
			fi = open("etc/hadoop/core-site.xml","w")
			fi.write(f"<configuration><property><name>fs.default.name</name><value>{ip}:9001</value></property></configuration>")
			fi.close()
		elif(ch==4):
			ip = input("Enter your Master IP")
			webbrowser.open(f"{ip}:50010")
		else:
			break


