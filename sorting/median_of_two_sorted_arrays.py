import unittest
from typing import List


def solution(a: List[int], b: List[int]) -> float:
    len_a, len_b = len(a), len(B)
    # 确保A
    if len_a > len_b:
        return solution(b, a)
    if len_a == 0:
        if len_b % 2 == 0:
            return (b[len_b // 2 - 1] + b[len_b // 2]) / 2.0
        else:
            return b[len_b // 2]
    a_left, a_right = 0, len_a-1
    while a_left < a_right:
        a_mid = (a_left + a_right) // 2
    return -1


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
