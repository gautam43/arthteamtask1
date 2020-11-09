
import os
import speech_recognition as sr
import pyttsx3

def info():
	os.system("color 02")
	print("\t-> Start the docker Tool")
	
	print("\t->Work on Images in Docker")
	
	print("\t->Work on Containers in Docker")
	
	print("\t->Work on Network in Docker")
	
	print("\t->Work on Volume in Docker")
	
	print("\t->Install the Docker-compose")
	
	print("\t->Launch the Wordpress site")
	
	print("\t->Close the Wordpress site")
		
	print("\t->exit the program")
	
def docker():
	print('''	
		   @@                                  @@@@@
		   @@                 @@@@@@@        @@     @@        @@@@@  @@        @@@@@@@@   @@@@@
		@@@@@     0          @@@@@@@@@     @@@       @@@     @@@     @@    @@  @@ @@@@@  @@   @@  
	  @@@@@@@@@@@@    00000 ___  @@@     @@@   @@@       @@@    @@       @@   @@   @@        @@    @@
	  @@@@@@@@@@@@    0000000000 @@@      @@@  @@@       @@@   @@@       @@  @@    @@        @@   @@
	00000000000000000000^00o^    @@@      @@@  @@@       @@@   @@@       @@ @@     @@@@@     @@ @@
	0000000000000000000          @@@      @@@  @@@       @@@   @@@       @ @@      @@        @@@@
	 000000 (@) 000000           @@@     @@@    @@       @@@    @@       @@ @@     @@        @@  @@
	  00000000000000             @@@@@@@@@       @@     @@       @@@     @@  @@    @@ @@@@   @@   @@
	    0000000000                @@@@@@@          @@@@@          @@@@@  @@   @@   @@@@@@@   @@    @@
	       ^^^^
''')
	
	os.system("color  01")
	pyttsx3.speak("Welcome to Smart TUI of docker")
	print("\t\t\tWelcome to Smart TUI of docker")
	#os.system("tput setaf 7")
	print("\t\t\t------------------------------")
	#os.system("tput setaf 4")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		pyttsx3.speak("Excited to know about Docker!! say yes or no..")
		print("\t\tExcited to know about Docker!! say yes or no..")
		audio = r.listen(source)
		print("\t\t\twe got it, plz wait....")

	ch=r.recognize_google(audio)
	
	#os.system("tput setaf 7")
	#os.system("tput setab 0")
	if ("yes" in ch) or ("Yes" in ch):
		pyttsx3.speak("Docker is basically a container engine, which uses the Linux Kernel features, like namespaces, and control groups to create containers on top of an operating system and automates application deployment on the container.")
		
	elif ("no" in ch) or ("No" in ch):
		pyttsx3.speak("okay, let's move on")
	input()
	pyttsx3.speak("In which system u want to run the program local or remote")
	with sr.Microphone() as source:
		print("\t\tIn which system u want to run the program local or remote..")
		audio = r.listen(source)
		print("\t\t\twe got it, plz wait....")

	voice=r.recognize_google(audio)
	
	if ("local" in voice) or ("Local" in voice):
		while True:
			info()
			input()
			with sr.Microphone() as source:
				print("Speak your choice ")
				audio = r.listen(source)
				print("\t\t\twe got it, plz wait....")

			choice=r.recognize_google(audio)
			

			if ("start" in choice) and ("docker" in choice):
				os.system("systemctl start docker")
				os.system("tput setaf 5")
				print("Also want to see the status of docker press y/n",end="...")
				os.system("tput setaf 7")
				status_input=input()
				if status_input =='y'or status_input =='Y':
					os.system("systemctl status docker")
			elif ("work" in choice or "Work" in choice) and ("Images" in choice or "images" in choice):
				os.system("color 03")
				print("To know about the Images in Docker")
				print("To pull the image")
				print("To save the image and transfer it to specific system")
				print("To create our own image")
				print("To push the image on docker hub")
				print("To see the list of images")
				print("To exit from this option")
				os.system("tput setaf 7")
				while True:
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					Choice=r.recognize_google(audio)
					print("Speak Your Choice :")
					if ("about" in Choice) and ("Images" in Choice or "images" in Choice):
						pyttsx3.speak("A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings")
						
					elif ("pull" in Choice) and ("image" in Choice):
						pyttsx3.speak("Enter the name of image")
						img_name=input("Enter the name of image :")
						os.system("sudo docker pull {}".format(img_name))
					elif ("save" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Enter the name of Image to save")
						image_name=input("Enter the name of Image to save :")
						pyttsx3.speak("Enter the name of file in which u want to save")
						file_name=input("Enter the name of file:")
						pyttsx3.speak("Enter the IP address of system where u want to transfer ")
						IP_add=input("Enter the IP address:")
						os.system("sudo docker save {0} -o {1}.tar".format(image_name,file_name))
						#os.system("yum install openssh-clients")
						os.system("scp {0}.tar root@{1}/root".format(file_name,IP_add))
						remote_in=input("Do You want to load this image in remote system y/n :")
						
						
						if remote_in == 'y':
							os.system("tput setaf 4")
							print("Make sure that you should know root password")
							os.system("tput setaf 7")
							os.system("ssh {0} docker load -i {1}.tar".format(IP_add,file_name))
							
							
					elif ("create" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Enter the name of OS from which u want to create image")
						os_name=input("Enter the name of OS from which u want to create image :")
						pyttsx3.speak("Enter the name of image u want to create")
						imag_name=input("Enter the name of image u want to create :")
						os.system("sudo docker commit {0} {1}".format(os_name,imag_name))
					elif ("push" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Do You have acccount in docker hub and internet connectivity")
						user_ch=input("Do You have acccount in docker hub and internet connectivity press y/n :")
						if user_ch == 'y':
							pyttsx3.speak("Enter the image name")
							im_name=input("Enter the image name :")
							pyttsx3.speak("Enter your user name or id that u have in docker hub")
							user_name=input("Enter your user name or id that u have in docker hub :") 
							os.system("sudo docker tag {0} {1}/	{0}".format(im_name,user_name))
						else:
							#os.system("tput setaf 5")
							pyttsx3.speak("Please go to dockerhub.com , make account and then come again")
							print("Please go to dockerhub.com , make account and then come again")
							#os.system("tput setaf 7")
					elif ("list" in Choice) and ("images" in Choice or "Images" in Choice):
						os.system("docker images")				
					elif ("exit" in Choice or "Exit" in Choice or "close" in Choice):
						break
					else:
						pyttsx3.speak("Enter Valid option")
						print("Enter valid option")

			elif ("work" in choice or "Work" in choice) and ("Container" in choice or "container" in choice):
				os.system("color 06")
				print("/t/t/tNOTE 1: You can type exit when u are inside the container, this will get out of container")
				#os.system("tput setaf 5")
				print("/t/t/tNOTE 2: You can press Ctrl+p+q, this will get u out from container,without closing the container")
				os.system("color 04")
				print("\t\t\t->Excited to know what is container?")
				print("\t\t\t->To run the container")
				print("\t\t\t->To know the information about launched contaniner")
				print("\t\t\t->TO see the list of running containers ")
				print("\t\t\t->To see the list of background containers, also have a option to start and attach that container")
				print("\t\t\t->To exit from this option")
				while True:
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					cont_ch=r.recognize_google(audio)
					
					if ("know" in cont_ch) and ("container" in cont_ch) :
						pyttsx3.speak("A container is a standard unit of software that packages up code and all its dependencies so 				 the application runs quickly and reliably from one computing environment to another")
						
					elif ("run" in cont_ch) and ("container" in cont_ch):
						pyttsx3.speak("Enter the name u want to give to container")
						cont_name=input("Enter the name of Container:")
						pyttsx3.speak("Enter the name of image from which u want to launch the container")
						cont_img_name=input("Enter the name of image:")

						pyttsx3.speak("Do you want to run the container in the specific network")
						web_name_ch=input("Do you want to run the container in the specific network press y/n :")
						if web_name_ch == 'y':
							pyttsx3.speak("Enter the network name")
							web_name=input("Enter the network name :")
							os.system("sudo docker container run -it --name {0} --network {2}	{1}".format(cont_name,cont_img_name,web_name))
						else:	
							os.system("sudo docker container run -it --name {0} 	{1}".format(cont_name,cont_img_name))
					elif ("information" in cont_ch) and ("container" in cont_ch):
						pyttsx3.speak("Enter the container name")
						container_name=input("Enter the container name: ")
						os.system("sudo docker container inspect {}".format(container_name))
					elif ("list" in cont_ch) and ("containers" in cont_ch or "container" in cont_ch) and ("running" in cont_ch):
						os.system("sudo docker container ls")
					elif ("list" in cont_ch) and ("containers" in cont_ch or "container" in cont_ch) and ("background" in cont_ch or "back" in cont_ch):
						os.system("sudo docker container ls -a")
						pyttsx3.speak("Do u want to start the container")
						start_ch=input("To start the container Press y/n :")
						if start_ch=='y':
							pyttsx3.speak("Enter the name of container")
							start_name=input("Name of container :")
							os.system("sudo docker container start {}".format(start_name))
							pyttsx3.speak("Do you want to go inside the container")
							attach_ch=input("To go inside the container Press y/n :")
							if attach_ch == 'y':
								os.system("sudo docker container attach {}".format(start_name))
					elif cont_ch == 6:
						break
					else:
						print("Option is Invalid")
						pyttsx3.speak("Option is Invalid")
			elif ("work" in choice or "Work" in choice) and ("network" in choice or "Network" in choice):
				os.system("color 03")
				print("\t\t\t->To know about networking in docker")
				print("\t\t\t->To Create our own network")
				print("\t\t\t->To know the information of network")
				print("\t\t\t->To see the list of networks")
				print("\t\t\t->To do the Patting")
				print("\t\t\t->To exit from the option")
				os.system("tput setaf 7")
				while True:
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					net_ch=r.recognize_google(audio)
				
					if ("know" in net_ch or "Know" in net_ch) and ("networking" in net_ch or "Networking" in net_ch):
						pyttsx3.speak("To build web applications that act in concert but do so securely, create a network. Network  provide complete isolation for containers. You can add containers to a network when you first run a container")
						
					elif ("create" in net_ch or "Create" in net_ch) and ("network" in net_ch or "Network" in net_ch):
						pyttsx3.speak("Enter the name of network")
						net_name=input("Enter the name of network :")
						os.system("sudo docker network create --driver bridge {}".format(	
					net_name))
					
					elif ("information" in net_ch or "Information" in net_ch) and ("network" in net_ch or "Network" in net_ch):
						network_name=input("Enter the name of network :")
						os.system("sudo docker network inspect {}".format(network_name))
					elif ("list" in net_ch or "List" in net_ch) and ("networks" in net_ch or "Networks" in net_ch):
						os.system("sudo docker network ls")
					elif ("patting" in net_ch or "Patting" in net_ch):
						pyttsx3.speak("Enter the name for new container")
						OS_name=input("Name for new container :")
						pyttsx3.speak("Enter the image name for launching container")
						IMG_name=input("Image name for launching container:")
						pyttsx3.speak("Enter the port no")
						port_no=int(input("Enter the port no :"))
						os.system("sudo docker run -dit --name {} -p {}:80 {}".format(OS_name,IMG_name,port_no))
					elif net_ch == 6:
						break
					else:
						print("Option is Invalid")
						pyttsx3.speak("Option is Invalid")
			elif ("work" in choice or "Work" in choice) and ("volume" in choice or "Volume" in choice):
				os.system("color 04")
				print("\t\t\t->Know about the volume in docker")
				print("\t\t\t->Create volume")
				print("\t\t\t->Attach or mount volume to container")
				print("\t\t\t->exit from volume")
				os.system("tput setaf 7")
				while True:
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					vol_ch=r.recognize_google(audio)
					
					if ("know" in vol_ch or "Know" in vol_ch) and ("volume" in vol_ch or "Volume" in vol_ch):
						pyttsx3.speak("A volume is a persistent data.It is used to quickly allow other containers to mount")
						
					elif ("create" in vol_ch or "Create" in vol_ch) and ("volume" in vol_ch or "Volume" in vol_ch):
						pyttsx3.speak("Enter the name of volume")
						vol_name=input("Name of volume :")
						os.system("sudo docker volume create {}".format(vol_name))
					elif ("attach" in vol_ch or "mount" in vol_ch or "Mount" in vol_ch or "Attach" in vol_ch):
						pyttsx3.speak("Enter the container name")
						os_Name=input("Name of Container: ")
						pyttsx3.speak("Enter the Image name")
						img_Name=input("Enter the Image name: ")
						pyttsx3.speak("Enter the volume name")
						vol_Name=input("Enter the volume name: ")
						os.system("sudo docker run -it --name {} {}:/var/www/html {}".format(os_Name,vol_Name,img_Name))
					elif ("exit" in vol_ch or "close" in vol_ch):
							break
			elif ("Install" in choice or "install" in choice) and ("Docker" in choice or "docker" in choice) and ("Compose" in choice or "compose" in choice):
				os.system("""sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose""")
				os.system("sudo chmod +x /usr/local/bin/docker-compose")	
			elif ("launch" in choice or "Launch" in choice) and ("Wordpress" in choice or "site" in choice):
				os.system("sudo docker-compose up")	
			elif ("Close" in choice or "close" in choice) and ("Wordpress" in choice or "site" in choice):
				os.system("sudo docker-compose down")
			elif ("close" in choice or "exit" in choice or "Exit" in choice):
				exit()
			else:
				print("\t\t\t----Please Enter valid choice----")
				pyttsx3.speak("Please Enter valid choice")
	else:
		pyttsx3.speak("Enter the Remote IP")
		ip=input("\t\tEnter remote ip:")
		while True:
			info()
			with sr.Microphone() as source:
				print("Speak your choice ")
				audio = r.listen(source)
				print("\t\t\twe got it, plz wait....")

			choice=r.recognize_google(audio)
			

			if ("start" in choice) and ("docker" in choice):
				os.system("ssh root@{} systemctl start docker".format(ip))
				#os.system("tput setaf 5")
				print("Also want to see the status of docker press y/n",end="...")
				#os.system("tput setaf 7")
				status_input=input()
				if status_input =='y'or status_input =='Y':
					os.system("ssh root@{} systemctl status docker".format(ip))
			elif ("work" in choice or "Work" in choice) and ("Images" in choice or "images" in choice):
				os.system("color 03")
				#os.system("tput setaf 7")
				while True:
					print("\t\t\t*Know about the Images in Docker")
					print("\t\t\t*Pull the image")
					print("\t\t\t*Save the image and transfer it to specific system")
					print("\t\t\t*Create our own image")
					print("\t\t\t*Push the image on docker hub")
					print("\t\t\t*See the list of images")
					print("\t\t\t*Exit from this option")
					input()
					with sr.Microphone() as source:
						print("\t\t\tSpeak your choice.. ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					Choice=r.recognize_google(audio)
					print("Speak Your Choice :")
					if ("about" in Choice) and ("Images" in Choice or "images" in Choice):
						pyttsx3.speak("A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings")
						
					elif ("pull" in Choice) and ("image" in Choice):
						pyttsx3.speak("Enter the name of image")
						img_name=input("Enter the name of image :")
						os.system("ssh root@{1} sudo docker pull {0}".format(img_name,ip))
					elif ("save" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Enter the name of Image to save")
						image_name=input("Enter the name of Image to save :")
						pyttsx3.speak("Enter the name of file in which u want to save")
						file_name=input("Enter the name of file:")
						pyttsx3.speak("Enter the IP address of system where u want to transfer ")
						IP_add=input("Enter the IP address:")
						os.system("ssh root@{2} sudo docker save {0} -o {1}.tar".format(image_name,file_name,ip))
						os.system("yum install openssh-clients")
						os.system("ssh root@{2} scp {0}.tar root@{1}/root".format(file_name,IP_add,ip))
						remote_in=input("Do You want to load this image in remote system y/n :")
						
						
						if remote_in == 'y':
							os.system("tput setaf 4")
							print("Make sure that you should know root password")
							os.system("tput setaf 7")
							os.system("ssh root@{2} ssh {0} docker load -i {1}.tar".format(IP_add,file_name,ip))
							
							
					elif ("create" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Enter the name of OS from which u want to create image")
						os_name=input("Enter the name of OS from which u want to create image :")
						pyttsx3.speak("Enter the name of image u want to create")
						imag_name=input("Enter the name of image u want to create :")
						os.system("ssh root@{2} sudo docker commit {0} {1}".format(os_name,imag_name,ip))
					elif ("push" in Choice) and ("image" in Choice or "Image" in Choice):
						pyttsx3.speak("Do You have acccount in docker hub and internet connectivity")
						user_ch=input("Do You have acccount in docker hub and internet connectivity press y/n :")
						if user_ch == 'y':
							pyttsx3.speak("Enter the image name")
							im_name=input("Enter the image name :")
							pyttsx3.speak("Enter your user name or id that u have in docker hub")
							user_name=input("Enter your user name or id that u have in docker hub :") 
							os.system("ssh root@{2} sudo docker tag {0} {1}/	{0}".format(im_name,user_name,ip))
						else:
							os.system("tput setaf 5")
							pyttsx3.speak("Please go to dockerhub.com , make account and then come again")
							print("Please go to dockerhub.com , make account and then come again")
							os.system("tput setaf 7")
					elif ("list" in Choice) and ("images" in Choice or "Images" in Choice):
						os.system("ssh root@{} docker images".format(ip))				
					elif ("exit" in Choice or "Exit" in Choice or "close" in Choice):
						break
					else:
						pyttsx3.speak("Enter Valid option")
						print("Enter valid option")
					input()
					os.system("cls")

			elif ("work" in choice or "Work" in choice) and ("Container" in choice or "container" in choice):
				
				while True:
					os.system("color 06")
					print("\t\t\tNOTE 1: You can type exit when u are inside the container, this will get out of container")
					#os.system("tput setaf 5")
					print("\t\t\tNOTE 2: You can press Ctrl+p+q, this will get u out from container,without closing the container")
					os.system("color 04")
					print("\t\t\t->Excited to know what is container?")
					print("\t\t\t->To run the container")
					print("\t\t\t->To know the information about launched contaniner")
					print("\t\t\t->TO see the list of running containers ")
					print("\t\t\t->To see the list of background containers, also have a option to start and attach that container")
					print("\t\t\t->To exit from this option")
					input()
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					cont_ch=r.recognize_google(audio)
					
					if ("know" in cont_ch) and ("container" in cont_ch) :
						pyttsx3.speak("A container is a standard unit of software that packages up code and all its dependencies so 				 the application runs quickly and reliably from one computing environment to another")
						
					elif ("run" in cont_ch) and ("container" in cont_ch):
						pyttsx3.speak("Enter the name u want to give to container")
						cont_name=input("Enter the name of Container:")
						pyttsx3.speak("Enter the name of image from which u want to launch the container")
						cont_img_name=input("Enter the name of image:")

						pyttsx3.speak("Do you want to run the container in the specific network")
						web_name_ch=input("Do you want to run the container in the specific network press y/n :")
						if web_name_ch == 'y':
							pyttsx3.speak("Enter the network name")
							web_name=input("Enter the network name :")
							os.system("ssh root@{3} sudo docker container run -dit --name {0} --network {2}	{1}".format(cont_name,cont_img_name,web_name,ip))
						else:	
							os.system("ssh root@{2} sudo docker container run -dit --name {0} 	{1}".format(cont_name,cont_img_name,ip))
					elif ("information" in cont_ch) and ("container" in cont_ch):
						pyttsx3.speak("Enter the container name")
						container_name=input("Enter the container name: ")
						os.system("ssh root@{1} sudo docker container inspect {0}".format(container_name,ip))
					elif ("list" in cont_ch) and ("containers" in cont_ch or "container" in cont_ch) and ("running" in cont_ch):
						os.system("ssh root@{} sudo docker container ls".format(ip))
					elif ("list" in cont_ch) and ("containers" in cont_ch or "container" in cont_ch) and ("background" in cont_ch or "back" in cont_ch):
						os.system("ssh root@{} sudo docker container ls -a".format(ip))
						pyttsx3.speak("Do u want to start the container")
						start_ch=input("To start the container Press y/n :")
						if start_ch=='y':
							pyttsx3.speak("Enter the name of container")
							start_name=input("Name of container :")
							os.system("ssh root@{1} sudo docker container start {0}".format(start_name,ip))
							pyttsx3.speak("Do you want to go inside the container")
							attach_ch=input("To go inside the container Press y/n :")
							if attach_ch == 'y':
								os.system("ssh root@{1} sudo docker container attach {0}".format(start_name,ip))
					elif cont_ch == 6:
						break
					else:
						print("Option is Invalid")
						pyttsx3.speak("Option is Invalid")
					input()
					os.system("cls")
			elif ("work" in choice or "Work" in choice) and ("network" in choice or "Network" in choice):
				
				#os.system("tput setaf 7")
				while True:
					os.system("color 03")
					print("\t\t\t->To know about networking in docker")
					print("\t\t\t->To Create our own network")
					print("\t\t\t->To know the information of network")
					print("\t\t\t->To see the list of networks")
					print("\t\t\t->To do the Patting")
					print("\t\t\t->To exit from the option")
					input()
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					net_ch=r.recognize_google(audio)
				
					if ("know" in net_ch or "Know" in net_ch) and ("networking" in net_ch or "Networking" in net_ch):
						pyttsx3.speak("To build web applications that act in concert but do so securely, create a network. Network  provide complete isolation for containers. You can add containers to a network when you first run a container")
						
					elif ("create" in net_ch or "Create" in net_ch) and ("network" in net_ch or "Network" in net_ch):
						pyttsx3.speak("Enter the name of network")
						net_name=input("Enter the name of network :")
						os.system("ssh root@{1} sudo docker network create --driver bridge {0}".format(net_name,ip))
					
					elif ("information" in net_ch or "Information" in net_ch) and ("network" in net_ch or "Network" in net_ch):
						network_name=input("Enter the name of network :")
						os.system("ssh root@{1} sudo docker network inspect {0}".format(network_name,ip))
					elif ("list" in net_ch or "List" in net_ch) and ("networks" in net_ch or "Networks" in net_ch):
						os.system("ssh root@{} sudo docker network ls".format(ip))
					elif ("patting" in net_ch or "Patting" in net_ch):
						pyttsx3.speak("Enter the name for new container")
						OS_name=input("Name for new container :")
						pyttsx3.speak("Enter the image name for launching container")
						IMG_name=input("Image name for launching container:")
						pyttsx3.speak("Enter the port no")
						port_no=int(input("Enter the port no :"))
						os.system("ssh root@{} sudo docker run -dit --name {} -p {}:80 {}".format(ip,OS_name,IMG_name,port_no))
					elif net_ch == 6:
						break
					else:
						print("Option is Invalid")
						pyttsx3.speak("Option is Invalid")
					input()
					os.system("cls")
			elif ("work" in choice or "Work" in choice) and ("volume" in choice or "Volume" in choice):
				
				#os.system("tput setaf 7")
				while True:
					os.system("color 04")
					print("\t\t\t->Know about the volume in docker")
					print("\t\t\t->Create volume")
					print("\t\t\t->Attach or mount volume to container")
					print("\t\t\t->exit from volume")
					input()
					with sr.Microphone() as source:
						print("Speak your choice ")
						audio = r.listen(source)
						print("\t\t\twe got it, plz wait....")

					vol_ch=r.recognize_google(audio)
					
					if ("know" in vol_ch or "Know" in vol_ch) and ("volume" in vol_ch or "Volume" in vol_ch):
						pyttsx3.speak("A volume is a persistent data.It is used to quickly allow other containers to mount")
						
					elif ("create" in vol_ch or "Create" in vol_ch) and ("volume" in vol_ch or "Volume" in vol_ch):
						pyttsx3.speak("Enter the name of volume")
						vol_name=input("Name of volume :")
						os.system("ssh root@{} sudo docker volume create {}".format(ip,vol_name))
					elif ("attach" in vol_ch or "mount" in vol_ch or "Mount" in vol_ch or "Attach" in vol_ch):
						pyttsx3.speak("Enter the container name")
						os_Name=input("Name of Container: ")
						pyttsx3.speak("Enter the Image name")
						img_Name=input("Enter the Image name: ")
						pyttsx3.speak("Enter the volume name")
						vol_Name=input("Enter the volume name: ")
						os.system("ssh root@{} sudo docker run -it --name {} {}:/var/www/html {}".format(ip,os_Name,vol_Name,img_Name))
					elif ("exit" in vol_ch or "close" in vol_ch):
							break
					input()
					os.system("cls")
			elif ("Install" in choice or "install" in choice) and ("Docker" in choice or "docker" in choice) and ("Compose" in choice or "compose" in choice):
				os.system("""ssh root@{} sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose""".format(ip))
				os.system("ssh root@{} sudo chmod +x /usr/local/bin/docker-compose".format(ip))	
				input()
				os.system("cls")
			elif ("launch" in choice or "Launch" in choice) and ("Wordpress" in choice or "site" in choice):
				os.system("ssh root@{} sudo docker-compose up".format(ip))
				input()
				os.system("cls")	
			elif ("Close" in choice or "close" in choice) and ("Wordpress" in choice or "site" in choice):
				os.system("ssh root@{} sudo docker-compose down".format(ip))
				input()
				os.system("cls")
			elif ("close" in choice or "exit" in choice or "Exit" in choice):
				exit()
			else:
				print("\t\t\t----Please Enter valid choice----")
				pyttsx3.speak("Please Enter valid choice")
			input()
			os.system("cls")


	


	

