# Root CMakeLists file for the "CMakeProjectFramework"
cmake_minimum_required (VERSION 3.8.0) 

include("${CMAKE_TOOLCHAIN_FILE}") # make sure the compiler is set before the project call	 
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/CPFCMake/Functions")
include(cpfAddPackages)

##################################### CREATE PROJECT ########################################
project(BCPFTestProject)
cpfAddPackages()
