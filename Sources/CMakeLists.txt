# Root CMakeLists file for the "CMakeProjectFramework"
cmake_minimum_required (VERSION 3.8.0) 

include("${CMAKE_TOOLCHAIN_FILE}") # make sure the compiler is set before the project call	 
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/CPFCMake/Functions")
include(cpfInit)

##################################### CREATE PROJECT ########################################
project(BCPFTestProject)
cpfInit()

####################################### ADD Packages #############################################

set( externalPackages
	cotire
	CPFCMake
	CPFBuildscripts
)

set( globalFiles
	documentation/BCPFTestProjectDoc.dox
)

cpfAddPackages( "${externalPackages}" "${globalFiles}")
