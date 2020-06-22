"""
以下两题都可以用同一个贪心算法解决
- https://leetcode.com/problems/longest-palindrome/
- https://leetcode.com/problems/palindrome-permutation/

## 同向双指针的贪心解法(有点像最长回文子序列的dp思路)
这题不能用排列组合回文串的贪心算法，因为这题要求在原字符串上去掉0个或1个字符，
整体要求有序，更像是子序列
s[left] != s[right]时
判断去掉头(left)后是否回文:  s[left-1:right]
判断去掉尾(right)后是否回文: s[left:right-1]
只要去掉头或去掉尾其中一个是回文就行了
"""
import unittest


class Solution:
    @staticmethod
    def find_difference(s: str, left: int, right: int) -> (int, int):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return left, right

    @staticmethod
    def is_palindrome(s: str):
        left, right = Solution.find_difference(s, 0, len(s) - 1)
        if left >= right:
            return True
        else:
            return False

    @staticmethod
    def valid_palindrome(s: str) -> bool:
        """
        以 tebbem 为例
        left=0, right=5时发现不相等
        于是检查去掉尾tebbe和去掉头ebbem的其中一个是不是回文串
        """
        left, right = Solution.find_difference(s, 0, len(s) - 1)
        if left >= right:
            return True
        return Solution.is_palindrome(s[left:right]) or Solution.is_palindrome(s[left + 1:right + 1])


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("tebbem", False),
        ("aba", True),
        ("abca", True),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            print(case)
            self.assertEqual(case[1], Solution.valid_palindrome(case[0]))
