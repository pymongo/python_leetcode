import unittest
from typing import List


def bubble_sort(A: List[int]):
    length: int = len(A)
    for i in range(length):
        for j in (i, length):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5])
    ]

    def test_bubble_sort(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(bubble_sort(case[0]), case[1])




