"""
这题不用哈希表记录重复的话，解法过于脑经急转弯了
由于数组内的数组都是1..=n
可以将数组看做一个图，node.next = nums[node.val]
所以只要数组的1..=n里有重复元素，那么图中必有环
所以使用快慢指针去找环的入口就行了
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    TESTCASES = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
    ]

    def test(self):
        for nums, duplicate in self.TESTCASES:
            self.assertEqual(duplicate, self.f(nums))

    @staticmethod
    def f(nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        head = 0
        while head != slow:
            slow = nums[slow]
            head = nums[head]
        return slow
