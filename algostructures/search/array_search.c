#include <algo_constants.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>

int search(const int numbers[], const int length, const int key) {
    for (int index = 0; index < length; index++) {
        if (key == numbers[index])
            return index;
    }
    return INDEX_NOT_FOUND;
}

int search_parallel(const int numbers[], const int length, const int key) {
    const int total_threads = omp_get_max_threads();
    int accumulator[total_threads], thread_id;
    const int chunk = ceil((float)length / (float)total_threads);
    for (int i = 0 ; i < total_threads ; ++i) {        //  Initialize the array
        accumulator[i] = INDEX_NOT_FOUND;
    }
    #pragma omp parallel shared(accumulator) private(thread_id)
    {
        thread_id = omp_get_thread_num();
        int resultant_index = INDEX_NOT_FOUND;
        const int last_index = length < ((thread_id + 1) * chunk) ? length : (thread_id + 1) * chunk;
        for (int i = thread_id * chunk ; i <= last_index ; ++i) {
            if (key == numbers[i]) {
                resultant_index = i;
                break;
            }
        }
        accumulator[thread_id] = resultant_index;
    }
    for (int i = 0 ; i < total_threads ; ++i) {
        if (accumulator[i] != INDEX_NOT_FOUND) {
            return accumulator[i];
        }
    }
    return INDEX_NOT_FOUND;
}
