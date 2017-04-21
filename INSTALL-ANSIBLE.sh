#/bin/bash

##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
## ############################################################################################ ##
##                                                                                              ##
##  Install Ansible from git and configure the environment to be able to run Ansible dev-tools  ##
##                                                                                              ##
  ##############################################################################################
      ######################################################################################
CWD=$(cwd)

cd ..

echo "Ansible git clone"
git clone git://github.com/ansible/ansible.git --recursive

echo "Ansible package dependencies"
sudo apt install python-pip
sudo apt install build-essential make gcc
sudo apt install libffi6 libffi-dev libssl-dev

echo "Ansible Python requirements"
cat ansible/requirements.txt
sudo pip install jinja2 PyYAML paramiko pycrypto setuptools

echo "Ansible install"
cd ansible
python setup.py build
sudo python setup.py install
cd $CWD

echo ""
echo "Start using Ansible dev-tools with first:"
echo "\$  source ansible/hacking/env-setup"
echo "\$  ansible/hacking/test-module -m ./yourmodulename.py"

