import unittest
from typing import List


# 前缀和的大致思想
# 如果nums[0:2]的和为2，如果nums[0:4]的和也为2，说明 nums[0:2] - (nums[0:2] + nums[3:4]) = 0
# 也就是nums[3:4]=0
def prefix_sum(nums: List[int]) -> List[int]:
    # key: prefix_sum, value: end_index
    prefix_sum_map = {}
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        # 这步可以优化成，sum_map的初始值为{0: -1}，这样遇到nums[0,i]=0时，直接返回[-1+1, i]
        if curr_sum == 0:
            return [0, i]
        if curr_sum in prefix_sum_map:
            return [prefix_sum_map[curr_sum]+1, i]
        prefix_sum_map[curr_sum] = i
    raise Exception("unreachable")


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([-3, 1, -4, 2, -3, 4], [1, 5]),
        ([-3, 1, 2, -3, 4], [0, 2]),
    ]

    def test_prefix_sum(self):
        for nums, expected in self.TEST_CASES:
            print(nums, expected)
            self.assertListEqual(expected, prefix_sum(nums))
