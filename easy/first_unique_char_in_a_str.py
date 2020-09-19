import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        # 由于HashMap是无序的，在第一次遍历完s生成每个字符出现次数的HashMap后还要遍历一遍字符串去找到第一个出现次数为1的字符
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1
