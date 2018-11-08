#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from cpt.packager import ConanMultiPackager

__PACKAGE_NAME__ = 'libffi'
PATTERN_ = re.compile(r'conanio/(?P<compiler>gcc|clang)(?P<version>\d+)(-(?P<arch>\w+))?')

if __name__ == "__main__":
#    command = 'echo start build %s'%__PACKAGE_NAME__
#    #if os.environ.get('CONAN_DOCKER_IMAGE') and os.environ.get('CONAN_GCC_VERSIONS'):
##    command += ' && sudo chmod 666 /etc/apt/sources.list'
##    command += ' && sudo echo deb mirrors.kernel.org/ubuntu cosmic main >> /etc/apt/sources.list'
#    command += ' && sudo apt-get update -y' 
#    command += ' && sudo apt-get upgrade -y' 
#    command += ' && sudo apt-get -y install libltdl-dev'
#    command += ' && sudo apt-get -y install texinfo'     
#    command += ' && ls /usr/share/aclocal/ltdl.m4 -l'
#
#    command = 'ls -l && sudo ./docker_entry_script.sh'
    docker_entry_script = ''    
    if PATTERN_.match(os.environ.get('CONAN_DOCKER_IMAGE','')):
        docker_entry_script = '/bin/sh docker_entry_script.sh'
        
    builder = ConanMultiPackager(docker_entry_script=docker_entry_script)
    builder.add_common_builds(pure_c=True)

#    filter(__PACKAGE_NAME__,builder)
    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if options["libffi:shared"] == True and settings["arch"] == "x86_64":
             filtered_builds.append([settings, options, env_vars, build_requires])
    builder.builds = filtered_builds
    
    builder.run()


#from bincrafters import build_template_default
#import platform
#import os
#from conanos.sdk.profile import filter
#if platform.system() == 'Windows':
#    os.environ['CONAN_VISUAL_VERSIONS']=os.environ.get('CONAN_VISUAL_VERSIONS','15')
#
#PACKAGE_NAME='libffi'	
#if __name__ == "__main__":
#    builder = build_template_default.get_builder()
#    filter(PACKAGE_NAME,builder)
#
#    builder.run()
