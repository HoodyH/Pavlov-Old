#!/bin/bash

python3 -m venv env

source env/bin/activate

#Install all libs required
echo Check requrements
pip3 install -r requirements

deactivate