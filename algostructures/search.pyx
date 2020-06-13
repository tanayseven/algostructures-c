from array import array

cdef extern from "search/array_search.h":
    int search(const int numbers[], const int length, const int key)
    int search_parallel(const int numbers[], const int length, const int key) nogil

cpdef int py_search(numbers, length, key):
    cdef int[:] c_numbers = array("i", numbers)
    cdef int c_length = length 
    cdef int c_key = key
    cdef int i
    cdef int result = -1
    result = search(&c_numbers[0], c_length, c_key)
    return result

cpdef int py_search_parallel(numbers, length, key):
    cdef int[:] c_numbers = array("i", numbers)
    cdef int c_length = length 
    cdef int c_key = key
    cdef int i
    cdef int result = -1
    with nogil:
        result = search_parallel(&c_numbers[0], c_length, c_key)
    return result
