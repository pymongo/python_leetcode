import unittest
import collections


class Solution(unittest.TestCase):
    TEST_CASE = [
        ("AAAA", 0, 4),
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

        # i往右挪到时，j只可能不动或往右动
        # for子串起点i
        for i in range(size):
            # for子串终点j, 子串至少能有k那么长，这样即使每个字符不同也能通过k次替换成相同
            for j in range(i + k + 1, size + 1):
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

    def test_two_pointers(self):
        for s, k, expected in self.TEST_CASE:
            self.assertEqual(expected, self.two_pointers_sliding_window(s, k))

    @staticmethod
    def two_pointers_sliding_window(s: str, k: int) -> int:
        res = 1
        n = len(s)
        # 如果是lintcode上的解答，counter不放入s[i=0]的初始值也不会报错...
        d = {s[0]: 1}
        max_freq = 1
        j = 1
        for i in range(n):
            while j < n and j - i <= k + max_freq:
                d[s[j]] = d.get(s[j], 0) + 1
                max_freq = max(d.values())
                j += 1
                if j - i <= k + max_freq:
                    res = max(res, j - i)
            d[s[i]] -= 1
        return res

    # 更优秀的窗函数法，固定窗的右边界
    @staticmethod
    def best_solution(s: str, k: int) -> int:
        d = {}
        left = max_freq = len_s = 0
        for right, char in enumerate(s):
            len_s += 1
            d[char] = d.get(char, 0) + 1
            max_freq = max(max_freq, d[char])
            if right - left >= max_freq + k:
                d[s[left]] -= 1
                left += 1
        res = len_s - left
        return res

    @staticmethod
    def two_pointers_lintcode_ok_leetcode_err(s: str, k: int) -> int:
        # j指向满足条件子串的后一个字符
        size = len(s)
        if size <= k:
            return size
        j = 0
        max_freq = 0
        counter = {}

        ans = 0
        for i in range(size):
            # j-i是字符串长度, 由于有可能替换了k次后j往后是全是相同的字符，所以要用<=k继续往后搜索一次
            # 由于k可能为0，如果用<k, ("ABAB",k)会得到0，所以宁可j可以多右移一位
            # 不同那么多解释，就跟暴力解法中判断是否需要更新最大长度的情况一样
            while j < size and j - i <= k + max_freq:
                count_j = counter.get(s[j], 0) + 1
                counter[s[j]] = count_j
                max_freq = max(max_freq, count_j)
                j += 1

            # 退出循环时有可能是替换次数大于k
            if j - i - max_freq > k:
                # s[i:j]这段需要k+1次替换, 所以s[i:j-2]需要k次替换
                ans = max(ans, j - i - 1)
            else:
                # s[i:j]这段替换次数小于等于k
                ans = max(ans, j - i)

            # 离开当前循环时先要把i剔除掉
            count_i = counter.get(s[i], 0)
            if count_i == 1:
                counter.pop(s[i])
            else:
                counter[s[i]] = count_i - 1
            if count_i > 0 and count_i == max_freq:
                max_freq -= 1
        return ans
