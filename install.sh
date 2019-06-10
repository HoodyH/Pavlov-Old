#!/bin/bash

#install the base requirements at system level
sudo apt update
sudo apt -y install python3
sudo apt -y install python3-pip

sudo apt -y install flac
sudo apt -y install ffmpeg

#create the virtual env
#sudo apt -y install python3-venv
#python3 -m venv env

#Install all libs required
echo Check requrements
pip3 install -r requirements 