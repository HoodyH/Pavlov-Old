#!/bin/bash

source env/bin/activate

while true; do python3 server.py; echo "command was killed, restarting it"; done

deactivate
