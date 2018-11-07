#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    brew install cmake || true

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    pyenv install 2.7.10
    pyenv virtualenv 2.7.10 conan
    pyenv rehash
    pyenv activate conan
else	
    echo "------------------------------------------"
    echo "------------------------------------------"
    sudo docker images
    gcc --version
    ls /usr/share/aclocal/ltdl.m4 -l
	sudo apt-get update
	sudo apt-get install libltdl-dev
    ls /usr/share/aclocal/ltdl.m4 -l 	
fi


pip install conan_package_tools
pip install conan  --upgrade
pip install bincrafters_package_tools
pip install conanos  --upgrade
conan user
