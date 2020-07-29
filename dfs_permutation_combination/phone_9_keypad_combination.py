import unittest
from typing import List, Tuple, Union
import collections

# "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
numeric_keypad: List[Union[None, Tuple[str, str, str], Tuple[str, str, str, str]]] = [
    None,
    None, ('a', 'b', 'c'), ('d', 'e', 'f'),
    ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'),
    ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')
]

keypad_mapping = {'2': ('a', 'b', 'c'),
                  '3': ('d', 'e', 'f'),
                  '4': ('g', 'h', 'i'),
                  '5': ('j', 'k', 'l'),
                  '6': ('m', 'n', 'o'),
                  '7': ('p', 'q', 'r', 's'),
                  '8': ('t', 'u', 'v'),
                  '9': ('w', 'x', 'y', 'z')}


# 本题的组合，更像是多个字符数组之间的product(笛卡尔积)，所以不需要去重
def keypad(digits: str) -> List[str]:
    # 预处理，将输入的的字符串转为2-9数字组成的List[int]
    results: List[str] = []
    size = len(digits)
    if size == 0:
        return results
    last_index = size - 1

    q = collections.deque()
    q.append([])
    q.append(None)
    for i in range(size):
        if digits[i] not in keypad_mapping:
            continue
        while True:
            combination = q.popleft()
            if combination is None:
                q.append(None)
                break
            for letter in keypad_mapping[digits[i]]:
                temp = combination.copy()
                temp.append(letter)
                if i == last_index:
                    results.append("".join(temp))
                else:
                    q.append(temp)
    return results

class Testing(unittest.TestCase):
    TEST_CASES = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("5", ["j", "k", "l"]),
    ]

    def test_keypad(self):
        for digits, combinations in self.TEST_CASES:
            self.assertCountEqual(combinations, keypad(digits))
