import unittest
from typing import List, Tuple
# from mydbg import dbg


def expand_center(s: str, size: int, left: int, right: int) -> (int, int):
    # dbg((left, right))
    while left >= 0 and right < size and s[left] == s[right]:
        left -= 1
        right += 1

    # 如果左边和右边不相等，例如ab，它不是个回文串，应该返回1
    # 由于跳出循环时哪怕两边不相等也会额外扩散一次，所以返回值要往里收缩一次
    # dbg(s[left+1:right])
    # dbg((left+1, right-1))
    return left+1, right-1


def longest_palindromic_substr(s: str) -> str:
    # 非法入参处理
    if not isinstance(s, str):
        return ""

    # 特殊情况处理
    size: int = len(s)
    if size <= 1:
        return s

    max_len: int = 1
    max_len_left: int = 0
    max_len_right: int = 0
    # 由于DP解法大多按列遍历，不能命中CPU缓存，就用中心扩散了
    for i in range(size - 1):
        odd_left, odd_right = expand_center(s, size, i, i)
        even_left, even_right = expand_center(s, size, i, i + 1)
        odd_len = odd_right - odd_left + 1
        even_len = even_right - even_left + 1
        if odd_len > max_len:
            max_len, max_len_left, max_len_right = odd_len, odd_left, odd_right
        if even_len > max_len:
            max_len, max_len_left, max_len_right = even_len, even_left, even_right
    return s[max_len_left:max_len_right+1]


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, str, str]] = [
        ("cbbd", "bb", "bb"),
        ("babad", "bab", "aba"),
        ("aba", "aba", "aba"),
        ("abadd", "aba", "bad"),
        ("ac", "a", "c"),
        ("ccc", "ccc", "ccc"),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertIn(longest_palindromic_substr(case[0]), [case[1], case[2]])
