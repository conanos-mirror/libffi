#!/bin/bash

set -e
set -x
ls -l
echo ' ==> docker entry script'
sudo apt-get -y update  
sudo apt-get -y upgrade
sudo apt-get -y install libltdl-dev
sudo apt-get -y install texinfo  
ls /usr/share/aclocal/ltdl.m4 -l'