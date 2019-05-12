#!/bin/bash

#install the base requirements at system level
sudo apt update
sudo apt install python3
sudo apt install python3-pip
#install venv
sudo apt install python3-venv

#create users
sudo adduser telegram_bot_master
sudo adduser telegram_bot_test

#create the virtual env in telegram_bot_master
sudo apt install python3-venv
sudo mkdir /home/telegram_bot_master/bot_00
cd /home/telegram_bot_master/bot_00
python3 -m venv env #create venv
source env/bin/activate
#Install all libs required in this
echo Check requrements
pip3 install -r requirements 
env deactivate

#create the virtual env in telegram_bot_test
sudo apt install python3-venv
sudo mkdir /home/telegram_bot_test/bot_00
cd /home/telegram_bot_test/bot_00
python3 -m venv env
source env/bin/activate
#Install all libs required in this
echo Check requrements
pip3 install -r requirements 
env deactivate

#now login as user tu run the bot