"""
https://leetcode.com/problems/implement-strstr/
"""
import unittest
from typing import List, Tuple


def kmp_compute_longest_prefix_suffix(target: str) -> List[int]:
    # FIXME 错误的KMP前缀pattern计算方法，KMP有点烧脑，为了节约时间还是用别的算法
    left_ptr: int
    size = len(target)
    lps = [0 for _ in range(size)]
    for right_prt in range(size):
        left_ptr = 0
        while left_ptr < right_prt:
            # 不能用回文数的比较思想
            if target[left_ptr] == target[right_prt]:
                lps[left_ptr] += 1
                left_ptr += 1
                right_prt -= 1
            else:
                break
    return lps


# def kmp_search(source: str, target: str) -> int:
#     return -1


# 我更喜欢将rabin_karp称为: rolling hash
# 可是rolling_hash也太慢了，在rotate_string一题上rolling_hash比`a in b`的语句还要慢，还是得学KMP
def rabin_karp(source: str, target: str) -> int:
    """
    优化思路：通过将字符串转换为整数，使字符串的比较相等从O(n)时间复杂度降低到O(1)
        怎么才能将字符串转换为整数呢？其中一个思路就是计算哈希值
        例如hash("abc") = ord('a')*31^0 + ord('b')*31^1 + ord('c')*31^2
        为什么基数选用31呢？这是业界的经验之谈，效率和性能较好
        避免整数溢出：将hash的计算结果%(10^12)，存在冲突的可能性几乎为0
    按照上述思路，在source中往右移动比较字符串窗口时，例如abcd从abc移到bcd，只需将a的权重减掉，再加上d的权重
    """
    if source is None or target is None:
        return -1
    target_len: int = len(target)
    source_len: int = len(source)
    if target_len == 0:
        return 0
    if target_len > source_len:
        return -1
    # if source == 199999 and source[999] == 'a':
    # base value for hash rolling hash function
    # BASE取26或31都行，只要保证BASE和MODULES的组合不会出现hash crash现象就行
    BASE: int = 26
    # modules value for rolling hash function to avoid overflow
    MODULES: int = 10 ** 5
    # 假设字符串中没有大写字母，所以ord(x)-ord('a')不会是负数
    CHAR_OFFSET: int = ord('a')

    # compute the hash of target
    # and init the hash of source
    target_hash: int = 0
    source_hash: int = 0
    for i in range(target_len):
        # 一边乘一边取模，保证不会越界
        # 过程类似取出整数每位的逆过程
        # 结果是target[0]的指数为31的(target_len-1)次方
        target_hash = (target_hash * BASE + ord(target[i]) - CHAR_OFFSET) % MODULES
        source_hash = (source_hash * BASE + ord(source[i]) - CHAR_OFFSET) % MODULES

    if source_hash == target_hash:
        return 0

    # sliding window traverse source
    for i in range(source_len - target_len):
        # abc + d
        source_hash = (source_hash * BASE + ord(source[i + target_len]) - CHAR_OFFSET) % MODULES
        # abcd - a，经过上面一次移位，a的系数应该是BASE ** (target_len-1)+1
        source_hash = source_hash - (ord(source[i]) - CHAR_OFFSET) * (BASE ** target_len) % MODULES
        if source_hash < 0:
            source_hash += MODULES
        if source_hash == target_hash:
            # TODO double check substr
            return i + 1
    return -1


class Testing(unittest.TestCase):
    TEST_CASE: List[Tuple[str, str, int]] = [
        ("abcdef", "bcd", 1),
        ("abcde", "e", 4),
        ("any", "", 0),
    ]

    def test_rabin_karp(self):
        for source, target, expected in self.TEST_CASE[:]:
            self.assertEqual(expected, rabin_karp(source, target))

    KMP_LPS_TEST_CASES: List[Tuple[str, List[str]]] = [
        ("ABCDABD", [0, 0, 0, 0, 1, 2, 0])
    ]

    def test_kmp_lps(self):
        for pattern, expected in self.KMP_LPS_TEST_CASES[:]:
            self.assertEqual(expected, kmp_compute_longest_prefix_suffix(pattern))
