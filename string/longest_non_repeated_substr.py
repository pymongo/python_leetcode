import unittest


def solution(s: str) -> int:
    size = len(s)
    # left, right = 0, 0
    left = 0
    max_len = 0
    # index: ASCII of char
    # value: s.find(char)
    table = [-1 for _ in range(128)]
    for right in range(size):
        ord_right = ord(s[right])
        if table[ord_right] != -1:
            left = table[ord_right] - 1
            # table[ord_right] = -1
        table[ord_right] = right
        temp_max = right - left + 1
        if temp_max > max_len:
            max_len = temp_max
    return max_len


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abcabcbb", 3),
        ("abba", 2),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], solution(case[0]))
