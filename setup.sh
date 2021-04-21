#!/bin/bash

yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
yum install git -y
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install python3 -y
python3 -m pip install elasticsearch
python3 -m pip install requests
systemctl start docker
systemctl enable docker
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.12.0
docker run -d --name kibana --link elasticsearch:elasticsearch -p 5601:5601 kibana:7.12.0
docker run -d -p 8080:8080 -p 50000:50000 -v /jenkins:/var/jenkins_home jenkins

