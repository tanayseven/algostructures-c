#include <stdio.h>

#ifndef TEST_SUCCESS
    int _test_suite_exit_value;
    #define TEST_SUCCESS _test_suite_exit_value
#endif

#define ASSERT(EXPRESSION) if ((EXPRESSION) != 1) {\
        fprintf(stderr, "Assertion failure [%s] on line %d in file %s\n", #EXPRESSION, __LINE__, __FILE__); \
        _test_suite_exit_value = 1; \
    }
