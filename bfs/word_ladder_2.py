import unittest
import collections
from typing import List, Dict, Set

LOWER_LETTERS = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)


# noinspection PyShadowingBuiltins
# 邻接矩阵List[List[bool]]:              4668ms, 302.2MB, 5%
# 邻接表Dict[node<int>, Set[node<int>]]: 560 ms, 21.4MB, 51%
def word_ladder_2(begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
    # 1. Build Unordered-Graph
    if begin_word not in word_list:
        word_list.append(begin_word)
    if end_word not in word_list:
        return []
    # size = len(word_list)
    # 所有单词都是相同的长度
    word_len = len(begin_word)
    # 用哈希表加速判断单词是否在列表中的过程
    words_index = {word: i for i, word in enumerate(word_list)}
    begin_index = words_index[begin_word]
    end_index = words_index[end_word]
    # print(word_list)
    # print(words_index)
    # 索引值是每个单词在单词列表中的下标，邻接矩阵的值表示两个单词之间是否连通
    # 单词数量比较多，用邻接表(HashMap[node][neighbors])性能比邻接矩阵更高
    # adjacency_matrix: List[List[bool]] = [[False] * size for _ in range(size)]
    graph: Dict[int, Set[int]] = dict()
    for i, word in enumerate(word_list):
        letters = list(word)
        for k in range(word_len):
            origin_letter = letters[k]
            for lower_letter in LOWER_LETTERS:
                if lower_letter == origin_letter:
                    continue
                letters[k] = lower_letter
                next_word = ''.join(letters)
                if next_word in words_index:
                    j = words_index[next_word]
                    if i not in graph:
                        graph[i] = set()
                    graph[i].add(j)
                    # adjacency_matrix[i][j] = True
                    # adjacency_matrix[j][i] = True
            letters[k] = origin_letter
    # 如果没有边连向终点
    if end_index not in graph:
        return []
    # if not any(adjacency_matrix[end_index]):
    #     return []
    # for row in range(size):
    #     for col in range(size):
    #         print(adjacency_matrix[row][col], end=', ')
    #     print()

    # 2. 从end开始做一次BFS，记录每个节点到end的最短距离
    distance_to_end: Dict[int, int] = {end_index: 0}
    queue = collections.deque()
    queue.append(end_index)
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if next in distance_to_end:
                continue
            distance_to_end[next] = distance_to_end[curr]+1
            queue.append(next)
        # for next in range(size):
        #     if not adjacency_matrix[curr][next]:
        #         continue
        #     # 这是必背必理解的BFS求所有点到某个点的最短距离的代码模板
        #     # 跟朋友圈一题的BFS模板相同，做完朋友圈这题就完了朋友圈的BFS模板，不应该啊
        #     if next not in distance_to_end:
        #         distance_to_end[next] = distance_to_end[curr] + 1
        #         queue.append(next)
    # for key in distance_to_end:
    #     print(word_list[key], distance_to_end[key])

    # 3. 从start开始做DFS，根据distance_to_end，只选择distance_to_end[next] = distance_to_end[curr] + 1的路径
    # BFS适合求最短路径，不适合列出所有方案，DFS(回溯)适合用于列出所有方案
    results = []

    def dfs(curr_node: int, path: List[int]):
        if curr_node == end_index:
            results.append([word_list[node] for node in path])
            return
        curr_distance_to_end = distance_to_end[curr_node]
        for next_node in graph[curr_node]:
            # 如果不是最短路径方案(到end的距离应该是每走一步就-1)
            if distance_to_end[next_node] != curr_distance_to_end - 1:
                continue
            path.append(next_node)
            dfs(next_node, path)
            path.pop()

    dfs(begin_index, [begin_index])
    # print(results)
    return results


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("hot", "dog", ["hot", "dog"], []),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"]
        ]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
    ]

    def test_bfs_dfs(self):
        for begin_word, end_word, word_list, shortest_path in self.TEST_CASES:
            self.assertCountEqual(shortest_path, word_ladder_2(begin_word, end_word, word_list))
