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
    visited_size: int,
    curr_distance: int,  # current city
    curr_city: int,
    graph: List[List[int]],
    size: int,
    min_distance: MinDistance,
):
    """
    这题剪枝(pruning)跟word-search-ii这题剪枝处理有点相似
    word-search-ii找到一个单词之后，从前缀树的叶子往上一直✂️到根
    而这题是搜索到一条路径之后，也是往上不断✂️到根
    """
    # if all True in visited
    # if all(visited):
    #     min_distance.update(curr_distance)
    #     return
    if visited_size == size:
        min_distance.update(curr_distance)
        return

    for next_city in range(1, size):
        if visited[next_city]:
            continue
        distance = graph[curr_city][next_city]
        if distance == sys.maxsize:
            continue

        # Early Return 部分
        next_distance = curr_distance + distance
        if next_distance >= min_distance.value:
            continue

        visited[next_city] = True

        dfs(visited, visited_size+1, next_distance, next_city, graph, size, min_distance)

        visited[next_city] = False


# 101ms, 97.5%
def dfs_helper(n: int, roads: List[List[int]]) -> int:
    # 图的设计方案1: 评价: 这种图还不如邻接矩阵
    # 将[[1, 2, 1], [2, 3, 2], [1, 3, 3]]的roads转为HashMap
    # FIXME 这是「有向图」{ 1: {2: 1, 3: 3}, 2: {3: 2} } 题目要求「无向图」
    # 结果: 还是用邻接矩阵
    if not roads:
        return 0
    adjacency_matrix: List[List[int]] = [[sys.maxsize] * n for _ in range(n)]
    for from_city, to_city, distance in roads:
        from_city, to_city = from_city - 1, to_city - 1
        adjacency_matrix[from_city][to_city] = min(adjacency_matrix[from_city][to_city], distance)
        adjacency_matrix[to_city][from_city] = min(adjacency_matrix[to_city][from_city], distance)

    # 既然入参中已给出城市的个数，那么用布尔值表示城市/节点是否被访问过更优
    # 用all(visited)判断是否遍历完所有节点
    visited: List[bool] = [False] * n
    visited[0] = True

    min_distance = MinDistance()
    dfs(visited=visited, visited_size=1, curr_distance=0, curr_city=0, graph=adjacency_matrix, size=n,
        min_distance=min_distance)
    return min_distance.output()


class Testing(unittest.TestCase):
    TEST_CASES = [
        # 解释: cost一定是个三元组组成的List，例如[1,2,1]表示从城市1到城市2耗费1
        # 注意: 可能会有重复的路径，例如城市1到城市2有多条路，取最短的一条即可
        # 1->3: 0+2
        # 3->2: 2+1
        # 2->4: 3+3
        # 4->5: 6+4
        (5, [[1, 2, 9], [2, 3, 1], [3, 4, 9], [4, 5, 4], [2, 4, 3], [1, 3, 2], [5, 4, 9]], 10),
        (3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]], 3),
    ]

    def test_dfs(self):
        for num_cities, roads, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, dfs_helper(num_cities, roads))
