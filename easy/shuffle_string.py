import unittest
from typing import List


# 类似循环移位字符串那题(rotate_string)
# 同样可以联想成「教室换座位的」
class Solution(unittest.TestCase):
    TESTCASES = [
        ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
    ]

    def test(self):
        for s, indices, output in self.TESTCASES:
            self.assertEqual(output, self.f(s, indices))

    @staticmethod
    def f(s: str, indices: List[int]) -> str:
        chars = list(s)
        output = chars.copy()
        for i, each in enumerate(indices):
            output[each] = chars[i]
        return ''.join(output)
