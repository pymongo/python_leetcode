"""
本题有三种解法: BFS、DFS、并查集
并查集用来解决连通性问题，简单来说数图中有几个环，例如本题中数朋友圈的总数
# 解读邻接矩阵
Example1:
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 1]]
首先邻接矩阵有几个特性:
1. 矩阵的长和宽相等
2. 对于无向图而言，矩阵关于对角线对称(左上到右下的对角线)，而且对角线上的值全相等
本题的邻接矩阵对角线全是1，表示每个同学自己是自己的朋友，就算没朋友自己一个人能组成一个朋友圈
可以联想到状态转移图中，一个节点绕一圈又连向自己
根据无向图的邻接矩阵特征，其实我们遍历矩阵的除对角线以外的上三角区域即可
所以Example1的图可以脑补为节点0,1,2有条边自连接，然后节点0和节点1相连
"""

import unittest
import collections
from typing import List, Set
from copy import deepcopy


def union_find():
    pass


# 临摹(照抄)了leetcode上BFS的解答
def my_bfs(m: List[List[int]]) -> int:
    # 邻接矩阵肯定是个"正方形"
    circles_count = 0
    size = len(m[0])

    visited = set()
    q = collections.deque()

    for node in range(size):
        if node in visited:
            continue
        q.append(node)
        while q:
            curr_node: int = q.popleft()
            visited.add(curr_node)
            for neighbourhood in range(1, size):
                if m[curr_node][neighbourhood] == 0:
                    continue
                if neighbourhood not in visited:
                    q.append(neighbourhood)
        # 队列为空时，一个节点以及它所有的邻居都被访问过，然后朋友圈+1
        circles_count += 1
    return circles_count


# 可以看到DFS和BFS的核心处理过程基本是一样的，只不过是队列(BFS)和栈代(DFS)替递归
def my_dfs(m: List[List[int]], size: int, visited, node: int):
    # 因为range是从0开始的，所以第一个neighbourhood就是自己
    # 不用看第一个节点，因为第一层递归就已经遍历过第一个点和其它点的连接状况
    for neighbourhood in range(1, size):
        if neighbourhood in visited:
            continue
        if m[node][neighbourhood] == 0:
            continue
        visited.add(neighbourhood)
        my_dfs(m, size, visited, neighbourhood)


# DFS解法耗时: 216ms, 而BFS解法耗时: 324ms, 在数圈圈问题上DFS更优
def my_dfs_entrance(m: List[List[int]]) -> int:
    size = len(m)
    visited = set()
    circles_count = 0
    for node in range(size):
        if node in visited:
            continue
        my_dfs(m, size, visited, node)
        circles_count += 1
    return circles_count


class Testing(unittest.TestCase):
    TEST_CASES = [
        ([[1, 1, 0],
          [1, 1, 0],
          [0, 0, 1]], 2),
        ([[1, 1, 0],
          [1, 1, 1],
          [0, 1, 1]], 1),
    ]

    def test_my_bfs(self):
        for adjacency_matrix, friend_circles_count in deepcopy(self.TEST_CASES):
            self.assertEqual(friend_circles_count, my_bfs(adjacency_matrix))

    def test_my_dfs(self):
        for adjacency_matrix, friend_circles_count in deepcopy(self.TEST_CASES):
            self.assertEqual(friend_circles_count, my_dfs_entrance(adjacency_matrix))
