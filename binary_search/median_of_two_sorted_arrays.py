"""
两个排序数组的中位数，题目要求用O(logn)时间复杂度。常见的时间复杂度有：
从时间复杂度推算法
复杂度	可能对应的语法	备注
O(1)	位运算	常数级复杂度，一般面试中不会有
O(logn)	二分法，倍增法，快速幂算法，辗转相除法
O(sqrt(n)) 分解质因数
O(n)	枚举法，双指针算法，单调栈算法，KMP算法，Rabin Karp，Manacher's Algorithm	又称作线性时间复杂度
O(nlogn)快速排序，归并排序，堆排序
O(n^2)	枚举法，动态规划，Dijkstra
O(n^3)	枚举法，动态规划，Floyd
O(2^n)	与组合有关的搜索问题
O(n!)	与排列有关的搜索问题
"""
import unittest
import sys
from typing import List


class Solution(unittest.TestCase):
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

    def test_recursive_solution(self):
        for nums_a, nums_b, expected in self.TEST_CASES[:]:
            print(nums_a, nums_b)
            self.assertEqual(expected, self.recursive_solution(nums_a, nums_b))

    # noinspection PyPep8Naming
    @staticmethod
    def recursive_solution(A: List[int], B: List[int]) -> float:
        # 第一次从A或B中排除掉k//2，第二次排除掉k-k//2 ...
        len_a, len_b = len(A), len(B)
        len_total = len_a + len_b

        def find_kth(a_start: int, b_start: int, k: int) -> int:
            # 细节1. 递归结束条件
            if a_start >= len_a:
                # 如果a数组为空，则返回B数组第k项，这里的异常处理比分隔线解法简单多了
                return B[b_start + k - 1]
            elif b_start >= len_b:
                return A[a_start + k - 1]
            if k == 1:
                return min(A[a_start], B[b_start])

            # 细节2. 可以理解成A和B数组后面都是无穷大的值
            # 这样的话如果a较短(a_start+k//2-1)在数组外，那么不能排除掉a，因为a的数量不够多「不够数」，只能去排除b，所以让a_2_k设为无穷大转而去排除b
            a_2_k = A[a_start + k // 2 - 1] if a_start + k // 2 - 1 < len_a else sys.maxsize
            # TODO 细节3. a和b有可能同时都是无穷大吗?
            b_2_k = B[b_start + k // 2 - 1] if b_start + k // 2 - 1 < len_b else sys.maxsize
            if a_2_k > b_2_k:
                # 排除掉较小的b前k//2个数，最后一个数的下标是k//2-1，所以下一个b_start是k//2
                return find_kth(a_start, b_start + k // 2, k - k // 2)
            else:
                # FIXME 细节4. 请你思考下为什么一定要写成k-k//2不能写成k//2(因为是排除了地板除k//2个数)
                return find_kth(a_start + k // 2, b_start, k - k // 2)

        if len_total % 2 == 1:
            # FIXME 细节5. 注意第k个数是一位数组中位数的下标再加1
            return find_kth(0, 0, len_total // 2 + 1)
        else:
            # 细节6. 虽然递归找kth的算法在偶数情况下会有重复计算，但是代码量/可读性/理解难度/异常情况处理都优于分隔线版本
            return (find_kth(0, 0, len_total // 2) + find_kth(0, 0, len_total // 2 + 1)) / 2

    def test_divider_solution(self):
        for nums1, nums2, expected in self.TEST_CASES[:]:
            self.assertEqual(expected, self.divider_solution(nums1, nums2))

    # Runtime: 92 ms, faster than 83.80%
    @staticmethod
    def divider_solution(a: List[int], b: List[int]) -> float:
        # 该解法的缺点是不如递归求kth那样通用，这种分隔线的思想只能解决一类问题，而kth的思想能解决多种问题
        len_a, len_b = len(a), len(b)
        # 确保a是较短的数组
        if len_a > len_b:
            return Solution.divider_solution(b, a)
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
        if total_len % 2 == 1:
            return max(a_mid_left, b_mid_left)
        a_mid_right = (a[a_mid_right_index] if a_mid_right_index < len_a else float("inf"))
        b_mid_right = (b[b_mid_right_index] if b_mid_right_index < len_b else float("inf"))
        return (max(a_mid_left, b_mid_left) + min(a_mid_right, b_mid_right)) / 2
