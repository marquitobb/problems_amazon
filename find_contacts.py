"""
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Example
Operations are requested as follows:

add ed
add eddie
add edward
find ed
add edwina
find edw
find a
"""

#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    # Write your code here
    find = [item_find[5:] for item_find in queries if "find" in item_find]
    count_find = 0
    for i in queries:
        if "add" in i:
            for item_add in find:
                if item_add in i:
                    count_find += 1
    return count_find


if __name__ == '__main__':
    queries = ['add hack', 'add hackerrank', 'find hac', 'find hak']
    result = contacts(queries)
    print(result)
