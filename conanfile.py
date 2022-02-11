from conans import ConanFile

class SimpleOneLibCPFTestProject(ConanFile):
    
    url = "https://github.com/Knitschi/BCPFTestProject"
    license = "MIT"
    description = "A package that is created by the BCPFTestProject repository."

    # Dependencies
    python_requires = "CPFConanfile/0.0.20@knitschi/development",
    python_requires_extend = "CPFConanfile.CPFBaseConanfile",

    cpf_conanfile_module = None

    def init(self):

        self.cpf_conanfile_module = self.python_requires["CPFConanfile"].module

        self.cpf_conanfile_module.init_impl(
            self,
            self.cpf_conanfile_module.CPFBaseConanfile,
            "https://github.com/Knitschi/BCPFTestProject.git",
            path_CPFCMake='Sources/CPFCMake',
            path_CPFBuildscripts='Sources/CPFBuildscripts',
            path_CIBuildConfigurations='Sources/CIBuildConfigurations'
            )

