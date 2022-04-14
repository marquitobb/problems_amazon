"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from array import array
from re import I

# TODO: optimize more
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_temp = ""
        array_result = []
        winner_string = ""
        cont = 0

        if len(s) == 1:
            return 1
        elif s == "":
            return 0

        # find max substring
        for item in s:
            cont += 1
            if item not in string_temp:
                string_temp += item
            else:
                find_equal = ""
                for j in reversed(string_temp):
                    if item == j:
                        break
                    find_equal = j + find_equal
                array_result.append(string_temp)
                string_temp = find_equal
                string_temp += item
            if len(s) == cont:
                array_result.append(string_temp)

        # compare max substring
        for i in array_result:
            if len(i) > len(winner_string):
                winner_string = i
            # print("winner: ", winner_string)
            # print("arrayresult: ", array_result)
            # return array_result
        return len(winner_string)

if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb")) # 3
    # print(s.lengthOfLongestSubstring("bbbbb")) # 1
    # print(s.lengthOfLongestSubstring("pwwkew")) # 3
    # print(s.lengthOfLongestSubstring("au")) # 2
    # print(s.lengthOfLongestSubstring("")) # 0
    # print(s.lengthOfLongestSubstring("e")) # 1
    # print(s.lengthOfLongestSubstring("dvdf")) # 3
    # print(s.lengthOfLongestSubstring("aab")) # 2
    print(s.lengthOfLongestSubstring("bpfbhmipx")) # 7