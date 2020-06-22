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
        # 给油箱加上出发点的油量
        gas_volume = gas[i]
        # 内层循环遍历len-1次，遍历的是线段而不是端点
        for j in range(1, stations_count):
            next_station = (i+j) % stations_count
            print(next_station)
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
            # will run only if the inner loop is exited normally
            # return if inner loop no break
            return i
    return -1


class Testing(unittest.TestCase):
    TEST_CASES: List[Tuple[List[int], List[int], int]] = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([1, 1, 3, 1], [2, 2, 1, 1], 2),
        ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ]

    def test_brute_force(self):
        for case in self.TEST_CASES[:]:
            self.assertEqual(case[2], brute_force(case[0], case[1]))
