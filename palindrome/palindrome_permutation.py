"""
https://www.lintcode.com/problem/palindrome-permutation/
https://www.lintcode.com/problem/longest-palindrome
这题的解法跟最长回文子串组合完全一样
只需要将返回值改为最长回文子串组合长度是否等于原字符串
"""
import unittest
import collections


def solution(s: str) -> bool:
    ascii_range_last = ord('z') + 1
    ascii_table = [0 for _ in range(ascii_range_last)]
    for char in s:
        ascii_table[ord(char)] += 1
    result = 0
    is_odd_occur = False
    for i in range(ord('A'), ascii_range_last):
        if ascii_table[i] % 2 == 0:
            result += ascii_table[i]
        else:
            is_odd_occur = True
            result += ascii_table[i] - 1
    if is_odd_occur:
        result += 1
    return result == len(s)


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("code", False),
        ("aab", True),
        ("carerac", True)
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], solution(case[0]))
