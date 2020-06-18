"""
https://www.lintcode.com/problem/palindrome-number/
https://leetcode.com/problems/palindrome-number/
"""


def solution(number: int) -> bool:
    """
    遍历一半整数判断相等的算法不太好背诵，边界探秘判断麻烦
    """
    palindromic_number: int = 0
    origin_number: int = number
    while number != 0:
        palindromic_number = palindromic_number * 10 + number % 10
        number //= 10
    return palindromic_number == origin_number
