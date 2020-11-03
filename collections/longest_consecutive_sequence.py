import unittest
from typing import List


# 这题问你的是一个乱序数组中，最长连续的元素个数有几个
# TODO 并查集+路径压缩解法也是O(n)时间复杂度
class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_len = 1
                curr_num = num
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len


class Testing(unittest.TestCase):
    TESTCASES = [
        ([100, 4, 200, 1, 3, 2], 4)
    ]

    def test(self):
        solution = Solution()
        for nums, longest_consecutive_length in self.TESTCASES:
            self.assertEqual(longest_consecutive_length, solution.longestConsecutive(nums))
