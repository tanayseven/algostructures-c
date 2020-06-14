#include <algo_constants.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>

long long search(const long long numbers[], const long long length, const long long key) {
    for (long long index = 0; index < length; index++) {
        if (key == numbers[index])
            return index;
    }
    return INDEX_NOT_FOUND;
}

long long search_parallel(const long long numbers[], const long long length, const long long key) {
    long long result_index = -1;
    #pragma omp for
    for (long long index = 0; index < length; index++) {
        if (key == numbers[index])
            result_index = index;
    }
    return result_index;
}
