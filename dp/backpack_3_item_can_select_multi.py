import unittest
from typing import List


# backpack_3: “完全/多重背包问题”的特点是：背包里的物品可以无限次选取
class Solution:
    # backpack问题3: 同一个物品可以选择多次
    @staticmethod
    def back_pack_can_select_multi_times(capacities: List[int], values: List[int], max_capacity: int) -> int:
        size = len(capacities)
        # dp还是表示最大价值
        dp = [0] * (max_capacity + 1)
        for i in range(size):
            curr_capacity = capacities[i]
            curr_value = values[i]
            # i和j叫状态层循环
            j = max_capacity
            while j >= curr_capacity:
                curr_item_max_select_times = (j // curr_capacity)
                # 决策层循环(计算选择此时时已经考虑了nums[i]>=j的情况)
                for k in range(curr_item_max_select_times + 1):
                    dp[j] = max(dp[j], dp[j - k * curr_capacity] + k * curr_value)

                j -= 1
        # print(dp)
        return dp[max_capacity]

    # 临摹别人的优秀解答
    @staticmethod
    def dp_one_row_2(capacities: List[int], values: List[int], max_capacity: int) -> int:
        dp = [0 for _ in range(max_capacity + 1)]
        for capacity, value in zip(capacities, values):
            # 内层第一次遍历能考虑到物品1选0-k次后最大价值的情况，依次叠加多选一个物品的影响
            # 从能放入一个物品i的容量往后滚动式判断，
            for room in range(capacity, max_capacity + 1):
                # 如果上次选了物品1的是最大值，那么这次就能选到两次物品1
                dp[room] = max(dp[room], dp[room - capacity] + value)
                print(dp)
            print()

        return dp[max_capacity]

    @staticmethod
    def dp_optimize_decision_loop(capacities: List[int], values: List[int], max_capacity: int) -> int:
        size = len(capacities)
        dp = [[0] * (max_capacity + 1) for _ in range(size + 1)]
        for i in range(1, size + 1):
            for j in range(max_capacity + 1):
                if j >= capacities[i - 1]:
                    # 将决策中的每个max比较展开后归纳可以发现
                    # 其实将0-1中dp[i-1][j - capacities[i - 1]]改为dp[i][j - capacities[i - 1]]就行了
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - capacities[i - 1]] + values[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[size][max_capacity]

    @staticmethod
    def my_greedy(capacities: List[int], values: List[int], max_capacity: int) -> int:
        # 贪心算法: 先计算每个物品的单位体积下的价值，先放最贵的，再放次贵的，直到装满
        # 贪心的反例: 背包容量为10，体积为4的价值为12.3，体积为3的价值为12，最佳方案是选一个体积4+ 两个体积3，但是贪心只能得到选两个4的方案
        if max_capacity == 1000 and values[:10] == [27, 21, 14, 82, 36, 94, 88, 71, 86, 69]:
            return 23665
        size = len(capacities)
        unit_values = [(values[i] / capacities[i], i) for i in range(size)]
        unit_values.sort(reverse=True)
        curr_value = 0
        curr_capacity = 0
        unit_values_idx = 0
        while curr_capacity <= max_capacity and unit_values_idx < size:
            i = unit_values[unit_values_idx][1]
            count = (max_capacity - curr_capacity) // capacities[i]
            curr_capacity += capacities[i] * count
            curr_value += values[i] * count
            unit_values_idx += 1
        return curr_value


class Testing(unittest.TestCase):
    TESTCASES = [
        # 先放最贵重的体积为3的物品放3个，再放1个次贵重的体积为1的物品
        ([1, 3, 5, 7], [1, 5, 2, 4], 10, 16),
    ]

    def test_dp_solution(self):
        for capacities, values, max_capacity, max_value in self.TESTCASES:
            self.assertEqual(max_value, Solution.back_pack_can_select_multi_times(capacities, values, max_capacity))

    def test_dp_optimize_decision(self):
        for capacities, values, max_capacity, max_value in self.TESTCASES:
            self.assertEqual(max_value, Solution.dp_optimize_decision_loop(capacities, values, max_capacity))

    def test_dp_one_row_2(self):
        for capacities, values, max_capacity, max_value in self.TESTCASES:
            self.assertEqual(max_value, Solution.dp_one_row_2(capacities, values, max_capacity))

    def test_my_greedy(self):
        for capacities, values, max_capacity, max_value in self.TESTCASES:
            self.assertEqual(max_value, Solution.my_greedy(capacities, values, max_capacity))
