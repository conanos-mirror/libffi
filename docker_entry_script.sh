#!/bin/bash

set -e
set -x
compiler=$1
version=$2
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get -y install libltdl-dev
sudo apt-get -y install texinfo  
#export DEBIAN_FRONTEND=noninteractive
#export DEBCONF_NONINTERACTIVE_SEEN=true
#sudo apt-get install -y tzdata
hint="skip dejagnu test conanio/${compiler}${version},since tzdata block" 
if [[ $compiler == 'gcc' && $version  -ge '8' ]]; then
   echo ${hint} 
elif [[ $compiler == 'clang' && $version  -ge '7' ]]; then
   echo ${hint} 
else
   sudo apt-get -y install dejagnu 
fi

