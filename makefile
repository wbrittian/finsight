.PHONY: run install test

run: install
	@cd src && python3 main.py

install:
	@conan install . --output-folder=build --build=missing -s build_type=Release
	@conan install . --output-folder=build --build=missing -s build_type=Debug

test: install
	