#include <algo_constants.h>
int search(const int numbers[], const int length, const int key) {
    for (int index = 0; index < length; index++) {
        if (key == numbers[index])
            return index;
    }
    return INDEX_NOT_FOUND;
}
