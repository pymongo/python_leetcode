import unittest
from typing import List


# noinspection PyPep8Naming
def four_sum_eq_0(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    pairs = dict()
    count = 0
    for a in A:
        for b in B:
            pairs[a + b] = pairs.get(a + b, 0) + 1
    for c in C:
        for d in D:
            count += pairs.get(-(c + d), 0)
    return count


class Testing(unittest.TestCase):
    TEST_CASES = [
        {'A': [1, 2], 'B': [-2, -1], 'C': [-1, 2], 'D': [0, 2], 'output': 2},
        {'A': [0], 'B': [0], 'C': [0], 'D': [0], 'output': 1},
    ]

    def test(self):
        for case in self.TEST_CASES:
            self.assertEqual(case['output'], four_sum_eq_0(case['A'], case['B'], case['C'], case['D']))
