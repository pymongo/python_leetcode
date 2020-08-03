import unittest
from typing import List, Dict


# nums是一个长度为2n+1的的数组，有其中一个元素出现了一次，其余元素都是出现了两次，请您返回出现一次的元素的值
# 要求: 时间复杂度O(n)，空间复杂度O(1)
# 正常思路(两遍哈希): 用HashMap<Integer, Integer>记录出现个数，第二次遍历哈希找到出现个数为1的
def find_single_1(nums: List[int]) -> int:
    occur_times: Dict[int, int] = dict()
    for num in nums:
        occur_times[num] = occur_times.get(num, 0) + 1
    for num, times in occur_times.items():
        if times == 1:
            return num


# 遍历一遍哈希表的解法
# 利用数学运算规律: (A + B + A) * 2 - (A + B) = B
def find_single_2(nums: List[int]) -> int:
    return sum(set(nums)) * 2 - sum(nums)


# 利用异或规律: A^B^A = A^A^B = 0^B = B
def find_single_3(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([1, 3, 1, -1, 3], -1),
        ([4, 1, 2, 1, 2], 4),
        ([2, 2, 1], 1),
    ]

    def test_find_single_1(self):
        for nums, single in self.TEST_CASES:
            self.assertEqual(single, find_single_1(nums))

    def test_find_single_2(self):
        for nums, single in self.TEST_CASES:
            self.assertEqual(single, find_single_2(nums))

    def test_find_single_3(self):
        for nums, single in self.TEST_CASES:
            self.assertEqual(single, find_single_3(nums))
