"""
https://www.lintcode.com/problem/longest-palindrome
输入一个字符串，通过组合字符串的每个字符，求出这些组合中最长回文串的长度
例如: cbbd的组合中，最长是3(bcb或bdb)

## 贪心算法
回文串中，每个字符要么出现奇数次，要么出现偶数次
可以借鉴桶排序/计数排序，定义一个ASCII的table记录每个字符的出现次数
最长回文串的组合可能是：奇数出现次数的最大值+所有偶数出现次数之和
这就是贪心算法，自己先假定一种数学公式能获得最大值，就像本题的sum(偶数次字符)+max(奇数次字符)
"""
import unittest


def solution(s: str) -> int:
    size = len(s)
    if size <= 1:
        return size
    ascii_table = [0 for _ in range(128)]
    for i in range(size):
        ascii_table[ord(s[i])] += 1
    # 奇数次出现次数的最大值
    max_odd = 0
    result = 0
    for i in range(128):
        if ascii_table[i] == 0:
            continue
        if ascii_table[i] % 2 == 0:
            result += ascii_table[i]
        else:
            if ascii_table[i] > max_odd:
                max_odd = ascii_table[i]
    result += max_odd
    return result




class Testing(unittest.TestCase):
    TEST_CASES = [
        ("abccccdd", 7),  # dccaccd
        ("cbbd", 3),  # bcb/bdb
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[1], solution(case[0]))
