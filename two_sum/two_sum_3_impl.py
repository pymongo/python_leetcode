import unittest
# Python binary search的API
import bisect


class TwoSum:
    """
    这题没有唯一正确答案，数据结构设计题面试时，要跟面试官沟通清楚每个方法的调用次数
    用HashMap(key: num, value: num出现次数)辅助数据结构，可以让插入为O(1)，判断为O(n)
    如果add和find调用次数均匀，还是要构思插入的查找都是O(logn)的设计
    但是除了HashMap，没有办法能让线性数据结构插入新元素和查找的时间复杂度都是O(logn)
    BST? BST只有是平衡二叉树才能让所有操作都是logn, BST插入是logn，查询时O(n)
    """
    def __init__(self):
        self.nums = []
        self.length = 0

    def add(self, num: int):
        # 这里用插入排序可能性能更好
        # 二分: logn, 插入元素后往后挪动: O(n)
        bisect.insort(self.nums, num)
        self.length += 1

    def find(self, target: int) -> bool:
        start, end = 0, self.length - 1
        while start < end:
            temp_sum = self.nums[start] + self.nums[end]
            if temp_sum > target:
                end -= 1
            elif temp_sum < target:
                start += 1
            else:
                return True
        return False


class TestTwoSum(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 5], [(4, True), (7, False)]),
    ]

    def test(self):
        for nums, cases in self.TEST_CASES:
            two_sum = TwoSum()
            for num in nums:
                two_sum.add(num)
            for num, expected in cases:
                self.assertEqual(expected, two_sum.find(num))
