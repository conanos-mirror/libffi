#!/bin/bash

set -e
set -x

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get -y install libltdl-dev
sudo apt-get -y install texinfo  
DEBIAN_FRONTEND=noninteractive sudo apt-get install -y tzdata
sudo apt-get -y install dejagnu  
 
ls /usr/share/aclocal/ltdl.m4 -l