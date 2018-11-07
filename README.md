| Windows | Linux |
|:------:|:------:|
| [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/conanos/libffi?svg=true)](https://ci.appveyor.com/project/Mingyiz/libffi) |[![Linux Build Status](https://api.travis-ci.org/conanos/libffi.svg)](https://travis-ci.org/conanos/libffi)|
# conan-libffi

Conan package for libffi library. https://github.com/libffi/libffi

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conanos/stable/libffi%3Aconanos).

## Basic setup

    $ conan install libffi/3.3-rc0@conanos/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    libffi/3.3-rc0@conanos/stable

    [options]
    libffi:shared=true # false

    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
