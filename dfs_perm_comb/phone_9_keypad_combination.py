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
        # 这里不用判断是否在2-9的范围，如果不是，`for letter in keypad_mapping[digits[i]]`这句就是个空循环
        # if digits[i] not in keypad_mapping:
        #     continue
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


# 不用queue 通过last_combs/curr_combs 生成product笛卡尔积
# 性能比用queue的遍历快一丢丢
def bfs_2(digits: str) -> List[str]:
    results = []
    size = len(digits)
    if size == 0:
        return results
    # combs = combinations
    last_combs = [[]]
    for digit in digits:
        curr_combs = []
        for last_comb in last_combs:
            for letter in keypad_mapping[digit]:
                curr_comb = last_comb.copy()
                curr_comb.append(letter)
                curr_combs.append(curr_comb)
        last_combs = curr_combs.copy()
    for comb in last_combs:
        results.append("".join(comb))
    return results


# 考虑List[List[str]]效率可能不如字符串拼接(copy操作太多了)，来个字符串拼接的版本试试
def bfs_3(digits: str) -> List[str]:
    if not digits:
        return []
    last_combs = [""]
    for digit in digits:
        curr_combs = []
        for last_comb in last_combs:
            for letter in keypad_mapping[digit]:
                curr_combs.append(last_comb + letter)
        last_combs = curr_combs.copy()
    return last_combs


def dfs(combination, digits, results: List[str]):
    if not digits:
        results.append(combination)
        return
    next_digits = digits[1:]
    for letter in keypad_mapping[digits[0]]:
        dfs(combination + letter, next_digits, results)


def def_helper(digits: str) -> List[str]:
    if not digits:
        return []
    results = []
    dfs("", digits, results)
    return results


class Testing(unittest.TestCase):
    TESTCASES = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("5", ["j", "k", "l"]),
    ]

    def test_keypad(self):
        for digits, combinations in self.TESTCASES:
            self.assertCountEqual(combinations, keypad(digits))
