import unittest
from typing import List


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 5, 7], 4)
    ]

    def test(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, self.solution(nums))

    @staticmethod
    def solution(nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return 1
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
