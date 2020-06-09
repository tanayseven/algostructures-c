from collections import namedtuple

import pytest
from algostructures._array_search import lib

TestCase = namedtuple("TestCase", ["name", "input_list", "search_key", "expected_result"])

test_cases = [
    TestCase(
        name="valid search even length list",
        input_list=[34, 23, 56, 38, 94, 35, 75, 28, 48, 47],
        search_key=28,
        expected_result=7,
    ),
    TestCase(
        name="valid search odd length list",
        input_list=[34, 23, 56, 38, 94, 35, 75, 28, 48],
        search_key=28,
        expected_result=7,
    ),
    TestCase(
        name="invalid search",
        input_list=[34, 23, 56, 38, 94, 35, 75, 28, 48, 47],
        search_key=100,
        expected_result=-1,
    ),
]


@pytest.mark.parametrize("name,input_list,search_key,expected_result", test_cases)
def test_sequential(name, input_list, search_key, expected_result):
    print(name)
    acutal_result = lib.search(input_list, len(input_list), search_key)
    assert acutal_result == expected_result


@pytest.mark.parametrize("name,input_list,search_key,expected_result", test_cases)
def test_parallel(name, input_list, search_key, expected_result):
    print(name)
    acutal_result = lib.search_parallel(input_list, len(input_list), search_key)
    assert acutal_result == expected_result
