import unittest
import collections
from typing import List


class Solution:
    LOWER_LETTERS = [chr(ord('a') + i) for i in range(26)]

    # 388 ms 在所有 Python3 提交中击败了 37.04%，更快的解答只能用双向BFS了
    # def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
    def bfs_1(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if not word_list:
            return 0

        # 将List转为HashSet提高查询单词的效率
        word_set = set(word_list)
        # 如果提交到lintcode，因为lintcode上end_word可以不在word_list上，为了统一解答还得把它加进去
        # word_set.add(end_word)
        if end_word not in word_set:
            return 0

        queue = collections.deque()
        queue.append(begin_word)
        visited = set(begin_word)
        # 只要是BFS搜索出来的就一定是最短路径(最少步数)
        step = 1

        # 所有单词都有相同长度
        word_len = len(begin_word)

        while queue:
            # 分层遍历类型题必有的模板语句: for _ in range(len(queue))
            # 与之对应的不分层遍历，例如克隆图就没有这一层，不过不分层遍历可以加上这一层
            for _ in range(len(queue)):
                word = queue.popleft()
                chars = list(word)
                for i in range(word_len):
                    # 保存将要改动单词中的字符
                    origin_char = chars[i]
                    # 枚举所有小写字母，将单词第i个字符改为枚举的小写字母
                    for letter in self.LOWER_LETTERS:
                        chars[i] = letter
                        next_word = ''.join(chars)
                        if next_word in word_set:
                            if next_word == end_word:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    # 穷举下一位字母前，复原单词
                    chars[i] = origin_char
            # 访问完当前节点的所有邻居，步数+1
            step += 1
        return 0


class Testing(unittest.TestCase):
    TEST_CASES = [
        ("a", "c", ["b"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ]

    def test_bfs_1(self):
        solution = Solution()
        for begin_word, end_word, word_list, shortest_length in self.TEST_CASES:
            self.assertEqual(shortest_length, solution.bfs_1(begin_word, end_word, word_list))
