#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import ConanFile, tools, CMake
import platform
from conans import ConanFile, VisualStudioBuildEnvironment, AutoToolsBuildEnvironment

class LibFFIConan(ConanFile):
    name = "libffi"
    version = "3.3-rc0"
    description = "libffi is a library that provides foreign function interface. "
    url = "http://github.com/libffi/libffi"
    homepage = "http://github.com/libffi/libffi"
    license = "http://github.com/libffi/libffi/LICENSE"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=True", "fPIC=True"

    source_subfolder = "source_subfolder"


    def config_options(self):
        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def configure(self):
        del self.settings.compiler.libcxx

    def build_requirements(self):
        if platform.system() == "Windows":
            #self.build_requires("mingw_installer/1.0@conan/stable")
            #self.build_requires("msys2_installer/latest@bincrafters/stable")
            self.build_requires("cygwin_installer/2.9.0@bincrafters/stable")
            

    def source(self):
               
        url = "https://github.com/libffi/libffi/archive/v{version}.tar.gz"
        tools.get(url.format(version =self.version))
        os.rename("libffi-" + self.version, self.source_subfolder)

    def build(self):
        import os
        os.system("ls /usr/share/aclocal/ltdl.m4 -l")
        if self.settings.compiler == 'Visual Studio':
            self.msvc_build()
        
        if self.settings.compiler == 'gcc':
            self.gcc_build()

    def msvc_build(self):
        host = build = 'x86_64-w64-cygwin'
        with tools.chdir(self.source_subfolder):
            msvcc = os.path.abspath( os.path.join('msvcc.sh') ).replace("\\","/")
            msvcc = '/cygdrive/%s '%msvcc.replace(":","/")
            msvcc += '-m64' if self.settings.arch == 'x86_64' else '-m32'
            if self.settings.build_type == 'Debug':
                msvcc += ' -g '

            options = ' '
            options += " CC='%s'"%msvcc
            options += " CXX='%s'"%msvcc
            options += " LD='link'"
            options += " CPP='cl -nologo -EP'"
            options += " CXXCPP='cl -nologo -EP'"
            options += " CPPFLAGS='-DFFI_BUILDING_DLL'"
            options += " AR='./.travis/ar-lib lib'"
            options += " NM='dumpbin -symbols'"
            options += " STRIP=':'"
            options += " --build=%s"%build
            options += " --host=%s"%host
            self.run( tools.vcvars_command(self.settings) + 
                " && sh ./autogen.sh "
                " && sh ./configure %s"%options +
                " && cp src/x86/ffitarget.h include" +
                " && make" 
                )
            rootd = os.path.abspath('.').replace('\\','/')

            defs={'LIBFFI_SOURCE_DIRECTORY': '%s/testsuite'%rootd ,
                  'LIBFFI_INCLUDE_DIRECTORY':'%s/%s'%(rootd,build),
                  'LIBFFI_LIBS_DIRECTORY':'%s/%s/.libs'%(rootd,build),
                  'BUILD_TYPE': self.settings.build_type
                  }
            cmake = CMake(self)
            cmake.configure(defs=defs)
            cmake.build()
            cmake.test()
        #tools.mkdir("package")
        
    def gcc_build(self):
        with tools.chdir(self.source_subfolder):
            self.run("autoreconf -f -i")

            autotools = AutoToolsBuildEnvironment(self)
            _args = ["--prefix=%s/build"%(os.getcwd()), "--enable-introspection"]
            if self.options.shared:
                _args.extend(['--enable-shared=yes','--enable-static=no'])
            else:
                _args.extend(['--enable-shared=no','--enable-static=yes'])
            autotools.configure(args=_args)
            autotools.make()#args=["-j2"])
            if self.settings.os == platform.system():
                # if not cross build
                self.run('make check')
            autotools.install()


    def package(self):
        if self.settings.os == "Windows":
            builddir=os.path.join(self.source_subfolder,'x86_64-w64-cygwin')
            builddir=os.path.abspath(builddir)
            bindir=os.path.join(builddir,'.libs')
            incdir=os.path.join(builddir,'include')

            self.copy(pattern="libffi-*.dll",dst="bin",src=bindir)
            self.copy(pattern="libffi-*.lib",dst="lib",src=bindir)
            self.copy(pattern="*.h",dst="include",src= incdir)

        if self.settings.os == "Linux":
            self.copy("*", src="%s/build"%(self.source_subfolder))


    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs = ['libffi-7']
        else:
            self.cpp_info.libs = ["libffi-7"]
