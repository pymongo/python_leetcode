import unittest


class Solution(unittest.TestCase):
    TESTCASES = [
        ("eceba", 3, 4)
    ]

    def test(self):
        for s, k, max_len in self.TESTCASES:
            self.assertEqual(max_len, self.f(s, k))

    # 返回 S 中至少包含 k 个不同字符的子串的数量
    @staticmethod
    def f(s: str, k: int) -> int:
        left = 0
        counter = dict()
        size = len(s)
        max_len = 0
        for right in range(size):
            counter[s[right]] = counter.get(s[right], 0) + 1
            # 如果s[left:right]内不同元素个数超过k个，则左边界需要收缩
            while left <= right and len(counter) > k:
                if counter[s[left]] == 1:
                    counter.pop(s[left])
                else:
                    counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
