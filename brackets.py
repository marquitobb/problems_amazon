"""
Balanced Brackets

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
"""

#!/bin/python3

import math
from multiprocessing.connection import answer_challenge
import os
import random
import re
import sys
from unittest import result

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    temp = []
    answer = "YES"
    for i in s:
        if i == '(' or i == '[' or i == '{':
            temp.append(i)
        elif i == ')' or i == ']' or i == '}':
            if len(temp) > 0:
                if i == ')' and temp[-1] == '(':
                    temp.pop()
                elif i == ']' and temp[-1] == '[':
                    temp.pop()
                elif i == '}' and temp[-1] == '{':
                    temp.pop()
                else:
                    answer = "NO"
                    break
            else:
                answer = "NO"
                break
    return answer

if __name__ == '__main__':
    data = "{][({(}]][[[{}]][[[())}[)(]([[[)][[))[}[]][()}))](]){}}})}[{]{}{((}]}{{)[{[){{)[]]}))]()]})))["
    result_balance = isBalanced(data)
    print(result_balance)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     s = input()

    #     result = isBalanced(s)

    #     fptr.write(result + '\n')

    # fptr.close()
