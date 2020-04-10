from conans import ConanFile, CMake, tools


class Open62541Conan(ConanFile):
    name = "open62541"
    version = "latest"
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
        self.run("git clone https://github.com/open62541/open62541.git")
        self.run("cd open62541 && git checkout master")
        self.run("cd open62541 && git submodule init")
        self.run("cd open62541 && git submodule update")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = "Debug"
        cmake.definitions["UA_NAMESPACE_ZERO"] = "FULL"
        cmake.definitions["UA_ENABLE_SUBSCRIPTIONS_EVENTS"] = "ON"
        cmake.configure(source_folder="open62541")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "./"
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.libs = ["open62541"]

