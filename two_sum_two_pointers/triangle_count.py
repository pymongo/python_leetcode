"""
https://lintcode.com/problem/triangle-count/description?_from=ladder&&fromId=161
输入一个排序数组，请问从数组中取3个值能组成多少个不同的三角形
由于数组是有序的，满足nums[a] + nums[b] > nums[c]即可，转换成两数之和大于类型问题
这题有点像three sum，和三数之和类似，遍历时可变的双指针要在等式的左边，而固定不变的target放等式右边
如果本题固定a，双指针是b和c，那么一定会出现漏掉解的情况，所以等式右边的target不能是可变的
"""

import unittest
from typing import List


# 根据排列组合C(n,3), 本题正常遍历需要O(n^3)的时间复杂度
# 由于求的是方案总数，而不是具体方案，所以时间复杂度降低到O(n^2)
# 在数方案总数的问题上，一定要批量批量的数，否则会超时
# 字节跳动有一题是数大矩阵中0和1随机分布，问3x3全是1的矩阵有几个，也是要批量数
def triangle_count(nums: List[int]) -> int:
    nums = sorted(nums)
    size = len(nums)
    if size < 3:
        return 0
    count = 0
    # target就是最长边c，固定等式右边的不变
    for c in range(2, size):
        a, b = 0, c - 1
        while a < b:
            if nums[a] + nums[b] > nums[c]:
                # [3,4,6,7]中如果a(3) + b(6) > c(7)，那么a右移一位的解4,6,7也满足条件
                # 这步是不会漏掉解的关键，参考two-sum-less-than-or-equal-to-target
                # 既然nums[left]+nums[right]>target，那么[left..right-1, right]的解都满足条件
                # count会算上固定b之后[a..b-1, b]的所有解，然后b-=1; 而two_sum_le一题是固定a之后[a,a+1..b]所有解，所以a+=1
                count = count + (b - a)
                b -= 1
            else:
                # 不会重复计算4,6,7这个解两次，因为4,6,7被记入时，b左移一位，已经退出循环，可以代入一些很小的用例去推敲
                a += 1
    return count


class Testing(unittest.TestCase):
    TEST_CASES = [
        # (3,4,6), (3,6,7), (4,6,7)
        ([3, 4, 6, 7], 3),
        ([4, 4, 4, 4], 4),
    ]

    def test_triangle_count(self):
        for nums, expected in self.TEST_CASES:
            self.assertEqual(expected, triangle_count(nums))
