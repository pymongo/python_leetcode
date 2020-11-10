import unittest
from typing import List


# 和longest_consecutive_sequence这题不同的是，这题只判断连续递增，而且不要求数字之间只差1
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 5, 7], 4)
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, self.solution(nums))

    @staticmethod
    def solution(nums: List[int]) -> int:
        # lintcode上正序逆序都要检索，所以正序遍历一遍后，数组逆序后再遍历一遍
        size = len(nums)
        if size < 2:
            return size
        ptr = 1
        max_len = 1
        curr_len = 1
        while ptr < size:
            if nums[ptr - 1] < nums[ptr]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
            ptr += 1
        max_len = max(max_len, curr_len)
        return max_len
