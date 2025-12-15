from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain

class VectornavDriverLib(ConanFile):
    name = "vndriverlib"
    version = "1.0.0"
    settings = ["os", "compiler", "build_type", "arch"]
    generators = "CMakeDeps", "CMakeToolchain"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["vndriverlib"]
