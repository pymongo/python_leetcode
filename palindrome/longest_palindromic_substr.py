"""
# 第二讲：最长回文子串
本讲是互动课，互动课指的是提前录制好的若干个短视频，中间穿插单选题和编程题组成的课程

## Subsequence子序列
子序列可以是非连续的字符
对于长度为n的字符串的子序列，每个字符都有选或不选两种可能。
因此其子序列的数量是指数级别O(2^n)的

## Java和Python刷题要对入参作校验
这个是给面试官的加分项
对于非基本类型的入参，例如String
Java的第一行要写上 if s==null
Python则写上 if not s 或 if not isinstance(s, str)

## Python初始化二维布尔值数组
不能用 [[False]*3]*3 的方式定义一个3*3的数组
否则第二行和第三行都是第一行的shallow copy
有经验的做法是
dp = [[False]*3 for _ in range(3)]

## 除了manacher，后缀数组也是O(n)
suffix array(后缀数组)比较难，不太考

## 以最长回文子串这题看面试评分标准

### Strong Hire:
用O(n)或O(nlogn)算法，如manacher、suffix_array
这种评分一般是留给参加ACM竞赛的，或者想拿SP offer的应聘者

### Hire
用中心扩散或动态规划解题

### Weak Hire
只用一种O(n^2)算法，而且代码中有点Bug，也不能给面试官讲清楚算法过程
Weak Hire相当于弃权票，三轮面试中，2次给了Weak Hire，1次No Hire就挂了，或者让加面

### No Hire
面试官给提示后，想到O(n^2)的解法，但Bug太多或者不能AC

### Strong No Hire
一种算法都想不到，或者用暴力遍历结果超时

DP解法填表顺序注意事项:
除了i和j的其中一个要倒着遍历，另一种解决思路是，本质上解决的思路是
「先循环区间长度，再循环区间的起点」
for length in range(3, size+1):
    for i in range(size-length+1):
        j = i+length-1
        dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
注意这种写法一定要把子串s[i]的两侧s[i+1]和s[i-1]也初始化了，也就是所有长度为2的子串都初始化了
"""
import unittest
from typing import List, Tuple


# from mydbg import dbg


def expand_center(s: str, size: int, left: int, right: int) -> (int, int):
    while left >= 0 and right < size and s[left] == s[right]:
        left -= 1
        right += 1

    # 如果左边和右边不相等，例如ab，它不是个回文串，应该返回1
    # 由于跳出循环时哪怕两边不相等也会额外扩散一次，所以返回值要往里收缩一次
    return left + 1, right - 1

# 暴力穷举(brute_force)已经是多项式级别的时间复杂度的题不适合用动态规划，例如本题是O(n^3)
# 本题 manacher > 中心扩散 > 动态规划
def longest_palindromic_substr(s: str) -> str:
    # 非法入参处理
    if not isinstance(s, str):
        return ""

    # 特殊情况处理
    size: int = len(s)
    if size <= 1:
        return s

    max_len: int = 1
    max_len_left: int = 0
    max_len_right: int = 0
    # 由于DP解法大多按列遍历，不能命中CPU缓存，就用中心扩散了
    for i in range(size - 1):
        odd_left, odd_right = expand_center(s, size, i, i)
        even_left, even_right = expand_center(s, size, i, i + 1)
        odd_len = odd_right - odd_left + 1
        even_len = even_right - even_left + 1
        if odd_len > max_len:
            max_len, max_len_left, max_len_right = odd_len, odd_left, odd_right
        if even_len > max_len:
            max_len, max_len_left, max_len_right = even_len, even_left, even_right
    return s[max_len_left:max_len_right + 1]


class Solution:
    @staticmethod
    def dp_solution(s: str) -> str:
        size = len(s)
        max_len = 0
        max_start = 0
        # dp[i][j]表示子串s[i][j]是不是回文串
        dp = [[False] * size for _ in range(size)]
        # TODO 由于填表时依赖左下角的值，所以区间型动态规划最佳的填表方向是「左上-右下」对角线那样斜着填
        # 枚举子串的长度(枚举区间型动态规划的长度)
        for length in range(1, size + 1):
            # 枚举子串的起始位置i
            for i in range(size - length + 1):
                j = i + length - 1
                if length == 1:
                    # 左上右下对角线
                    dp[i][j] = True
                elif length == 2:
                    # 这是填表时的第二条斜线
                    # 长度为2的字符串，只看头尾是否相等判断是不是回文串
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                # 找到一个回文子串就要判断是否要更新最大值
                if dp[i][j] and length > max_len:
                    max_len = length
                    max_start = i
        return s[max_start:max_start + max_len]


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
        for input_str, expected1, expected2 in self.TEST_CASES[:]:
            self.assertIn(longest_palindromic_substr(input_str), [expected1, expected2])

    def test_dp_solution(self):
        for input_str, expected1, expected2 in self.TEST_CASES[:]:
            self.assertIn(Solution.dp_solution(input_str), [expected1, expected2])
