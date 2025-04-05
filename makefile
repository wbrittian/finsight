.PHONY: build run install test

build: install
	@cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=./conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
	@cd build && cmake --build .

run: build
	@cd build && ./poker-engine

clean:
	rm -rf build

install:
	@conan install . --output-folder=build --build=missing -s build_type=Release
	@conan install . --output-folder=build --build=missing -s build_type=Debug

test: build
	cd build && ctest --output-on-failure