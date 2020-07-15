"""
https://leetcode.com/problems/find-k-closest-elements/
给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。在A中找与target最接近的k个整数。
返回这k个数并按照与target的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
"""

import unittest
from typing import List
def solution(nums: List[int], target: int, k: int) -> List[int]:

    return []


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3], 2, 3, [2, 1, 3]),
        ([1, 4, 6, 8], 3, 3, [4, 1, 6]),
    ]

    def test(self):
        for nums, target, k, expected in self.TEST_CASES:
            self.assertEqual(expected, solution(nums, target, k))
