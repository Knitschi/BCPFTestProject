cmake_minimum_required(VERSION 3.15)
project(test_package_GPackage CXX)

find_package(GPackage CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example g::GPackage)
