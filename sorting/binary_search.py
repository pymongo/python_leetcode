import unittest
from copy import deepcopy


def solution(nums, target):
    size = len(nums)
    left, right = 0, size-1
    while left <= right:
        middle = (left+right) // 2
        if nums[middle] > target:
            right = middle-1
        elif nums[middle] < target:
            left = middle+1
        else:
            return middle
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1)
    ]

    def test(self):
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, solution(nums, target))
