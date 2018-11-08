#!/bin/bash

set -e
set -x

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get -y install libltdl-dev
sudo apt-get -y install texinfo  
ls /usr/share/aclocal/ltdl.m4 -l'