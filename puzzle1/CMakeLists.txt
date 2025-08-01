# TODO 1: Set the minimum required version of CMake to be 3.10
cmake_minimum_required(VERSION 3.28)

# TODO 2: Create a project named Tutorial
project(Puzzle)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Define source files 
set(SRCS  
    ${CMAKE_CURRENT_SOURCE_DIR}/puzzle.cpp
)

set(EXECUTABLE ${CMAKE_PROJECT_NAME})
add_executable(${EXECUTABLE}
    ${SRCS}
)

target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )
