# Setup repository
This repo is for setting up host with grafana and elasticsearch

# Elasticsearch
Elasticsearch runs as a container

# Grafana
Grafana also runs as a container

# Setup
In order to setup the environment either you need to run the shell script on the host as root or ansible. Follow the below instructions.

# a.Using shell
1. ssh root@ip-of-the-docker-host
2. run the command "bash setup.sh"

# b.Using ansible
1. add the docker host ip and it's credentials to the hosts.ini
2. run the command "ansible-playbook setup-playbook.yml -i hosts.ini"

