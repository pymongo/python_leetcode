import unittest


def solution(s: str) -> int:
    size = len(s)
    left = 0
    max_len = 0

    # index: ASCII of char
    # value: s.find(char)
    table = [-1 for _ in range(128)]

    for right in range(size):
        ord_right = ord(s[right])
        if table[ord_right] != -1:
            # 避免重复的字符「不在当前的移动窗口中」
            # max能确保左指针只会向前移动
            # 例如abba的用例，当right移到第二个a时，left在第二个b，此时虽有重复但是left不能往左移到第一个a，会导致计算的最大长度变大
            left = max(left, table[ord_right] + 1)
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
        for s, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, solution(s))
