"""Aqui se ejecutan todas la pruebas para validar que pase el ejercicio
"""
# TODO: add test completly

import pytest
from unittest import TestCase

# import functions interviews
from .find_contacts import contacts
from .brackets import isBalanced
from .median import runningMedian

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