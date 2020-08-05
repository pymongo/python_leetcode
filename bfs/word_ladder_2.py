import unittest
import collections
from typing import List, Dict

LOWER_LETTERS = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)


# noinspection PyShadowingBuiltins
def main(begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
    # 1. Build Unordered-Graph
    if begin_word not in word_list:
        word_list.append(begin_word)
    if end_word not in word_list:
        word_list.append(end_word)
    size = len(word_list)
    # 所有单词都是相同的长度
    word_len = len(begin_word)
    # 用哈希表加速判断单词是否在列表中的过程
    words_index = {word: i for i, word in enumerate(word_list)}
    begin_index = words_index[begin_word]
    end_index = words_index[end_word]
    # 索引值是每个单词在单词列表中的下标，邻接矩阵的值表示两个单词之间是否连通
    adjacency_matrix: List[List[int]] = [[0] * size for _ in range(size)]
    for i, word in enumerate(word_list):
        letters = list(word)
        for k in range(word_len):
            origin_letter = letters[k]
            for lower_letter in LOWER_LETTERS:
                letters[k] = lower_letter
                next_word = ''.join(letters)
                if next_word in words_index:
                    j = words_index[next_word]
                    # 0: 不连通, 1: 普通节点的连边, 2: 起点的连边, 3: 终点的连边
                    # value = 1
                    if i == begin_index or j == begin_index:
                        value = 2
                    elif i == end_index or j == end_index:
                        value = 3
                    else:
                        value = 1
                    adjacency_matrix[i][j] = value
                    adjacency_matrix[j][i] = value
            letters[k] = origin_letter
    # print(begin_index, end_index)
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
        for next in range(size):
            if adjacency_matrix[curr][next] == 0:
                continue
            if next not in distance_to_end:
                distance_to_end[next] = distance_to_end[curr] + 1
                queue.append(next)
    print(distance_to_end)

    # 3. 从start开始做DFS，根据distance_to_end，只选择distance_to_end[next] = distance_to_end[curr] + 1的路径
    # BFS适合求最短路径，不适合列出所有方案，DFS(回溯)适合用于列出所有方案
    return []


def bfs_1(begin_word: str, end_word: str, word_list: List[str]) -> int:
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
        # 可以使用一个<word,distance>的HashMap，就不需要分层遍历的这层for
        for _ in range(len(queue)):
            word = queue.popleft()
            chars = list(word)
            for i in range(word_len):
                # 保存将要改动单词中的字符
                origin_char = chars[i]
                # 枚举所有小写字母，将单词第i个字符改为枚举的小写字母
                for letter in LOWER_LETTERS:
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
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], [
            ["hit", "hot", "dot", "dog", "cog"],
            ["hit", "hot", "lot", "log", "cog"]
        ]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
    ]

    def test_bfs_1(self):
        for begin_word, end_word, word_list, shortest_path in self.TEST_CASES:
            self.assertCountEqual(shortest_path, main(begin_word, end_word, word_list))
