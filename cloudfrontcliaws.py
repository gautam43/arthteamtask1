import speech_recognition as sr
import os
import getpass
import subprocess
import pyttsx3
def menu():
	print("\t\t\t1.create a key pair")
	print("\t\t\t2.delete a key pair")
	print("\t\t\t3.list of keypairs")
	print("\t\t\t4.create a security group")
	print("\t\t\t5.delete a security group")
	print("\t\t\t6.list of security groups")
	print("\t\t\t7.launch an ec2-instance")
	print("\t\t\t8.create a volume")
	print("\t\t\t9.start an instance")
	print("\t\t\t10.stop an instance")
	print("\t\t\t11.Terminate an instance")
	print("\t\t\t12.Attach the volume")
	print("\t\t\t13.configure webserver")
	print("\t\t\t14.create, format and mounting of partition")
	print("\t\t\t15.show the partition result")
	print("\t\t\t16.download the code from Github")
	print("\t\t\t17.Show the webpage")
	print("\t\t\t18.create a S3 bucket")
	print("\t\t\t19.upload a image in s3 bucket")
	print("\t\t\t20.Create a distribution in cloudfront")
def aws():
	print ('''          
                 @@@@@@@       @@                   @@    @@@@@@  
                @@@@@@@@@@      @@                 @@   @@
                       @@@      @@       @@        @@   @@
                   @@@@@@@       @@     @@ @@     @@      @@@@@@  
                 @@@   @@@       @@    @@   @@    @@      @@@@@@
                @@     @@@        @@  @@     @@  @@             @@
                @@   @@@@@        @@ @@       @@ @@             @@
                 @@@@@  @@@       @@@@        @@@@       @@@@@@@       

                                                    @@@@@@@@@
          @@@@                                              @
           @@@@@                                    @@@@@   @
               @@@@@                              @@@@@@    @
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @
                      @@@@@@@@@@@@@@@@@@@@@@@@@@@


''')
	os.system("color 09")
	print("\t\t\tWelcome to the AWS Assistant")
	print("\t\t\t----------------------------\n")
	pyttsx3.speak("Enter the password to use AWS assistant")
	p=getpass.getpass("Password for verification: ") 
	if p!='gautam':
		pyttsx3.speak("password incorrect")
		exit()
	else:
		pyttsx3.speak("Congrats! Password is correct")
		pyttsx3.speak("Speak your Requirements ... we are listening")
		print("Speak your Requirements ... we are listening ..",end='')
		r=sr.Recognizer()
		print("\n")
		while True:
			menu()
			input()
			with sr.Microphone() as source:
				print("Start saying..")
				audio = r.listen(source)
				print("\t\t\twe got it, plz wait....")

			ch=r.recognize_google(audio)
			print(ch)
			buckName=eval(subprocess.getoutput("aws s3api list-buckets --query Buckets[-1].Name"))

			volId=eval(subprocess.getoutput("aws ec2 describe-volumes  --filters  --query Volumes[-1].VolumeId "))

			InstId=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].InstanceId "))


			if ("create" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
				pyttsx3.speak("Enter the keyname")
				keyname=input("Enter the keyname :")
				os.system("aws ec2 create-key-pair --key-name {} ".format(keyname))
				pyttsx3.speak("Key pair created successfully")

			elif ("delete" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
				pyttsx3.speak("Enter the keyname")
				keyname=input("Enter the keyname :")
				os.system("aws ec2 delete-key-pair --key-name {} ".format(keyname))
				pyttsx3.speak("Key pair deleted successfully")

			elif ("list" in ch) and ("keypair" in ch or ("key" in ch and "pair" in ch) ):
				os.system("aws ec2 describe-key-pairs")

			elif ("security" in ch) and ("group" in ch) and ("create" in ch):
				pyttsx3.speak("Enter the security group name")	
				secgrp=input("Enter the security group name :")
				#desc=created security grp with AWS-CLI
				os.system("aws ec2 create-security-group --description security --group-name {} ".format(secgrp) )
				pyttsx3.speak("security group created successfully")

			elif ("security" in ch) and ("group" in ch) and ("delete" in ch):
				pyttsx3.speak("Enter the security group name")	
				secgrp=input("Enter the security group name :")
				os.system("aws ec2 delete-security-group --group-name {} ".format(secgrp) )
				pyttsx3.speak("security group deleted successfully")

			elif ("list" in ch) and ("security" in ch) and ("groups" in ch):
				os.system("aws ec2 describe-security-groups")

			elif ("launch" in ch) and ("instance" in ch):
				os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name hadoopslave --security-group-ids sg-00821ef2e9cf219fe --subnet-id subnet-933930fb --count 1 ")
				pyttsx3.speak("Instance launch successfully")
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))

			elif ("create" in ch) and ("volume" in ch):
				os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 1")
				pyttsx3.speak("volume created successfully")

			elif ("start" in ch) and ("instance" in ch):
				os.system("aws ec2 start-instances --instance-ids {}".format(InstId) )
				pyttsx3.speak("Instance started successfully")

			elif ("stop" in ch) and ("instance" in ch):
				os.system("aws ec2 stop-instances --instance-ids {}".format(InstId) )
				pyttsx3.speak("Instance stopped successfully")

			elif ("terminate" in ch) and ("instance" in ch):
				os.system("aws ec2 terminate-instances --instance-ids {}".format(InstId) )
				pyttsx3.speak("Instance terminated successfully")

			elif ("attach" in ch) and ("volume" in ch):
				os.system("aws ec2 attach-volume --volume-id {} --device /dev/sdf --instance-id {}".format(volId,InstId) )
				pyttsx3.speak("volume attached successfully")

			elif ("thanks" in ch) and ("assistant" in ch) or ("quit" in ch):
				pyttsx3.speak("Welcome Gautam call me Whenever you want")

			elif ("configure" in ch) and (("webserver" in ch) or (("web" in ch) and ("server" in ch))):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo yum install httpd -y".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo systemctl start httpd".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo systemctl status httpd".format(instIP))
				pyttsx3.speak("webserver configure successfully")		

			elif (("create" in ch) and ("format" in ch)) or ("Mount" in ch) and ("partition" in ch):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo fdisk /dev/xvdf".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo mkfs.ext4 /dev/xvdf1".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo mount /dev/xvdf1 /var/www/html".format(instIP))
				pyttsx3.speak("successfully completed partition setup")

			elif ("show" in ch) and ("partition" in ch) and ("result" in ch):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo fdisk -l".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo df -h".format(instIP))
				pyttsx3.speak("result showed successfully")

			elif ("download" in ch) and ("code" in ch) and ("GitHub" in ch):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo yum install git -y".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo rm -rf /var/www/html/*".format(instIP))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{} sudo git clone https://github.com/gautam43/cloudfront.git /var/www/html/.".format(instIP))
				pyttsx3.speak("Code downloaded successfully")

			elif ("show" in ch) and (("webpage" in ch) or (("web" in ch) and ("page" in ch))):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("chrome.exe {}/web.html".format(instIP))
				pyttsx3.speak("webpage opened successfully")

			elif ("create" in ch) and ("S3" in ch) and ("bucket" in ch):
				pyttsx3.speak("Please Enter the bucket name")
				buckName=input("Please Enter the bucket name:")
				os.system("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1".format(buckName))
				pyttsx3.speak("Bucket created successfully")

			elif ("upload" in ch) and ("image" in ch):
				os.system("aws s3 sync C:\\Users\\user\\Pictures\\cloud s3://{}".format(buckName))
				pyttsx3.speak("Image uploaded successfully")

			elif ("create" in ch) and ("distribution" in ch) and ("cloudfront" in ch):
				os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(buckName))
				pyttsx3.speak("Distribution created successfully")

			elif ("let's" in ch) and ("copy" in ch) and ("path" in ch):
				instIP=eval(subprocess.getoutput("aws ec2 describe-instances  --filters  --query Reservations[-4].Instances[0].PublicIpAddress"))
				os.system("ssh -i C:\\Users\\user\\Downloads\\hadoopslave.pem ec2-user@{}".format(instIP))
			inp=input("Press any key to continue")
			os.system("cls")


