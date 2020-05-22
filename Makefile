CC=gcc
CFLAGS:=-Wall -Werror -fpic -c -I./src -I./include -std=c11 -fopenmp
SRC=src/array_search.c
PERF_TEST_SRC=perf_test/main.c
BUILD_SO=./build/algostrutures.so
BUILD_O=./build/algostrutures.o

build: $(BUILD_SO)

$(BUILD_SO): $(BUILD_O)
	$(CC) -shared -o $(BUILD_SO) $(BUILD_O)

$(BUILD_O): $(SRC)
	$(CC) -o $(BUILD_O) $(SRC) $(CFLAGS)

.PHONY clean:
clean:
	rm -rf ./build/*

.PHONY setup_on_mac:
setup_on_mac:
	brew reinstall clang-omp

