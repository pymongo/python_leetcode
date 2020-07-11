import unittest
# Python binary search的API
import bisect


class TwoSum:

    def __init__(self):
        self.nums = []
        self.length = 0

    def add(self, num: int):
        bisect.insort(self.nums, num)
        self.length += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, target: int) -> bool:
        pass


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
