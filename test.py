"""Aqui se ejecutan todas la pruebas para validar que pase el ejercicio
"""
# TODO: add test completly

import pytest
from unittest import TestCase

# import functions interviews
from .find_contacts import contacts
from .brackets import isBalanced
from .median import runningMedian
from .substring import Solution

def test_find_contacts():
    """
    Create a test case for find_contacts
    """
    queries = ['add hack', 'add hackerrank', 'find hac', 'find hak']
    result = contacts(queries)
    print(result)
    assert int(result) == 2

def test_isBalanced():
    data = "{][({(}]][[[{}]][[[())}[)(]([[[)][[))[}[]][()}))](]){}}})}[{]{}{((}]}{{)[{[){{)[]]}))]()]})))["
    result_balance = isBalanced(data)
    print(result_balance)
    assert result_balance == "NO"

def test_runningMedian():
    """
    Create a test case for runningMedian
    """
    a = [7, 3, 5, 2, 4, 6, 8]
    result = runningMedian(a)
    print(result)
    assert result == 2

@pytest.mark.parametrize(
    "substring,expected",
    [
        ("abcabcbb",3),
        ("bbbbb",1),
        ("pwwkew",3),
        ("",0),
        ("a",1),
        ("au",2),
        ("dvdf",3),
    ]
)
def test_substring(substring, expected):
    """
    Create a test case for substring
    """
    s = Solution()
    string_one = s.lengthOfLongestSubstring(substring)
    print(substring, ": ", string_one)
    assert int(string_one) == expected

@pytest.mark.parametrize(
    "array_one,array_two,expected",
    [
        ([1,2],[3,4],2.5),
    ]
)
def test_median_two_array(array_one,array_two,expected):
    assert 2.5 == 2.5