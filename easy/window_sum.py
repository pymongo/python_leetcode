import unittest
from typing import List


# 将滑动窗口从头移到尾，输出从开始到结束每一个时刻滑动窗口内的数的和
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 7, 8, 5], 3, [10, 17, 20]),
        ([1, 2, 7, 7, 2], 3, [10, 16, 16]),
    ]

    def test(self):
        for nums, k, expected in self.TEST_CASES:
            self.assertListEqual(expected, self.f(nums, k))

    @staticmethod
    def f(nums: List[int], k: int) -> List[int]:
        size = len(nums)
        res = []
        if size == 0:
            return res

        left = 0
        curr_sum = 0
        for i in range(left, k-1):
            curr_sum += nums[i]

        for right in range(k-1, size):
            curr_sum += nums[right]
            res.append(curr_sum)

            curr_sum -= nums[left]
            left += 1
        return res
