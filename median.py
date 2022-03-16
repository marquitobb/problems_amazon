"""The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set ,  is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted sample. In the sorted set ,  is the median.
Given an input stream of  integers, perform the following task for each  integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the  element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).

Sorted          Median
[7]             7.0
[3, 7]          5.0
[3, 5, 7]       5.0
[2, 3, 5, 7]    4.0

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    result = 0.0
    if len(a) % 2 == 0:
        pos_median = int(len(a)/2)
        result = (a[pos_median] + a[pos_median-1]) / 2
    else:
        pos_median = int((len(a)/2)+1)
        result = a[pos_median-1]

    return result

if __name__ == '__main__':

    a = [12, 4, 5, 3, 8, 7, 9, 2, 6]
    result = runningMedian(a)
    print(result)

