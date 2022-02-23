cmake_minimum_required(VERSION 3.15)
project(test_package_FPackage CXX)

find_package(FPackage CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example F::Component1 F::Component2)
