import unittest
from typing import List


def rev(chars: List[str], start: int, end: int):
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1


# 先翻转每个字符串再翻转单词
def reverse_words(s: str) -> str:
    # if not s:
    #     return s
    chars = list(s)
    output = []
    size = len(chars)
    rev(chars, 0, size - 1)

    # 末尾要加一个空格，防止最后一个单词没被识别
    chars.append(' ')
    size += 1

    word_start = 0
    while word_start < size and chars[word_start] == ' ':
        word_start += 1
    i = word_start + 1
    while i < size:
        if chars[i] == ' ':
            # 发现一个单词
            for k in range(i - 1, word_start - 1, -1):
                output.append(chars[k])
            output.append(' ')
            word_start = i + 1
            while word_start < size and chars[word_start] == ' ':
                word_start += 1
            i = word_start
        i += 1
    # 去掉末尾的空格
    if len(output) > 0:
        output.pop()
    return ''.join(output)

class Testing(unittest.TestCase):
    TEST_CASES = [
        "the sky is blue",
        "  hello    world!  ",
    ]

    def test_reverse_words(self):
        for s in self.TEST_CASES:
            # 其它语言中strip也叫trim，用于去掉头尾的多余空格
            # expected: str = ' '.join(reversed(s.strip().split()))
            # 如果有多个空格, split也会当成一个
            expected: str = ' '.join(reversed(s.split()))
            self.assertEqual(expected, reverse_words(s))
