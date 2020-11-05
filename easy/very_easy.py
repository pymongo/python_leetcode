import unittest
import collections
from typing import List


# https://lintcode.com/problem/digit-counts/description
# noinspection PyPep8Naming
def digitCounts(k: int, n: int) -> int:
    """
    计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值

    k = 1, n = 12
    输出：5
    解释：在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 中，我们发现 1 出现了 5 次 (1, 10, 11, 12)(注意11中有两个1)。

    例如想批量地数10*k..10*(k+1)，难以找到迭代代码，难以解决边界或特殊的k=0
    最终还是直接把0..n+1拼成字符串，再去数更好
    """
    return str(list(range(n + 1))).count(str(k))


# https://leetcode.com/problems/fizz-buzz/
# 由于这题逻辑比较简单，还有一个多线程版本的follow up，适合用来入门Leetcode多线程题(但只支持C/Java/Python三种语言)
# noinspection PyPep8Naming
def fizzBuzz(n):
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0:
            if num % 5 == 0:
                result.append("fizz buzz")
            else:
                result.append("fizz")
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(num))
    return result


# https://leetcode.com/problems/jewels-and-stones/
# noinspection PyPep8Naming
def JewelsInStones(J: str, S: str) -> int:
    jewels = set(J)
    count = 0
    for stone in S:
        if stone in jewels:
            count += 1
    return count
    # 以下是网友分享的一行解法
    # return sum(S.count(i) for i in J)


# https://leetcode.com/problems/running-sum-of-1d-array/
def running_sum_of_1d_array(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums


# https://lintcode.com/problem/window-sum/
# 这种简单题用Rust的window API一行就能搞定，可惜lintcode不支持Rust
def window_sum(nums: List[int], k: int) -> List[int]:
    """
    TESTCASES = [
        ([1, 2, 7, 8, 5], 3, [10, 17, 20]),
        ([1, 2, 7, 7, 2], 3, [10, 16, 16]),
    ]
    """
    size = len(nums)
    res = []
    if size == 0:
        return res

    left = 0
    curr_sum = 0
    for i in range(left, k - 1):
        curr_sum += nums[i]

    for right in range(k - 1, size):
        curr_sum += nums[right]
        res.append(curr_sum)

        curr_sum -= nums[left]
        left += 1
    return res


# https://lintcode.com/problem/find-the-number/
def find_the_number(nums: int, k: int) -> bool:
    return k in nums


# https://leetcode.com/problems/shuffle-string/
# 类似循环移位字符串那题(rotate_string)
# 同样可以联想成「教室换座位的」
def shuffle_string(s: str, indices: List[int]) -> str:
    chars = list(s)
    output = chars.copy()
    for i, each in enumerate(indices):
        output[each] = chars[i]
    return ''.join(output)


def first_unique_char(s: str) -> int:
    counter = collections.Counter(s)
    # 由于HashMap是无序的，在第一次遍历完s生成每个字符出现次数的HashMap后还要遍历一遍字符串去找到第一个出现次数为1的字符
    for i, char in enumerate(s):
        if counter[char] == 1:
            return i
    return -1


class Unittest(unittest.TestCase):
    def test_shuffle_string(self):
        testcases = [
            ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
        ]
        for s, indices, output in testcases:
            self.assertEqual(output, shuffle_string(s, indices))
