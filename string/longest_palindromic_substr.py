import unittest
from typing import List, Tuple
from pydbg import dbg


def expand_center(s: str, size: int, left: int, right: int) -> int:
    while s[left] == s[right] and left > 0 and right < size:
        left -= 1
        right += 1
    # 如果左边和右边不相等，例如ab，它也是个回文串，应该返回2
    return right - left + 1


def longest_palindromic_substr(s: str) -> str:
    # 非法入参处理
    if not isinstance(s, str):
        return ""

    # 特殊情况处理
    size: int = len(s)
    if size < 2:
        return s

    max_len: int = 1
    max_len_start_index: int = 0
    # 中心扩散
    for i in range(1, size - 1):
        odd_len: int = expand_center(s, size, i, i)
        even_len: int = expand_center(s, size, i, i + 1)
        temp_max_len: int = max(odd_len, even_len)
        if temp_max_len > max_len:
            max_len = temp_max_len
            max_len_start_index = i-max_len//2

    dbg(max_len_start_index)
    return s[max_len_start_index:(max_len_start_index+max_len)]


# 由于DP解法大多按列遍历，不能命中CPU缓存，就用中心扩散了
class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, str]] = [
        ("babad", "bab"),
        ("abadd", "aba"),
        ("cbbd", "bb"),
        ("aba", "aba"),
        ("ac", "a"),
        ("ccc", "ccc"),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], longest_palindromic_substr(case[0]))
