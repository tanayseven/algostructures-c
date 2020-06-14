#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algo_constants.h>
#include <array_search.h>

int main(void) {
    const long long MAX = 1000000000;
    long long *numbers = (long long *)malloc(sizeof(long long) * MAX);
    clock_t generate_numbers_begin = clock();
    for (long long i = 0; i < MAX; ++i) {
        numbers[i] = i+1;
    }
    clock_t generate_numbers_end = clock();
    clock_t time_taken_to_generate_numbers = (clock_t) (generate_numbers_end - generate_numbers_begin);
    printf("Time taken to generate numbers: %ld\n", time_taken_to_generate_numbers);
    printf("Starting benchmarking...\n");
    clock_t search_begin = clock();
    search(numbers, MAX, 1);
    clock_t search_end = clock();
    clock_t time_taken_by_sequential_search = (clock_t) (search_end - search_begin);
    printf("Time taken for sequential search: %ld\n", time_taken_by_sequential_search);
    clock_t parallel_search_begin = clock();
    search_parallel(numbers, MAX, 1);
    clock_t parallel_search_end = clock();
    clock_t time_taken_by_parallel_search = (clock_t) (parallel_search_end - parallel_search_begin);
    printf("Time taken for parallel search: %ld\n", time_taken_by_parallel_search);
    free(numbers);

    return 0;
}