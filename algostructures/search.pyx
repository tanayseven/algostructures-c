from array import array

cdef extern from "search/array_search.h":
    long search(const long numbers[], const long length, const long key)
    long search_parallel(const long numbers[], const long length, const long key) nogil

cpdef long py_search(numbers, length, key):
    cdef long[:] c_numbers = array("l", numbers)
    cdef long c_length = length 
    cdef long c_key = key
    cdef long result = -1
    result = search(&c_numbers[0], c_length, c_key)
    return result

cpdef long py_search_parallel(numbers, length, key):
    cdef long [:] c_numbers = array("l", numbers)
    cdef long  c_length = length 
    cdef long  c_key = key
    cdef long result = -1
    with nogil:
        result = search_parallel(&c_numbers[0], c_length, c_key)
    return result
