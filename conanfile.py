#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from conans import ConanFile, tools, CMake
import platform
from conans import ConanFile, VisualStudioBuildEnvironment, AutoToolsBuildEnvironment
from conans.client.tools.oss import cross_building
from conanos.build import config_scheme
from conans import Meson

class LibFFIConan(ConanFile):
    name = "libffi"
    version = "3.299999"
    description = "libffi is a library that provides foreign function interface. "
    url = "http://github.com/libffi/libffi"
    homepage = "http://github.com/libffi/libffi"
    license = "MIT"
    exports = ["LICENSE"]
    generators = "visual_studio", "gcc"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = { 'shared': False, 'fPIC': True }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
        
        config_scheme(self)

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        url_ = "https://github.com/CentricularK/libffi.git"
        branch_ = "meson"
        git = tools.Git(folder=self._source_subfolder)
        git.clone(url_, branch=branch_)

    def build(self):
        prefix = os.path.join(self.build_folder, self._build_subfolder, "install")
        meson = Meson(self)
        meson.configure(defs={'prefix' : prefix},
                        source_dir=self._source_subfolder, build_dir=self._build_subfolder)
        meson.build()
        self.run('ninja -C {0} install'.format(meson.build_dir))

    def package(self):
        self.copy("*", dst=self.package_folder, src=os.path.join(self.build_folder,self._build_subfolder, "install"))


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
