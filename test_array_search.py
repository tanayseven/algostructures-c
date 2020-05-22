from array_search import lib, ffi

input_list = [34, 23, 56, 38, 94, 35, 75, 28, 48, 47]
valid_search_key = 28
invalid_search_key = 1000


def test_sequential_valid_key():
    acutal_result = lib.search(input_list, len(input_list), valid_search_key)
    expected_result = 7
    assert acutal_result == expected_result

def test_sequential_invalid_key():
    acutal_result = lib.search(input_list, len(input_list), invalid_search_key)
    expected_result = -1
    assert acutal_result == expected_result

def test_parallel_valid_key():
    acutal_result = lib.search_parallel(input_list, len(input_list), valid_search_key)
    expected_result = 7
    assert acutal_result == expected_result

def test_parallel_invalid_key():
    acutal_result = lib.search_parallel(input_list, len(input_list), invalid_search_key)
    expected_result = -1
    assert acutal_result == expected_result
