cmake_minimum_required(VERSION 3.20)
project(fab C)
project(test C)

set(CMAKE_C_STANDARD 99)

add_library(fab SHARED library.c)

add_executable(test test.c library.c)

if (NOT WIN32)
    target_link_libraries(fab m)
    target_link_libraries(test m)
endif()
