# We can set this to whatever we choose. A safe starting point is the current version determined by "cmake --version"
cmake_minimum_required(VERSION 3.10)

# Set the project name:
project(Hello)

# Do any OS-specific work like setting system-specific compiler flags:
if("${CMAKE_SYSTEM_NAME}" STREQUAL "Linux")
    message("Running on Linux...")
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "Windows")
    message("Running on Windows...")
elseif("${CMAKE_SYSTEM_NAME}" STREQUAL "Darwin")
    message("Running on Mac...")
else()
    message("Not sure what this is running on...")
    message("${CMAKE_SYSTEM_NAME}")
endif()

# Specify name for executable and source file from which to compile it:
add_executable(hello-cmake hello-cmake.cpp)