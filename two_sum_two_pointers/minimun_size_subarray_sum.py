import unittest
from typing import List
import sys


class Solution(unittest.TestCase):
    TEST_CASES = [
        ([2, 3, 1, 2, 4, 3], 7, 2),
    ]

    def test(self):
        for nums, target, min_len in self.TEST_CASES:
            self.assertEqual(min_len, self.sliding_window(target, nums))

    # 返回连续子数组和>=target的最小区间长度
    @staticmethod
    def sliding_window(target: int, nums: List[int]) -> int:
        min_len = sys.maxsize
        window_sum = 0
        left = 0
        for right, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                # 如果sum已经大于target, 窗口的左边界需要收缩
                window_sum -= nums[left]
                left += 1
        return min_len if min_len != sys.maxsize else 0
