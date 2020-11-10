"""
TODO 二分法解决的几类问题
- [x] 有序数组的二分搜索: 34(二分搜索第一个和最后一个), 704(经典二分搜索)
- [x] 山脉数组(mountain array)类问题: 852、(941)、1095
- [x] 旋转排序数组: 33, 81, 153, 154
- [ ] 分割数组的最大值: 410
- [ ] 转变数组后最接近目标值的数组和: 1300
- [x] 平方根: 69(牛顿连续均值求平方根?)
- [ ] 寻找重复数: 287
- [x] 爱吃香蕉的珂珂: 875
"""

import unittest
from copy import deepcopy


def solution(nums, target):
    size = len(nums)
    left, right = 0, size-1
    while left <= right:
        # FIXME 面试官可能会问，(left+right)//2会有什么问题
        # left+right可能会i32/u32溢出，解决办法是写成 middle = start + (end - start) / 2
        # 实际上i32数组如果有2**31个元素，那么要占用4*4G的内存
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle-1
        elif nums[middle] < target:
            left = middle+1
        else:
            return middle
    return -1


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([-1, 1, 2, 2, 2, 3], 2, 2),
    ]

    def test(self):
        # 另一种提高单元测试-测试用例可读性的方法，用namedtuple
        # 例如Point = namedtuple('Point', ['x', 'y']) 会生成一个含有x,y字段的Point类
        for nums, target, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, solution(nums, target))
