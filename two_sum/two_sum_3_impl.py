import unittest
# Python binary search的API
import bisect


class TwoSum:

    def __init__(self):
        self.nums = []
        self.length = 0

    def add(self, num: int):
        # 这里用插入排序可能性能更好
        bisect.insort(self.nums, num)
        self.length += 1

    def find(self, target: int) -> bool:
        start, end = 0, self.length - 1
        while start < end:
            temp_sum = self.nums[start] + self.nums[end]
            if temp_sum > target:
                end -= 1
            elif temp_sum < target:
                start += 1
            else:
                return True
        return False


class TestTwoSum(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 5], [(4, True), (7, False)]),
    ]

    def test(self):
        for nums, cases in self.TEST_CASES:
            two_sum = TwoSum()
            for num in nums:
                two_sum.add(num)
            for num, expected in cases:
                self.assertEqual(expected, two_sum.find(num))
