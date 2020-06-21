import unittest
from typing import List
from mydbg import dbg

def solution(a: List[int], b: List[int]) -> float:
    len_a, len_b = len(a), len(b)
    # 确保A
    if len_a > len_b:
        return solution(b, a)
    # if len_a == 0:
    #     if len_b % 2 == 0:
    #         return (b[len_b // 2 - 1] + b[len_b // 2]) / 2.0
    #     else:
    #         return b[len_b // 2]
    total_len = len_a + len_b
    half_len = (total_len + 1) // 2

    a_left, a_right = 0, len_a
    a_mid_right_index: int
    b_mid_right_index: int
    while a_left < a_right:
        # 如果数组a是奇数个，a_mid_right会是数组a正中间的元素
        # a_mid_right_index = (a_left + a_right + 1) // 2 #  会陷入死循环的二分法
        a_mid_right_index = a_left + (a_right - a_left) // 2
        b_mid_right_index = half_len - a_mid_right_index
        # 如果a分隔线右边的元素比b分隔线左边的元素小
        if a[a_mid_right_index] < b[b_mid_right_index - 1]:
            # a分隔线左边元素太小了，a的分隔线需要右移
            a_left = a_mid_right_index + 1
        else:
            # a分隔线左边元素太大了，a的分隔线需要左移
            a_right = a_mid_right_index
    # 跳出二分法的循环后需要再次更新分隔线的位置
    a_mid_right_index = a_left
    b_mid_right_index = half_len - a_mid_right_index

    a_mid_left = (a[a_mid_right_index - 1] if a_mid_right_index >= 1 else float("-inf"))
    b_mid_left = (b[b_mid_right_index - 1] if b_mid_right_index >= 1 else float("-inf"))
    dbg((a_mid_left, b_mid_left))
    if total_len % 2 == 1:
        return max(a_mid_left, b_mid_left)
    a_mid_right = (a[a_mid_right_index] if a_mid_right_index < len_a else float("inf"))
    b_mid_right = (b[b_mid_right_index] if b_mid_right_index < len_b else float("inf"))
    return (max(a_mid_left, b_mid_left) + min(a_mid_right, b_mid_right)) / 2


class Test(unittest.TestCase):
    TEST_CASES = [
        ([1, 2, 3, 4], [3, 6, 8, 9], 3.5),
        ([1, 5, 6, 7], [2, 3, 4, 8], 4.5),
        ([1, 2], [3, 4, 5, 6, 7], 4),
        ([4, 5, 6], [1, 2, 3], 3.5),
        ([4, 5], [1, 2, 3, 6], 3.5),
        ([1, 3], [2, 4, 5, 6], 3.5),
        ([1, 2], [3, 4, 5, 6], 3.5),
        ([1, 3], [2, 4, 5], 3),
        ([1, 2, 3], [4, 5], 3),
        ([3, 4], [1, 2, 5], 3),
        ([-2, -1], [3], -1),
        ([1, 3], [2], 2),
        ([3], [-2, -1], -1),
        ([1, 2], [3, 4], 2.5),
        ([4, 5], [1, 2, 3], 3),
        ([1, 2], [1, 2, 3], 2),
        ([1, 2, 3], [1, 2, 3], 2),
    ]

    def test(self):
        for case in self.TEST_CASES[:]:
            print(case)
            self.assertEqual(case[2], solution(case[0], case[1]))
