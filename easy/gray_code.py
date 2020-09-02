"""
《数字信号处理》—— 镜像反射法生成格雷码:
0 0|0 0|00
  1|0 0|10
      1|10
      1|00
先将上次迭代的结果「上下镜像复制」一份，第一份在左侧加上1，另一部分在左侧加上0
这样能保证格雷码的要求: 从上到下仅有1bit的变化
如果懂了这些背景知识，那么这题就是easy难度了，首先左侧补0的那一半可以不做(二进制左侧加0等于不变)，因为原数组各项+0后还是原数组
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    def test(self):
        print(Solution.gray_code(3))

    @staticmethod
    def gray_code(n: int) -> List[int]:
        # 镜像反射法生成格雷码的技巧，左侧要补1的镜像部分的个数刚好等于head，而且
        res, head = [0], 1
        for _ in range(n):
            for i in range(head - 1, -1, -1):
                res.append(head + res[i])
            head *= 2
        return res
