import unittest
from typing import List
import collections
import heapq


# dijkstra可以理解为: BFS+优先队列+贪心
class Solution(unittest.TestCase):
    TEST_CASES = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
    ]

    def test(self):
        for times, n, k, expected in self.TEST_CASES:
            self.assertEqual(expected, self.dijkstra(times, n, k))

    @staticmethod
    def dijkstra(times: List[List[int]], n: int, k: int) -> int:
        """
        @param times: 每项例如[2,1,1]表示有向图从节点2到节点1，路径为1
        @param n: 节点的总数
        @param k: 起点
        @return: 从节点k出发(扩散)需要多久才能访问到最远的节点，如果不能扩散到所有节点则返回-1
        dijkstra的贪心过程简单解释:
        例如A-B-C互连的无向图A-B路径为20, A-C路径为30, B-C路径为15
        Round 1: 取出A所有连边中最短的A-B(20)，然后更新visited_distance表: {A:0,B:inf,C:inf} -> {A:20,B:20,C:inf}
        Round 2: 取B所有连边，由于A已被seen，所以只会取到A-C(15)，将A-B-C(35)入队
        Round 3: 发现堆中到C的更短路径其实是Round 1已入队的A-C(30)，所以最终A到C的最短路径是30
        """
        graph = collections.defaultdict(list)
        for node, next_node, distance in times:
            graph[node].append((next_node, distance))

        # 注意优先队列Tuple要让距离放在第一位
        pq = [(0, k)]
        # 兼任dijkstra算法中seen和distance表的作用
        visited_distance = dict()
        while pq:
            distance, node = heapq.heappop(pq)
            if node in visited_distance:
                continue
            visited_distance[node] = distance
            for neighbor, next_distance in graph[node]:
                if neighbor not in visited_distance:
                    heapq.heappush(pq, (distance + next_distance, neighbor))
        return max(visited_distance.values()) if len(visited_distance) == n else -1
