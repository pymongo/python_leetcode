import unittest
import collections


class Solution(unittest.TestCase):
    TEST_CASE = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ]

    def test_brute_force(self):
        for s, k, expected in self.TEST_CASE:
            self.assertEqual(expected, self.brute_force(s, k))

    @staticmethod
    def brute_force(s: str, k: int):
        size = len(s)
        if size <= k:
            return size
        max_len = k

        # for子串起点i
        for i in range(size):
            # for子串终点j, 子串至少能有k那么长，这样即使每个字符不同也能通过k次替换成相同
            for j in range(i + k + 1, size+1):
                # 目标: i和j之间需要几次替换才能完全一样，如果替换次数<=k则更新max_len
                # 统计i和j之间出现次数最多的字符
                # 优化: 多次重复计算子串之间重复字母的出现次数
                counter = collections.Counter(s[i:j])
                max_freq = max(counter.values())
                curr_len = j - i
                print(curr_len)
                print(s[i:j])
                if curr_len <= k + max_freq:
                    max_len = max(max_len, curr_len)
        return max_len
