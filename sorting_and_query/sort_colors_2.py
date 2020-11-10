"""
[lintcode only]https://lintcode.com/problem/sort-colors-ii/
1. 快速排序(空间复杂度最优)
传入两个区间，一个是颜色区间 color_from, color_to；另外一个是待排序的数组区间 index_from, index_to
找到颜色区间的中点，将数组范围内进行 partition，<= color 的去左边，>color 的去右边。 然后继续递归
时间复杂度O(nlogk) n是数的个数，k是颜色数目
2. 计数排序(时间复杂度最优)
既然入参中给定了有k种不同的取值，于是可以直接得到计数器数组的长度
计数排序的时间复杂度最优，而且较容易背诵
"""
import unittest
from typing import List


# Your submission beats 99.40% Submissions!
def counting_sort(nums: List[int], k: int):
    # 注意颜色从[1,k]，索引0是无用索引
    counter = [0] * (k + 1)
    for num in nums:
        counter[num] += 1
    # 不能用nums = []，否则nums会shadowing成新的局部变量，不能inplace修改nums指针
    nums.clear()
    for i in range(1, k + 1):
        nums += ([i] * counter[i])


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([3, 2, 2, 1, 4], 4, [1, 2, 2, 3, 4]),
        ([2, 1, 1, 2, 2], 2, [1, 1, 2, 2, 2]),
    ]

    def test(self):
        for nums, k, expected in self.TEST_CASES:
            counting_sort(nums, k)
            print(nums)
            self.assertListEqual(expected, nums)
