import unittest
import random


# https://lintcode.com/problem/insert-delete-getrandom-o1/
# TODO 这题的解答并不好
class RandomizedSet:

    def __init__(self):
        self.len = 0
        self.nums = []
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.nums.append(val)
        self.set.add(val)
        self.len += 1
        return True

    def remove(self, val) -> bool:
        if val not in self.set:
            return False
        self.nums.remove(val)
        # set还有一个discard API如果key不存在就Do nothing，不会报错
        self.set.remove(val)
        self.len -= 1
        return True

    # noinspection PyPep8Naming
    def getRandom(self) -> int:
        # 随机返回一个数这里用系统库有点作弊啊，还是了解下生成随机数算法更好
        # 主要是面试时不够时间写随机算法函数
        # return random.choice(self.num)
        return self.nums[random.randint(0, self.len - 1)]


class RandomizedCollection:
    def __init__(self):
        self.len = 0
        self.nums = []
        # 每个值出现了几次
        self.counter = dict()

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.len += 1
        return_val = val not in self.counter
        self.counter[val] = self.counter.get(val, 0) + 1
        return return_val

    def remove(self, val) -> bool:
        if val not in self.counter:
            return False
        if self.counter[val] == 1:
            self.counter.pop(val)
        else:
            self.counter[val] -= 1
        self.len -= 1
        self.nums.remove(val)
        return True

    # noinspection PyPep8Naming
    def getRandom(self) -> int:
        # return random.choice(self.num)
        return self.nums[random.randint(0, self.len - 1)]


class Testing(unittest.TestCase):
    def test_insert_duplicates_numbers(self):
        obj = RandomizedCollection()
        obj.insert(1)
        obj.insert(1)
        obj.remove(1)
        obj.getRandom()

    def test_insert_2(self):
        obj = RandomizedCollection()
        obj.insert(4)
        obj.insert(3)
        obj.insert(4)
        obj.insert(2)
        obj.insert(4)