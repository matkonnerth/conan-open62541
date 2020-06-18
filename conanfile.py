from conans import ConanFile, CMake, tools

class Open62541Conan(ConanFile):
    name = "open62541"
    version = "master"
    license = "Mozilla Public License v2.0"
    url = "https://github.com/open62541/open62541"
    homepage = "https://open62541.org/"
    description = "open source C99 implementation of OPC UA"
    topics = ("opcua", "open62541")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        self.run("git clone https://github.com/open62541/open62541.git")
        #self.run("cd open62541 && git checkout tags/v"+self.version)
        self.run("cd open62541 && git checkout master")
        self.run("cd open62541 && git submodule init")
        self.run("cd open62541 && git submodule update")


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.definitions["UA_NAMESPACE_ZERO"] = "FULL"
        cmake.definitions["UA_ENABLE_SUBSCRIPTIONS_EVENTS"] = "ON"
        cmake.configure(source_folder="open62541")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        #cmake.definitions["CMAKE_INSTALL_PREFIX"] = "./"
        cmake.install()
        cmake.patch_config_paths()

    def package_info(self):
        self.cpp_info.libs = ["open62541"]
        if self.settings.build_type == "Debug" and self.settings.compiler == "clang":
            self.cpp_info.cflags = ["-fsanitize=address"]
            self.cpp_info.cflags.append('-fsanitize-address-use-after-scope')
            self.cpp_info.cflags.append('-fsanitize-coverage=trace-pc-guard,trace-cmp')
            self.cpp_info.cflags.append('-fsanitize=leak')
            self.cpp_info.cflags.append('-fsanitize=undefined')
            self.cpp_info.cxxflags = self.cpp_info.cflags 
            self.cpp_info.sharedlinkflags = ["-fsanitize=address"]
