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


# https://lintcode.com/problem/window-sum/
# 这种简单题用Rust的window API一行就能搞定，可惜lintcode不支持Rust
def window_sum(nums: List[int], k: int) -> List[int]:
    """
    TEST_CASES = [
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


# https://leetcode.com/problems/delete-node-in-a-linked-list/
def delete_node_in_a_linked_list(node):
    node.val = node.next.val
    node.next = node.next.nex
