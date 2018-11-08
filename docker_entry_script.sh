#!/bin/bash

set -e
set -x

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get -y install libltdl-dev
sudo apt-get -y install texinfo  
export DEBIAN_FRONTEND=noninteractive
export DEBCONF_NONINTERACTIVE_SEEN=true
sudo apt-get install -y tzdata
sudo apt-get -y install dejagnu  
