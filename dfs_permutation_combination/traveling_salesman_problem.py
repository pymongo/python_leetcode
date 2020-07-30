"""
## 什么是NP问题
P是多项式英文的缩写，NP问题表示不能用多项式级别的时间复杂度解决的问题
著名的NP问题就是本题(英文缩写为TSP)
本题可以抽象为从起点1开始，经过所有点1次仅一次，遍历所有图中所有节点的最短路径是什么
TSP也叫「最短哈密尔顿路径问题」

## 欧拉路径问题(类似七桥问题/一笔画?)
遍历图中所有边一次且仅一次叫「欧拉路径问题」
欧拉路径是一个P问题

## 暴力DFS(排列搜索) + 最优性剪枝(pruning)

## TODO 最优解法: 状态压缩性动态规划

时间复杂度从n!降低到2^n

## 随机化算法: 使用交换/反转调整策略

随机化(Randomization)算法又称遗传算法、模拟退火算法(Simulated Annealing)

类似最长回文子串，这题也是一题涵盖5-6种解法，既有构建图也有动态规划最短路径等等，属于必刷的经典题
"""
import unittest
from copy import deepcopy
from typing import List, Dict, Union
import sys


# Python没有指针，所以定义一个类实现最短路径的引用传递，反正你用[0]也是占48个字节
class MinDistance:
    def __init__(self):
        self.value = sys.maxsize

    def update(self, distance: int):
        self.value = min(self.value, distance)

    def output(self) -> int:
        if self.value == sys.maxsize:
            return 0
        else:
            return self.value


# 只遍历图中的每个节点1次，用贪心的思考方式，如果有节点遍历超过2次，那就一定不是最短路径的遍历了
def dfs(
    visited: List[bool],
    sum_distance: int,  # current city
    last_city: int,
    curr_city: int,
    # graph: Dict[int, Dict[int, Dict[int, int]]],
    graph,
    min_distance: MinDistance,
):
    """
    这题剪枝(pruning)跟word-search-ii这题剪枝处理有点相似
    word-search-ii找到一个单词之后，从前缀树的叶子往上一直✂️到根
    而这题是搜索到一条路径之后，也是往上不断✂️到根
    """
    # if all True in visited
    if all(visited):
        # 剪枝
        # RuntimeError: dictionary changed size during iteration
        # graph[last_city].pop(curr_city)
        min_distance.update(sum_distance)
        return

    for next_city in graph[curr_city]:
        if visited[next_city]:
            continue
        visited[next_city] = True

        dfs(visited, sum_distance + graph[curr_city][next_city], curr_city, next_city, graph, min_distance)

        visited[next_city] = False


def dfs_helper(n: int, roads: List[List[int]]) -> int:
    # 1. 构建图
    # 将[[1, 2, 1], [2, 3, 2], [1, 3, 3]]的roads转为HashMap<int(from_city), HashMap<int(to_city), int(distance)>>
    # { 1: {2: 1, 3: 3}, 2: {3: 2} }
    if not roads:
        return 0
    graph: Dict[int, Dict[int, Dict[int, int]]] = {}
    for from_city, to_city, distance in roads:
        if from_city not in graph:
            graph[from_city] = {to_city: distance}
            continue
        if to_city in graph[from_city]:
            graph[from_city][to_city] = min(graph[from_city][to_city], distance)
    # 既然入参中已给出城市的个数，那么用布尔值表示城市/节点是否被访问过更优

    # any(iterable) Return True if bool(x) is True for any x in the iterable
    # 用all(visited)判断是否遍历完所有节点
    visited: List[bool] = [False] * (n + 1)
    visited[0] = True
    visited[1] = True

    min_distance = MinDistance()
    dfs(visited, 0, 1, 1, graph, min_distance)
    return min_distance.output()


class Testing(unittest.TestCase):
    TEST_CASES = [
        # 解释: cost一定是个三元组组成的List，例如[1,2,1]表示从城市1到城市2耗费1
        # 注意: 可能会有重复的路径，例如城市1到城市2有多条路，取最短的一条即可
        (3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]], 3),
    ]

    def test_dfs(self):
        for num_cities, roads, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, dfs_helper(num_cities, roads))
