from conan import ConanFile

class MyProjectConan(ConanFile):
    name = "hackathon"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = "gtest/1.15.0"

    def layout(self):
        self.folders.source = "src"
