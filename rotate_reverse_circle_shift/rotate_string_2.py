"""
https://lintcode.com/problem/rotate-string-ii/description?_from=ladder&&fromId=161
https://jiuzhang.com/solution/rotate-string-ii/
给定left、right的循环移位量
如果left>right则将字符串循环向左移left-right位

输入：str ="abcdefg", left = 3, right = 1
输出："cdefgab"
解释：左偏移量为3，右偏移量为1，总的偏移量为向左2，故原字符串向左移动，变为"cdefg" + "ab"。

输入：str="abcdefg", left = 0, right = 0
输出："abcdefg"
解释：左偏移量为0，右偏移量为0，总的偏移量0，故字符串不变。

输入：str = "abcdefg",left = 1, right = 2
输出："gabcdef"
解释：左偏移量为1，右偏移量为2，总的偏移量为向右1，故原字符串向右移动，变为"g" + "abcdef"。
"""
import unittest
from typing import List


def reverse(s: List[int], start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


def cycle_shift(s: str, left: int, right: int) -> str:
    chars = list(s)
    length = len(chars)
    last_index = length - 1
    # k表示循环右移位数
    k = (right - left) % length
    reverse(chars, 0, last_index)
    reverse(chars, 0, k - 1)
    reverse(chars, k, last_index)
    return "".join(chars)


class UnitTest(unittest.TestCase):
    TESTCASES = [
        ("abcdefg", 3, 1, "cdefgab"),
        ("abcdefg", 0, 0, "abcdefg"),
        ("abcdefg", 1, 2, "gabcdef"),
    ]

    def test(self):
        for s, left, right, expected in self.TESTCASES:
            self.assertEqual(expected, cycle_shift(s, left, right))
