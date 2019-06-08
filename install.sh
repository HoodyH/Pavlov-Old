#!/bin/bash

#install the base requirements at system level
sudo apt update
sudo apt install python3
sudo apt install python3-pip

#create the virtual env
#sudo apt install python3-venv
#python3 -m venv env

#Install all libs required
echo Check requrements
pip3 install -r requirements 