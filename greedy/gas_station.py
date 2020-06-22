"""
https://leetcode.com/problems/gas-station/
"""

import unittest
from typing import List, Tuple


def brute_force(gas: List[int], cost: List[int]) -> int:
    gas_volume: int
    station: int
    next_station: int
    stations_count = len(gas)
    for i in range(stations_count):
        gas_volume = 0
        # 内层循环遍历len-1次，遍历的是线段而不是端点
        for j in range(stations_count):
            station = (i + j) % stations_count
            gas_volume += gas[station] - cost[station]
            if gas_volume < 0:
                break
        else:
            # 如果内层for循环break了
            return i
    return -1


def brute_force_wrong_traverse(gas: List[int], cost: List[int]) -> int:
    gas_volume: int
    station: int
    next_station: int
    stations_count = len(gas)
    for i in range(stations_count):
        # 给油箱加上出发点的油量
        # FIXME 遍历顺序不是4->2->5，而是4->1->5->2(简单多了)
        gas_volume = gas[i]
        # 内层循环遍历len-1次，遍历的是线段而不是端点
        for j in range(1, stations_count):
            next_station = (i + j) % stations_count
            # next_station = (i+j)
            # if next_station > stations_count:
            #     next_station -= stations_count
            # 遍历到最后一个(也就是出发点)时，不能重复加两次出发点的油量
            # if next_station == i:
            #     gas_volume -= cost[next_station]
            # else:
            #     gas_volume += gas[next_station] - cost[next_station]
            gas_volume -= cost[next_station]
            if gas_volume < 0:
                break
            gas_volume += gas[next_station]
        else:
            # 如果内层for循环break了
            return i
    return -1


class Testing(unittest.TestCase):
    """
    gas:  [1, 2, 3, 4, 5]
    cost: [3, 4, 5, 1, 2]
    从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
    开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
    开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
    开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
    开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
    开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
    因此，3 可为起始索引。
    【纠错】：遍历顺序不是4->2->5，而是4->1->5->2(简单多了)
    """
    TEST_CASES: List[Tuple[List[int], List[int], int]] = [
        ([2, 3, 4], [3, 4, 3], -1),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([1, 1, 3, 1], [2, 2, 1, 1], 2),
        ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ]

    def test_brute_force(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[2], brute_force(case[0], case[1]))