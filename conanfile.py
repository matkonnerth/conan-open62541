from conans import ConanFile, CMake, tools


class Open62541Conan(ConanFile):
    name = "open62541"
    version = "0.3.0"
    license = "Mozilla Public License v2.0"
    author = "matkonnerth@gmail.com"
    url = "https://github.com/matkonnerth/conan-open62541"
    homepage = "https://open62541.org/"
    description = "open source C99 implementation of OPC UA"
    topics = ("conan", "opcua", "open62541")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/open62541/open62541.git --branch=v0.3.0")
        self.run("cd open62541 && git submodule init")
        self.run("cd open62541 && git submodule update")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['UA_ENABLE_AMALGAMATION'] = False
        cmake.definitions['UA_ENABLE_FULL_NS0'] = False


        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.configure(source_folder="open62541")
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.libs = ["open62541"]

