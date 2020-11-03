import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        ("99", "111", "11010")
    ]

    def test(self):
        for A, B, expected in self.TESTCASES:
            self.assertEqual(expected, self.SumofTwoStrings(A, B))

    @staticmethod
    def SumofTwoStrings(A: str, B: str) -> str:
        a, b = len(A) - 1, len(B) - 1
        res = ""
        while a >= 0 and b >= 0:
            res = str(int(A[a]) + int(B[b])) + res
            a -= 1
            b -= 1
        if a >= 0:
            res = A[:a + 1] + res
        elif b >= 0:
            res = B[:b + 1] + res
        return res
