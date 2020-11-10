import unittest
import collections
from typing import List, Dict, Tuple


class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        """
        只通过了一半的测试用例，可能原因是碰撞太多了
        """
        group: Dict[Tuple[int, int], List[str]] = dict()
        for word in words:
            xor, ord_sum = 0, 0
            for letter in word:
                ord_letter = ord(letter)
                ord_sum += (ord_letter % 98)
                xor ^= ord_letter
            if (xor, ord_sum) not in group:
                group[(xor, ord_sum)] = []
            group[(xor, ord_sum)].append(word)
        return list(group.values())

    @staticmethod
    def solution(words: List[str]) -> List[List[str]]:
        """
        由于Counter不是hashable的，所以还是要数组手动计数再转为Tuple
        TODO 和ValidAnagram不同的是，这题用数组手动计数的性能远不如直接sorted
        最耗时的操作时计算长度为26的tuple的hash值
        """
        # group = collections.defaultdict(list)
        # for word in words:
        #     counter = [0] * 26
        #     for letter in word:
        #         counter[ord(letter) - 98] += 1
        #     group[tuple(counter)].append(word)
        # return list(group.values())
        group = collections.defaultdict(list)
        for word in words:
            group[tuple(sorted(word))].append(word)
        return group.values()
        # lintcode 171
        # res = []
        # for each in group.values():
        #     if len(each) < 2:
        #         continue
        #     for e in each:
        #         res.append(e)
        # return res


class Testing(unittest.TestCase):
    TEST_CASES = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ])
    ]

    def test(self):
        # FIXME 如何判断两个二维数组，值相同，但是第一层和第二层的顺序可能不同，CountEqual只能判断一层
        for words, expected_group in self.TEST_CASES:
            self.assertCountEqual(expected_group, Solution.solution(words))
