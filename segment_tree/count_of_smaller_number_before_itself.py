import unittest
from typing import List


class Block:
    def __init__(self):
        self.total = 0
        self.counter = {}


class BlockArray:
    def __init__(self):
        # 最后一个blocks只有10000一个元素
        # FIXME 不能用 [Block()] * 101, 否则不是深拷贝
        self.blocks = [Block() for _ in range(101)]

    def count_smaller(self, value: int) -> int:
        count = 0
        block_index = value // 100

        # 先数在value桶的前面所有桶的元素个数
        for i in range(block_index):
            count += self.blocks[i].total

        block_counter = self.blocks[block_index].counter
        for val in block_counter:
            if val < value:
                count += block_counter[val]
        return count

    def insert(self, value: int):
        block = self.blocks[value // 100]
        block.total += 1
        block.counter[value] = block.counter.get(value, 0) + 1


# 这题推荐用线段树，如果不会可用分块检索
# 类似桶排序/计数排序的分块检索，由于题目限定数字的大小范围是1万以内，于是可以分为根号1万=100个桶
class Solution(unittest.TestCase):
    TEST_CASE = [
        ([1, 2, 7, 8, 5], [0, 1, 2, 3, 2]),
        ([7, 8, 2, 1, 3], [0, 1, 0, 0, 2]),
    ]

    def test(self):
        for nums, expected in self.TEST_CASE:
            self.assertEqual(expected, self.f(nums))

    @staticmethod
    def f(nums: List[int]) -> List[int]:
        if not nums:
            return []

        block_array = BlockArray()
        res = []
        for num in nums:
            res.append(block_array.count_smaller(num))
            block_array.insert(num)
        return res
