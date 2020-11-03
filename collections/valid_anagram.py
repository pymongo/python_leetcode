import unittest
import collections


# anagram: 相同字母异序词，易位构词，变位词
# anagram: 如果两个字符串在更改字符顺序后它们可以相同，则两个字符串互为anagram
# 既然每个字母的出现个数要相同，那HashSet就不够用了，要用Counter了
# 排序后比较的时间复杂度O(nlogn)就不如Counter的O(n)时间复杂度了
class Solution:
    # noinspection PyMethodMayBeStatic,PyPep8Naming
    def isAnagram(self, source: str, target: str) -> bool:
        return collections.Counter(source) == collections.Counter(target)

    @staticmethod
    def counter_optimize(source: str, target: str) -> bool:
        """
        性能不如比较两个Counter
        """
        source_counter = collections.Counter(source)

        for letter in target:
            if letter in source_counter:
                if source_counter[letter] == 1:
                    # 这里的pop操作很耗时
                    source_counter.pop(letter)
                else:
                    source_counter[letter] -= 1
            else:
                return False
        # 如果source_counter为空
        return not source_counter

    @staticmethod
    def xor_solution(source: str, target: str) -> bool:
        """
        性能不如比较两个Counter
        """
        xor, ord_sum = 0, 0
        for letter in source:
            ord_letter = ord(letter)
            ord_sum += (ord_letter % 98)
            xor ^= ord_letter
        for letter in target:
            ord_letter = ord(letter)
            ord_sum -= (ord_letter % 98)
            if ord_sum < 0:
                return False
            xor ^= ord_letter
        return xor == 0 and ord_sum == 0

        # xor1, ord_sum1 = 0, 0
        # for letter in source:
        #     ord_letter = ord(letter)
        #     xor1 ^= ord_letter
        #     ord_sum1 += (ord_letter % 98)
        # xor2, ord_sum2 = 0, 0
        # for letter in target:
        #     ord_letter = ord(letter)
        #     xor2 ^= ord_letter
        #     ord_sum2 += (ord_letter % 98)
        # return xor1 == xor2 and ord_sum1 == ord_sum2

    @staticmethod
    def rolling_hash(source: str, target: str) -> bool:
        """
        FIXME rolling_hash的特性是字母会有序，所以这题用不了rollingHash
        """
        source_hash = 0
        for letter in source:
            ord_letter = ord(letter) - 98
            source_hash = (source_hash * 26 + ord_letter) % 100000
        target_hash = 0
        for letter in target:
            ord_letter = ord(letter) - 98
            target_hash = (target_hash * 26 + ord_letter) % 100000
        return source_hash == target_hash


class Testing(unittest.TestCase):
    TESTCASES = [
        ("aacc", "ccac", False),
        ("rat", "car", False),
        ("eat", "tea", True),
    ]

    def test_is_anagram(self):
        solution = Solution()
        for source, target, is_anagram in self.TESTCASES:
            self.assertEqual(is_anagram, solution.isAnagram(source, target))
