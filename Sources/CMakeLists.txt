# Root CMakeLists file for the BCPFTestProject

include("CPFCMake/cpfInitCIProject.cmake")
cmake_minimum_required(VERSION ${CPF_MINIMUM_CMAKE_VERSION}) 

project(BCPFTestProject)

cpfAddPackages()
