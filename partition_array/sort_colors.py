import unittest
from copy import deepcopy
from typing import List


# https://lintcode.com/problem/sort-letters-by-case/
# 和sort_color用的是完全一样的算法，只不过更简单，只有2个值区分，而sort_color有三个
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


# 思路，把所有2挪到右边，把所有0挪到左边，那么剩余的1就刚好在中间了
# 需要三根指针，左右以及curr
# 若nums[curr] = 0 则将其与 nums[p0]互换；
# 若nums[curr] = 2 则与 nums[p2]互换。
def partition(nums: List[int]):
    size = len(nums)
    left, right, current = 0, size - 1, 0

    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            # 与右指针交换值之后current不要动，需要再次判断右边换过来的值是不是0
            nums[right], nums[current] = nums[current], nums[right]
            right -= 1
        else:
            current += 1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        [1, 2, 0],
        [1, 0, 1, 2],
        [2, 0, 2, 1, 1, 0]
    ]

    def test(self):
        for nums in deepcopy(self.TEST_CASES):
            input_nums = deepcopy(nums)
            partition(input_nums)
            self.assertEqual(sorted(nums), input_nums)
