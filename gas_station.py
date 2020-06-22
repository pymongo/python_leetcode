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
        for j in range(stations_count):
            station = (i+j) % stations_count
            next_station = (i+j+1) % stations_count
            gas_volume += gas[station]
            gas_volume -= cost[next_station]
            if gas_volume < 0:
                break
        else:
            # will run only if the inner loop is exited normally
            # return if inner loop no break
            return i+1
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
