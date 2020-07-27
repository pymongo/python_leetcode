import unittest
from typing import List


def is_words_in_order(words: List[str], order: str) -> bool:
    """
    有一种拉丁系语言的26个字母按order
    判断入参中单词列表是否该语言的字母顺序排序？
    例如字母顺序是abcd，那么d开头的单词如果在a开头的单词的后面，就返回True，否则返回False
    我的思路: 题目入参限定了每个单词最大长度是20，那么加上预处理把所有单词补长为字符串(超过i32长度了)
    """
    size = len(words)
    if size <= 1:
        return True
    # key: alphabet in order, value: index(priority) of alphabet
    alphabet_priority = dict()
    for i, char in enumerate(order):
        alphabet_priority[char] = i
    last_size = len(words[0])
    # 两两比较(冒泡)是否有序
    for i in range(1, size):
        curr_size = len(words[1])
        for k in range(min(last_size, curr_size)):
            if alphabet_priority[words[i][k]] == alphabet_priority[words[i - 1][k]]:
                continue
            # 只有当单词字母出现不相等时才需要判断权重
            if alphabet_priority[words[i][k]] < alphabet_priority[words[i - 1][k]]:
                return False
            # 比一个不相等的首字母就够了
            break
        # 如果for循环没有break
        else:
            # 如果前后两个单词的前面部分一样，例如apple, app
            if last_size > curr_size:
                return False
        last_size = curr_size
    return True


class Testing(unittest.TestCase):
    TEST_CASE = [
        (["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz", True),
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        # 然后根据词典编纂规则 "apple" > "app", 因为第四位l>空字符串，所以apple应该在app后面
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ]

    def test(self):
        for words, order, expected in self.TEST_CASE:
            print(words)
            self.assertEqual(expected, is_words_in_order(words, order))
