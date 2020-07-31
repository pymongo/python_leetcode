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
    # 既然入参中已给出城市的个数，那么用布尔值表示城市/节点是否被访问过更优
    # 用all(visited)判断是否遍历完所有节点
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
        # 另一种剪枝方案：
        # curr_path = [1->2->3->4], next_city=5
        # for i in 2..4: if [1->2->4->3->5] < [1->2->3->4->5]: 说明当前路径不是最优解，抛弃掉next_city(continue)
        # 枚举走过的点，判断 边 4->5 + 2->3 是否小于 2->4 + 3->5
        next_distance = curr_distance + distance
        if next_distance >= min_distance.value:
            continue

        visited[next_city] = True

        dfs(visited, visited_size + 1, next_distance, next_city, graph, size, min_distance)

        visited[next_city] = False


# 101ms, 97.5%
# noinspection DuplicatedCode
def dfs_helper(n: int, roads: List[List[int]]) -> int:
    # 图的设计方案1: 评价: 这种图还不如邻接矩阵
    # 将[[1, 2, 1], [2, 3, 2], [1, 3, 3]]的roads转为HashMap
    # FIXME 这是「有向图」{ 1: {2: 1, 3: 3}, 2: {3: 2} } 题目要求「无向图」
    # 结果: 还是用邻接矩阵
    if not roads:
        return 0
    visited: List[bool] = []
    adjacency_matrix: List[List[int]] = []
    for _ in range(n):
        adjacency_matrix.append([sys.maxsize] * n)
        visited.append(False)
    visited[0] = True
    for from_city, to_city, distance in roads:
        from_city, to_city = from_city - 1, to_city - 1
        adjacency_matrix[from_city][to_city] = min(adjacency_matrix[from_city][to_city], distance)
        adjacency_matrix[to_city][from_city] = min(adjacency_matrix[to_city][from_city], distance)

    min_distance = MinDistance()
    dfs(visited=visited, visited_size=1, curr_distance=0, curr_city=0, graph=adjacency_matrix, size=n,
        min_distance=min_distance)
    return min_distance.output()


# noinspection DuplicatedCode
def dp_solution(n: int, roads: List[List[int]]) -> int:
    if not roads:
        return 0
    # 也就是所有城市全被访问过的二进制值，长度为2**n, 最后一个索引为2**n-1
    state_size = 1 << n
    dp: List[List[int]] = [[sys.maxsize] * n for _ in range(state_size)]
    adjacency_matrix: List[List[int]] = [[sys.maxsize] * n for _ in range(n)]
    # TODO 状态压缩DP的特点: 使用足够长二进制表示状态
    # dp的优化思路，不关心先后顺序，只关心每个节点是否访问了一次
    # dp[state][city]=distance；city表示到达城市后，state表示之前访问过哪些城市，
    # 例如二进制10101(从右往左倒着看)表示1，3，5城市已被访问过
    # 二进制的(从右往左)第n位表示city_n是否被遍历
    # 既然状态表示已确定，那么状态转移也容易推导出来
    for from_city, to_city, distance in roads:
        from_city, to_city = from_city - 1, to_city - 1
        adjacency_matrix[from_city][to_city] = min(adjacency_matrix[from_city][to_city], distance)
        adjacency_matrix[to_city][from_city] = min(adjacency_matrix[to_city][from_city], distance)
    # dp初始值
    # 1. dp[0][0..=n-1] 是冗余列，不考虑所有城市都没访问的状态
    # 2. dp[0..2^n-1][0] 是冗余列，不能含有到达城市是1的状态，因为1是出发点
    # 2. dp[城市1已被遍历][到达城市1] = 0
    dp[1][0] = 0
    # 开始填表了
    # dp的状态转移方程
    # last_state = state ^ (1 << city)
    # dp[state][city] = min(dp[state][city], dp[last_state][city] + adjacency_matrix[j?][city])
    for state in range(state_size):
        # 如果state只有一位是1
        if (state & -state) == state:
            continue
        for city in range(1, n):
            # print(state, city)
            city_bit = 1 << city
            # 如果当前状态state和 xxx 没有公共部分，例如0b1011和2**2
            # 也就是当前状态 不包含city 或 只包含city，那一定找不到子状态last_state的，可以pass掉
            if state & city_bit == 0:
                continue

            # 以city=2为例，0b0101 ^ 2**2 = 0b0001, last_state里刚好把现在city给去掉了
            last_state = state ^ city_bit

            # for visited city in last state
            # 这步的目的: 遍历last_state中所有城市(city2)，找到能连上city的所有city2中的最短路径
            # 所以这步操作就跟DFS剪枝的过程有点像
            # for visited_city_in_last_state in range(1, n):
            for visited_city_in_last_state in range(n):
                # if city2 not in last_state
                if last_state & (1 << visited_city_in_last_state) == 0:
                    continue

                # 从last_state中其中一个节点到`for city in range(1, n)`的距离
                temp_distance = adjacency_matrix[city][visited_city_in_last_state]
                # 如果visited_city_in_last_state不能连上city
                if temp_distance == sys.maxsize:
                    continue

                # 找到能连上city的所有city2中的最短路径
                print(city, visited_city_in_last_state)
                print(state, last_state)
                dp[state][city] = min(dp[state][city], dp[last_state][visited_city_in_last_state] + temp_distance)

    # 全部城市都已访问，而且最后的到达城市不是城市0的所有距离的最小值
    return min(dp[state_size - 1][1:])


class Testing(unittest.TestCase):
    TEST_CASES = [
        # 解释: cost一定是个三元组组成的List，例如[1,2,1]表示从城市1到城市2耗费1
        # 注意: 可能会有重复的路径，例如城市1到城市2有多条路，取最短的一条即可
        # 1->3: 0+2
        # 3->2: 2+1
        # 2->4: 3+3
        # 4->5: 6+4
        # (5, [[1, 2, 9], [2, 3, 1], [3, 4, 9], [4, 5, 4], [2, 4, 3], [1, 3, 2], [5, 4, 9]], 10),
        (3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]], 3),
    ]

    def test_dfs(self):
        for num_cities, roads, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, dfs_helper(num_cities, roads))

    def test_dp(self):
        for num_cities, roads, expected in deepcopy(self.TEST_CASES):
            self.assertEqual(expected, dp_solution(num_cities, roads))
