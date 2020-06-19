import unittest
from typing import List


def solution(nums1: List[int], nums2: List[int]) -> float:
    pass


class Test(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, 4], [3, 6, 8, 9], 3.5),
        ([1, 5, 6, 7], [2, 3, 4, 8], 4.5),
        ([1, 2], [3, 4, 5, 6, 7], 4),
        ([4, 5, 6], [1, 2, 3], 3.5),
        ([4, 5], [1, 2, 3, 6], 3.5),
        ([1, 3], [2, 4, 5, 6], 3.5),
        ([1, 2], [3, 4, 5, 6], 3.5),
        ([1, 3], [2, 4, 5], 3),
        ([1, 2, 3], [4, 5], 3),
        ([3, 4], [1, 2, 5], 3),
        ([-2, -1], [3], -1),
        ([1, 3], [2], 2),
        ([3], [-2, -1], -1),
        ([1, 2], [3, 4], 2.5),
        ([4, 5], [1, 2, 3], 3),
        ([1, 2], [1, 2, 3], 2),
        ([1, 2, 3], [1, 2, 3], 2),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[2], solution(case[0], case[1]))
