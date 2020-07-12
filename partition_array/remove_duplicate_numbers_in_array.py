"""
[lintcode only](https://www.lintcode.com/problem/remove-duplicate-numbers-in-array/description?_from=ladder&&fromId=161)
https://www.jiuzhang.com/solution/remove-duplicate-numbers-in-array/

Example 1:
Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
Explanation:
Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Example 2:
Input:
nums = [1,2,3]
Output:
[1,2,3]
3
"""

import unittest
from typing import List


def move_duplicate(nums: List[int]) -> int:
    length = len(nums)
    if length <= 1:
        return length
    # 指针停在最后一个无重复元素
    last_non_duplicate = 1
    seen = set()
    seen.add(nums[0])
    for i in range(1, length):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[last_non_duplicate] = nums[i]
            last_non_duplicate += 1
    return last_non_duplicate


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 1, 4, 4, 2], 4, [1, 3, 4, 2]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    def test_move_duplicate(self):
        for nums, unique_len, expected in self.TEST_CASES:
            output = move_duplicate(nums)
            self.assertEqual(unique_len, output)
            self.assertEqual(expected, nums[:unique_len])
