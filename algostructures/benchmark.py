from random import randrange
from timeit import timeit
from typing import Generator

from algostructures.search import py_search, py_search_parallel

TIMEIT_REPS = 10


def random_int_generator(integer_digits: int) -> Generator[int, None, None]:
    print(f"Generating {integer_digits} random numbers")
    for _ in range(integer_digits):
        yield randrange(integer_digits)
    print(f"Generation of {integer_digits} random numbers complete")


def benchmark_search(search_list_size: int):
    list_of_random_ints = [number for number in random_int_generator(search_list_size)]
    element_to_search = list_of_random_ints[-1]
    time_taken = timeit(lambda: py_search(list_of_random_ints, len(list_of_random_ints), element_to_search), number=TIMEIT_REPS)
    print(f"Time taken for sequential search of {search_list_size} length of elements: {time_taken:.5f}")
    time_taken = timeit(lambda: py_search_parallel(list_of_random_ints, len(list_of_random_ints), element_to_search), number=TIMEIT_REPS)
    print(f"Time taken for parallel search of {search_list_size} length of elements: {time_taken:.5f}")


if __name__ == '__main__':
    print("=== Benchmarking the algorithms, this will take a while... ===")
    benchmark_search(100000000)
    print("=== Benchmarking completed! ===")
