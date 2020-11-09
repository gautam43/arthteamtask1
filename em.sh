#!/bin/bash
  
sudo mv core-site.xml /root/
sudo mv hdfs-site.xml /root/
sudo su - root
mv core-site.xml /etc/hadoop/
mv hdfs-site.xml /etc/hadoop/
hadoop datanode - format
hadoop-daemon.sh start datanode
jps
