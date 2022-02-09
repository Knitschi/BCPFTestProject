from conans import ConanFile

class BPackageTest(ConanFile):

    # Dependencies
    python_requires =  "CPFConanfile/0.0.16@knitschi/development", "CPFPackageTestConanfile/0.0.1@knitschi/development",
    python_requires_extend = "CPFConanfile.CPFBaseConanfile", "CPFPackageTestConanfile.CPFBasePackageTestConanfile", 

    cpf_conanfile_module = None

    def init(self):
        self.cpf_conanfile_module = self.python_requires["CPFPackageTestConanfile"].module
        self.cpf_conanfile_module.init_impl(
            self,
            self.cpf_conanfile_module.CPFBasePackageTestConanfile,
            "BPackage")



