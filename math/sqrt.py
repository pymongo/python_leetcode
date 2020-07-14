"""
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
number=16
init: guess=16/2=8
guess=(8+16/8)/2=5
guess=(5+16/5)/2=4.001...
// ...
难点在于退出循环的条件
我认为是当前的guess与新的guess相差小于千分之一时就可以break了
"""

import unittest
import random
import math


# 用牛顿连续均值迭代法会比二分法快得多，迭代次数少很多
def my_sqrt(x: int) -> int:
    if x == 0:
        return 0
    # 误差设为1e-5就刚好能在leetcode上AC
    # 如果是lintcode[586. Sqrt(x) II]，把误差调低点就能AC
    accuracy: float = 1e-5
    guess: float = x / 2
    while True:
        new_guess = (guess + x / guess) / 2
        if abs(new_guess - guess) < accuracy:
            break
        guess = new_guess
    return int(guess)


class Testing(unittest.TestCase):
    def test_my_sqrt(self):
        # print(my_sqrt(25))
        for _ in range(100):
            num = random.randint(1, 1000)
            self.assertLessEqual(abs(int(math.sqrt(num)) - my_sqrt(num)), 1e-3)
