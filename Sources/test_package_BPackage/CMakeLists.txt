cmake_minimum_required(VERSION 3.15)
project(test_package_BPackage CXX)

find_package(BPackage CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example b::BPackage )
