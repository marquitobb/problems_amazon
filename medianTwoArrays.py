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
        """function for find type median sorted

        Args:
            nums1 (List[int]): array number one
            nums2 (List[int]): array number two

        Returns:
            float: return median when sum array

        Big O notantion: O(2)
        """

        array_temp = []    # o(1)
        array_finally = []
        option_one = 0
        option_two = 0
        result = 0.0

        for item_two in nums2:
            for item_one in nums1:
                print("one---",item_one)
                print("two---",item_two)
                if item_one < item_two:
                    array_temp.append(item_one)
        print("r---",array_temp)


        # if len(array_temp)%2 == 0:  # o(1)
        #     option_one = int((len(array_temp)/2)-1)
        #     option_two = int(len(array_temp)/2)
        #     result = (float(array_temp[option_one]) + float(array_temp[option_two])) /2.0
        # else:
        #     result = array_temp[int((len(array_temp)/2)-0.5)]

        # return result  # o(1)
        return 0.0


if __name__ == '__main__':
    s = Solution()
    # nums1 = [1,2]
    # nums2 = [3]
    # print(s.findMedianSortedArrays(nums1,nums2))
    # nums1 = [1,2]
    # nums2 = [3,4]
    # print(s.findMedianSortedArrays(nums1,nums2))
    nums1 = [1,3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1,nums2))