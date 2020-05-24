PYTHONPATH=$(PWD)
export PYTHONPATH

SRC_PY:=$(shell find algostructures/ -name "*.py")
SRC_CACHE_FILES:=$(shell find algostructures/ -name "*.pyc")
TEST_PY:=$(shell find test/ -name "*.py")
TEST_CACHE_FILES:=$(shell find test/ -name "*.pyc")
SRC_C:=$(shell find algostructures/ -name "*.c" -or -name "*.h")
COMPILED_C:=$(shell find algostructures/ -name "_array_search*.c" -or -name "_array_search*.o" -or -name "_array_search*.so")

all: clean build test

.PHONY build:
build: $(SRC_C) wheel-package install-deps
	python -m algostructures.build
	python setup.py bdist_wheel

.PHONY install-deps:
install-deps: pip-tools-package requirements.txt requirements-dev.txt
	pip-sync requirements.txt requirements-dev.txt

requirements.txt: requirements.in
	pip-compile --generate-hashes requirements.in

requirements-dev.txt: requirements-dev.in
	pip-compile --generate-hashes requirements-dev.in

.PHONY install-deps:
update-deps: pip-tools-package requirements.txt requirements-dev.txt
	pip-sync requirements.txt requirements-dev.txt

.PHONY pip-tools-package:
pip-tools-package:
	python -c "import piptools" || pip install pip-tools

.PHONY wheel-package:
wheel-package:
	python -c "import wheel" || pip install wheel

.PHONY clean:
clean:
	rm -rf ./algostrutures/_array_search* dist/

.PHONY test:
test: $(SRC_CACHE_FILES) $(TEST_CACHE_FILES) $(COMPILED_C)
	pytest $(PYTHONPATH)

.PHONY help:
help:
	@echo "** MAKE TARGETS **"
	@echo "build        : compile the algorithms written in C and also the python wheel"
	@echo "update-deps  : update all the python packages in the requirements[-dev].in files"
	@echo "install-deps : install all the dependencies from the requirements[-dev].txt files"
	@echo "clean        : delete the compiled files of algorithms written in C"
	@echo "test         : run all the unit tests written"
	@echo "run          : start the algostructures program in a RELP mode"
	@echo "benchmark    : run benchmarking and generate report"
