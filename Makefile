CC=gcc
CFLAGS:=-Wall -I./include -I./src -I./test -std=c11 -fopenmp
SRC=src/array_search.c
TEST_SRC=test/main.c test/test_array_search.c test/uassert.c
PERF_TEST_SRC=perf_test/main.c
TEST_BIN=./bin/tests

.PHONY test:
test: build
	$(TEST_BIN)

build: $(TEST_BIN)

./bin/tests: $(TEST_SRC) ./bin
	$(CC) -o $(TEST_BIN) $(TEST_SRC) $(SRC) $(CFLAGS)

./bin:
	mkdir bin

.PHONY clean:
clean:
	rm -rf ./bin/*

.PHONY setup_on_mac:
setup_on_mac:
	brew reinstall clang-omp

