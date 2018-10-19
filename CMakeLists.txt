PROJECT(conanzlib)
cmake_minimum_required(VERSION 2.8)

#set(LIBFFI_SOURCE_DIRECTORY  D:/github.com/conanos/libffi/source_subfolder/testsuite)
#set(LIBFFI_INCLUDE_DIRECTORY D:/github.com/conanos/libffi/source_subfolder/x86_64-w64-cygwin)
#set(LIBFFI_LIBS_DIRECTORY D:/github.com/conanos/libffi/source_subfolder/x86_64-w64-cygwin/.libs)

include_directories(${LIBFFI_INCLUDE_DIRECTORY} ${LIBFFI_INCLUDE_DIRECTORY}/include)

macro(MakeTest suitename casename files)
    
    set(srcs)
    foreach(name ${files})
       list(APPEND srcs ${LIBFFI_SOURCE_DIRECTORY}/${suitename}/${name})
    endforeach()
    add_executable(${suitename}-${casename} ${srcs})

    target_link_libraries(${suitename}-${casename}  ${LIBFFI_LIBS_DIRECTORY}/libffi-7.lib)   
    add_test(${suitename}-${casename} ${suitename}-${casename})
endmacro()
enable_testing()
file(COPY  ${LIBFFI_LIBS_DIRECTORY}/libffi-7.dll DESTINATION  ${BUILD_TYPE} )

set(rootd ${LIBFFI_SOURCE_DIRECTORY}/libffi.call)
file(GLOB files RELATIVE ${rootd} ${rootd}/*.c)

foreach(name ${files})
   message(" [${name}]")
   MakeTest(libffi.call ${name} ${name})    
endforeach(name ${files})

