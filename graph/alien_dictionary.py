"""
alien_dictionary这题用的还是拓补排序的模板
不过deque要换成heapq，Java中是把Queue换成PriorityQueue
Python中heapq本身不是优先队列，但是可以实现优先队列的效果
deque也是如此，本身deque不是栈，但是也能实现栈的效果(因为是双端队列)
为什么不用`from queue import PriorityQueue`
PriorityQueue是多线程安全的，PriorityQueue is synchronized and provides locking semantics to support multiple concurrent producers and consumers
算法题基本上是单线程的，锁只会带来额外的性能开销

在理解本题前需要先理解verifying_an_alien_dictionary一题
verifying_an_alien_dictionary给出某种语言的字母排序以及单词列表，判断单词列表是否有序
而这题给出的是有序的单词列表，然后推出该语言的字母排序
https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
"""
import unittest
from binary_tree.binary_tree import dbg
from typing import List, Optional, Dict, Set
import heapq


def build_graph_from_words(words: List[str]) -> Optional[Dict[str, Set[str]]]:
    # key<char>: node/vertex, value<HashSet<char>>: edges/neighbors
    graph: Dict[str, Set[str]] = dict()
    # initialize graph
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = set()
    # add edges
    words_size = len(words)
    last_word_size = len(words[0])
    for i in range(1, words_size):
        # dbg(i)
        curr_word_size = len(words[i])
        common_word_size = min(last_word_size, curr_word_size)
        for j in range(common_word_size):
            last_word_char, curr_word_char = words[i - 1][j], words[i][j]
            # dbg((words[i-1], words[i]))
            # dbg((last_word_char, curr_word_char))
            # 只能确认第一个不相同字母的先后顺序
            if last_word_char != curr_word_char:
                graph[last_word_char].add(curr_word_char)
                break
            if j == common_word_size - 1:
                # 前面公共的字母顺序都相同，但是前一个单词的字母更多，不符合排序
                if last_word_size > curr_word_size:
                    return None
        last_word_size = curr_word_size
    return graph


def topological_sort(graph: Dict[str, Set[str]]) -> str:
    # print(graph)
    indegree: Dict[str, int] = {vertex: 0 for vertex in graph}
    vertex_count = 0
    for vertex in graph:
        vertex_count += 1
        for neighbor in graph[vertex]:
            indegree[neighbor] += 1

    # 为什么要用heapq? 如果有多个度为0的顶点，则用堆排序将字母较小的优先弹出，达到题目要求的最小字典序的要求(有多个拓扑序，则返回开头字母更小)
    # 注意我们常用的堆排序模板中，heappop()通常是从大到小弹出，而heapq.heappop则是从小到大弹出
    heap_queue = []
    for vertex in indegree:
        if indegree[vertex] == 0:
            heapq.heappush(heap_queue, vertex)
    lexicographical_order: List[str] = []
    lexicographical_order_size = 0
    while heap_queue:
        vertex = heapq.heappop(heap_queue)
        # print(vertex)
        lexicographical_order.append(vertex)
        lexicographical_order_size += 1
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap_queue, neighbor)
    if lexicographical_order_size < vertex_count:
        return ""
    else:
        return "".join(lexicographical_order)


def bfs(words: List[str]) -> str:
    graph = build_graph_from_words(words)
    if not graph:
        return ""
    return topological_sort(graph)


class Testing(unittest.TestCase):
    TESTCASES = [
        (["z", "x"], "zx"),
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    ]

    def test(self):
        for words, order in self.TESTCASES:
            print("words", words)
            self.assertEqual(order, bfs(words))
