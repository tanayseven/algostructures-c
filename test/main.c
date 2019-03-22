#include <stdio.h>
#include <uassert.h>
#include <test_array_search.h>

void run_all_test_suites(void) {
    search_test_suite();
}

int main(int argc, char const *argv[])
{
    printf("Running tests...\n");
    run_all_test_suites();
    if (TEST_SUCCESS == 0) printf("All tests passed!\n");
    return TEST_SUCCESS;
}
