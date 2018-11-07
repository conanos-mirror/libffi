#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

	
echo "------------------------------------------"
echo "------------------------------------------"
sudo docker images
gcc --version
ls /usr/share/aclocal/ltdl.m4 -l
sudo apt-get update
sudo apt-get install libltdl-dev
ls /usr/share/aclocal/ltdl.m4 -l 

python build.py
