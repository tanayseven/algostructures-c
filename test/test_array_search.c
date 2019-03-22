#include <stdio.h>
#include <uassert.h>
#include <array_search.h>

const int search_array[] = {34, 23, 56, 38, 94, 35, 75, 28, 48, 47};
const size_t search_array_length = sizeof(search_array)/sizeof(search_array[0]);
const int valid_search_key = 28;
const int invalid_search_key = 1000;

void test_sequential_valid_key(void) {
    const int expected_value = 7;
    const int actual_value = search(search_array, search_array_length, valid_search_key);
    ASSERT(expected_value == actual_value);
}

void test_sequential_invalid_key(void) {
    const int expected_value = -1;
    const int actual_value = search(search_array, search_array_length, invalid_search_key);
    ASSERT(expected_value == actual_value);
}

void search_test_suite(void) {
    test_sequential_valid_key();
    test_sequential_invalid_key();
}
