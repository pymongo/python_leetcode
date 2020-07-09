"""
https://leetcode.com/problems/rotate-array/
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: nums数组向右循环移位 3位

原地换位(In place)算法主要有两种:
1. 环状替换
   参考学生时代换座位时，A同学要换到D同学的位置上，先把D同学移出教室(temp)，再将A同学移到D同学的位置上
   以此类推，重复上述过程N次。向右移位k次后的`new_index=(old_index+k)%len`
   参考: https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-yuan-di-huan-wei-xiang-xi-tu-jie/
2. 借助反转的数学原理
   向右移k位等于整个数组reverse后，nums[0:k]和nums[k+1:len]再reverse一次
   另一个利用反转的应用是
   反转句子中的单词:
   例如: I love you -> you love I
   "I love you" -> ouy evol I -> you love I
"""

import unittest
from typing import List


def right_circle_shift(nums: List[int], k: int):
    pass


class UnitTest(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100])
    ]

    def test(self):
        for nums, k, expected in self.TEST_CASES:
            right_circle_shift(nums, k)
            self.assertEqual(expected, nums)
