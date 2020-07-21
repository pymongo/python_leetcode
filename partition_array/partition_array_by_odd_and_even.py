import unittest
from typing import List


# 这题算是sort_colors的简单版，只有两种情况，而sort_colors有0,1,2三种情况
# |373|[Partition Array by Odd and Even]
def partition_odd_and_even(nums: List[int]):
    odd, even = 0, len(nums) - 1
    curr = 0
    while odd < even:
        if nums[curr] % 2 == 1:
            odd += 1
            curr += 1
        else:
            nums[curr], nums[even] = nums[even], nums[curr]
            even -= 1


# |49|[Sort Letters by Case]
def partition_lower_upper(chars: List[str]):
    lower, upper = 0, len(chars) - 1
    curr = 0
    while lower < upper:
        if chars[curr].islower():
            lower += 1
            curr += 1
        else:
            chars[curr], chars[upper] = chars[upper], chars[curr]
            upper -= 1


class Testing(unittest.TestCase):
    ODD_EVEN_TEST_CASES = [
        ([1, 2, 3, 4], [1, 3, 4, 2])
    ]

    LOWER_UPPER_TEST_CASES = [
        (['A', 'c'], 'cA')
    ]

    def test_partition_odd_even(self):
        for nums, expected in self.ODD_EVEN_TEST_CASES:
            partition_odd_and_even(nums)
            self.assertEqual(expected, nums)

    def test_lower_upper(self):
        for chars, expected in self.LOWER_UPPER_TEST_CASES:
            partition_lower_upper(chars)
            self.assertEqual(expected, chars)
