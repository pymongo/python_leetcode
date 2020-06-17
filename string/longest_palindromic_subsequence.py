"""
https://www.lintcode.com/problem/longest-palindromic-subsequence
最长回文子序列是「最长回文子串」一题的follow up(变形题)

## dp矩阵的横坐标纵坐标定义
dp矩阵的纵坐标i表示子序列的结束位置
dp矩阵的横坐标j表示子序列的起始位置
dp[i][j]表示第i到第j个字符组成子串的最长回文子序列的长度(i<=j)
注意本题的i是纵坐标，这是为了遍历时更简单
子序列的DP规律
if s[i] == s[j]:
    # 要查询的旧值在当前位置的左下方，所以只能从左到右遍历
    dp[i][j] = dp[i+1][j-1]
else:
    # 因为头尾不相等，在最长子序列中s[i]与s[j]不会同时出现
    # 这种情况下最长回文子串长度等于去掉头的字符串的最长子序列 和 去掉尾的字符串的最长子序列的较大者
    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

## 初始条件
1. dp[0][j] = 1
2. dp[j][0] = 1
3. 对角线的值为1

## DP矩阵遍历方向
以入参aba为例(注意纵坐标是i)
if s[i] == s[j]:
    需要的值在左下方
  a b a
a   1 3
b     2
a
"""
# from mydbg import dbg
import unittest
from typing import List, Tuple


def solution(s: str) -> int:
    size: int = len(s)
    if size <= 1:
        return size
    dp: List[List[int]] = [[1] * 3 for _ in range(3)]



    return 0


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
            self.assertIn(solution(case[0]), [case[1], case[2]])
