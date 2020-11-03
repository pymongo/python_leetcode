from typing import List


# https://www.lintcode.com/problem/digit-counts/description
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
