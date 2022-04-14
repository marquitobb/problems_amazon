"""Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from pip import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # TODO: add sum two arrays
        array_temp = nums1+nums2
        print("size-->", len(array_temp))
        print("example-->",len(array_temp)/2)
        if len(array_temp)%2 == 0:
            print("option_one-->", (len(array_temp)/2)-1)
            print("option_two-->", len(array_temp)/2)
        else:
            print("option-->",(len(array_temp)/2)-0.5)
        return 2.50000


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2]
    nums2 = [3]
    print(s.findMedianSortedArrays(nums1,nums2))
    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays(nums1,nums2))