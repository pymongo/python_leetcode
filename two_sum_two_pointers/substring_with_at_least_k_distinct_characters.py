import unittest


class Solution(unittest.TestCase):
    TEST_CASES = [
        # s字符串内没有长度为4的无重复子串
        ("abcabcabca", 4, 0),
        ("abcabcabcabc", 3, 55),
    ]

    def test(self):
        for s, k, expected in self.TEST_CASES:
            self.assertEqual(expected, self.f(s, k))

    # 求至少包含k个不同字符的子串
    @staticmethod
    def f(s: str, k: int) -> int:
        count = 0
        size = len(s)
        if size == 0:
            return count
        for i in range(size):
            unique = set()
            unique_len = 0
            # 有点暴力求解的感觉，反正无论哪种时间复杂度都是O(n^2)
            for j in range(i, size):
                if s[j] not in unique:
                    unique.add(s[j])
                    unique_len += 1
                if unique_len >= k:
                    # 向右找一直找到distinct char 大于 k，break
                    # break出来之后，包括当前点，到末尾，所以的substring全都是解。
                    count += size - j
                    break
        return count
