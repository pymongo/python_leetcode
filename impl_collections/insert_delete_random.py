import random


# https://www.lintcode.com/problem/insert-delete-getrandom-o1/
# TODO 这题的解答并不好
class RandomizedSet:

    def __init__(self):
        self.len = 0
        self.nums = []
        self.set = set()

    def insert(self, val: int):
        if val in self.set:
            return
        self.nums.append(val)
        self.set.add(val)
        self.len += 1

    def remove(self, val):
        if val not in self.set:
            return
        self.nums.remove(val)
        # set还有一个discard API如果key不存在就Do nothing，不会报错
        self.set.remove(val)
        self.len -= 1

    # noinspection PyPep8Naming
    def getRandom(self) -> int:
        # 随机返回一个数这里用系统库有点作弊啊，还是了解下生成随机数算法更好
        return self.nums[random.randint(0, self.len - 1)]
