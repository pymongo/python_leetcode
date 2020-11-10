import unittest
from typing import List


# 按指定长度去切，最多能切成几份
def get_max_cut_quantity(nums: List[int], wood_len: int) -> int:
    if wood_len == 0:
        return 0
    cut_count = 0
    for wood in nums:
        cut_count += wood // wood_len
    return cut_count


def solution(nums: List[int], k: int) -> int:
    """
    一堆木头切成「等长」k份(假设是无损切割)，请问每份的最长长度是多少
    本题属于缩小答案集的二分搜索
    那么最大长度的边界要如何算出？取最短木头的长度？不行，最短木头可以不参与切割
    可以认为木头堆中最长的木头是能切长度的最大值
    本题的二分比较特殊，start和end不是数组的下标，而且切木头的长度
    时间复杂度: nlog(max(nums))
    """
    if not nums:
        return 0
    max_cut_len = max(nums)
    start, end = 0, max_cut_len
    while start + 1 < end:
        # start, mid, end指的都是木头长度
        mid = start + (end - start) // 2
        mid_cut_count = get_max_cut_quantity(nums, mid)
        if mid_cut_count < k:
            # 切的长度过长了，导致切不到k份
            end = mid - 1
        else:
            start = mid

    if get_max_cut_quantity(nums, end) >= k:
        return end
    if get_max_cut_quantity(nums, start) >= k:
        return start
    return 0


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([232, 124, 456], 7, 114),
        ([1, 2, 3], 7, 0),
    ]

    def test_solution(self):
        for nums, k, expected in self.TEST_CASES:
            self.assertEqual(expected, solution(nums, k))
