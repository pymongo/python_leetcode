"""
alien_dictionary这题用的还是拓补排序的模板
不过deque要换成heapq，Java中是把Queue换成PriorityQueue
Python中heapq本身不是优先队列，但是可以实现优先队列的效果
deque也是如此，本身deque不是栈，但是也能实现栈的效果(因为是双端队列)

在理解本题前需要先理解verifying_an_alien_dictionary一题
verifying_an_alien_dictionary给出某种语言的字母排序以及单词列表，判断单词列表是否有序
而这题给出的是有序的单词列表，然后推出该语言的字母排序
https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
"""
import unittest
from typing import List


def bfs(words: List[str]) -> str:
    pass


class Testing(unittest.TestCase):
    TEST_CASES = [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
    ]

    def test(self):
        for words, order in self.TEST_CASES:
            self.assertEqual(order, bfs(words))
