"""
这题没有什么难点，不用re库的话就头尾双指针，遇到非法字符就移动，移动时也要判断是否越界
NOTE: 空字符串也是回文串，可以跟面试官确认下
"""
import re
import unittest


# 击败98%，不过调了内置库...
def solution(s: str) -> bool:
    s = re.sub(r'\W+', '', s).lower()
    # return s == s[::-1]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False)
    ]

    def test(self):
        for input, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, solution(input))
