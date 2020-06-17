"""
https://www.lintcode.com/problem/longest-palindromic-subsequence
最长回文子序列是「最长回文子串」一题的follow up(变形题)

## dp矩阵的横坐标纵坐标定义
dp[i][j]表示第i到第j个字符组成子串的最长回文子序列的长度(i<=j)
dp[i][j]表示子串s[i..=j]的最长回文序列的长度
【注意】根据二维数组的规律，左边第一个索引值是表示第几行，所以i在表中是纵坐标
子序列的DP规律
if s[i] == s[j]:
    dp[i][j] = dp[i+1][j-1]
else:
    # 因为头尾不相等，在最长子序列中s[i]与s[j]不会同时出现
    # 这种情况下最长回文子串长度等于去掉头的字符串的最长子序列 和 去掉尾的字符串的最长子序列的较大者
    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

## 边界条件子串长度大于2
只有子串长度大于等于2时这种去掉头尾才能有意义
所以边界条件是
j-1 - (i+1) + 1 > 2
整理得j-i<3

## 初始条件
第一行和第一列以及对角线的值为1

## 填表遍历方向
由于表格的纵坐标i(i是二维数组外层索引，所以表示行是纵坐标)
i必须小于等于j，所以图表的合法区域是右上角
以入参aba为例(注意纵坐标是i)
if s[i] == s[j]:
    需要的值在右上方
else:
    需要下方的值(dp[i+1][j])
    需要左方的值(dp[i][j-1])
因此填表遍历的顺序是在右上角区域，从下到上，做左到右
  a b a
a 4 5 6
b   2 3
a     1
事实上1和2都是边界条件
"""
from mydbg import dbg
from pprint import pprint as p
import unittest
from typing import List, Tuple


def solution(s: str) -> int:
    size: int = len(s)
    if size <= 1:
        return size
    # 只有子串长度大于等于2时这种去掉头尾才能有意义
    elif size <= 3:
        if s[0] == s[size-1]:
            return size
        else:
            return size-1

    # 你以为第一行所有元素是二维数组的第一项dp[0][x]，实际上第一列
    dp: List[List[int]] = [[0] * 3 for _ in range(3)]
    # 不会遍历到表格的边界
    # i: 从下到上
    cnt = 0
    dbg(s)
    for i in range(size-2, -1, -1):
        # j：从左到右
        for j in range(i, size):
            dbg((i,j))
            cnt += 1
            dp[i][j] = cnt
            # if j-i < 3:
            #     dbg(0)
            #     dp[i][j] = 1
            #     continue
            # print("after 0")
            # if s[i] == s[j]:
            #     dbg(1)
            #     dp[i][j] = dp[i+1][j-1] + 2
            # else:
            #     dbg(2)
            #     dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    p(dp)
    return dp[0][size-1]
    # return dp[0][size-1]


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[str, int]] = [
        ("cbbd", 2),
        ("aba", 3),
        ("babad", 3),
        ("abadd", 3),
        ("ac", 1),
        ("ccc", 3),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            print(case)
            self.assertEqual(solution(case[0]), case[1])
