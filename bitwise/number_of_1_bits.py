"""
Rust: n.count_ones()
Java: Integer.bitCount(n)
Python: bin(n).count('1')

类似的颠倒整数的二进制可以用: Integer.reverse(n)
"""


# 数位1的个数也叫hammingWeight
def count_ones_by_mask(n: int) -> int:
    cnt = 0
    # mask只有一位是1，不断左移唯一的一位1
    mask = 1
    for _ in range(32):
        if n & mask != 0:
            cnt += 1
        mask <<= 1
    return cnt


def best_count_ones(n: int) -> int:
    cnt = 0
    while n != 0:
        # 利用is_power_of_2一题相同的位运算规律—— n&(n-1)能去掉最右边的1
        n = n & (n - 1)
        cnt += 1
    return cnt


class Solution:
    @staticmethod
    def hamming_distance(x: int, y: int) -> int:
        """
        两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
        思路: 异或后数位1的个数
        注意汉明距离总和一题，两两去算一定超时
        sum(map(lambda each: best_count_ones(each[0]^each[1]), itertools.combinations(nums, 2)))
        """
        return bin(x ^ y).count('1')
